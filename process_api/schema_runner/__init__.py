import json

# Purpose: SchemaRunner class
# Run processes using a json file to define the intent.
# You can register schemas and templates to be used in the json file.
# Templates define reusable processes.
# You can also add a schema to the store if you want to use a greater schema to call other processes.


async def process_parameters(process, parameters, ctx=None):
    parameters_def = process.get("parameters_def")
    schema_parameters = {}

    for parameter_name in parameters_def.keys():
        parameter = parameters_def[parameter_name]
        data_type = parameter.get("type", "string")
        required = parameter.get("required", False)

        value = parameters.get(parameter_name, None)

        if value is None and required:
            raise Exception(f"Parameter '{parameter_name}' is required.")

        if data_type == "string" and isinstance(value, str) is False:
            raise Exception(f"Parameter '{parameter_name}' must be a string.")

        if data_type == "number" and isinstance(value, int) is False:
            raise Exception(f"Parameter '{parameter_name}' must be a number.")

        if data_type == "boolean" and isinstance(value, bool) is False:
            raise Exception(f"Parameter '{parameter_name}' must be a boolean.")

        if data_type == "object" and isinstance(value, dict) is False:
            raise Exception(f"Parameter '{parameter_name}' must be an object.")

        if data_type == "array" and isinstance(value, list) is False:
            raise Exception(f"Parameter '{parameter_name}' must be an array.")

        schema_parameters[parameter_name] = value

    process["parameters"] = schema_parameters


async def run_process(api, schema, process_name, ctx=None, parameters=None):
    process = schema.get(process_name, None)

    # make a copy of the process
    process = process.copy()

    if "parameters_def" in process:
        await process_parameters(process, parameters, ctx=None)
        del process["parameters_def"]

    start_step = process["steps"]["start"]
    await api.run(start_step, ctx, process, None)


async def run_schema(api, schema, ctx=None, parameters=None):
    sequence = schema.get('sequence', None)

    if sequence is not None:
        for process in sequence:
            await run_process(api, schema, process, ctx, parameters)

    elif "main" in schema:
        await run_process(api, schema, "main", ctx, parameters)


async def load_json(file_path):
    try:
        file = open(file_path, 'r')
        json_data = json.load(file)
        file.close()

        return json_data
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


class SchemaRunner:
    templates = {}
    schemas = {}

    async def run_from_file(self, api, filename, ctx=None, parameters=None):
        schema = await load_json(filename)
        await self.run_schema(api, schema, ctx, parameters)

    async def run_schema(self, api, schema, ctx=None, parameters=None):
        await run_schema(api, schema, ctx, parameters)

    async def run_process(self, api, schema, process_name, ctx=None, parameters=None):
        await run_process(api, schema, process_name, ctx, parameters)

    async def add_schema(self, schema):
        name = schema.get('id')
        self.schemas[name] = schema

    async def remove_schema(self, name):
        del self.schemas[name]

    async def clear_schemas(self):
        self.schemas = {}

    async def add_template(self, template):
        name = template.get('id')
        self.templates[name] = template

    async def remove_template(self, name):
        del self.templates[name]

    async def clear_templates(self):
        self.templates = {}

