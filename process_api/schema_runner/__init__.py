import json

# Purpose: SchemaRunner class
# Run processes using a json file to define the intent.
# You can register schemas and templates to be used in the json file.
# Templates define reusable processes.
# You can also add a schema to the store if you want to use a greater schema to call other processes.


async def process_parameters(process, parameters, ctx=None):
    parameters_def = process.get("parameters_def")

    pass


async def run_process(api, schema, process_name, ctx=None, parameters=None):
    process = schema.get(process_name, None)

    # make a copy of the process
    process = process.copy()

    if "parameters_def" in process:
        await process_parameters(process, parameters, ctx=None)

    start_step = process["steps"]["start"]
    await api.run(start_step, ctx, process, None)


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


async def run_schema(api, schema, ctx=None, parameters=None):
    sequence = schema.get('sequence', None)
    main = schema.get('main', None)

    if sequence is not None:
        for process in sequence:
            await run_process(api, schema, process, ctx, parameters)

    elif "main" in schema:
        await run_process(api, schema, "main", ctx, parameters)

    pass


class SchemaRunner:
    templates = {}
    schemas = {}

    async def run_from_file(self, api, filename, ctx=None, parameters=None):
        schema = await load_json(filename)
        await self.run_schema(api, schema, ctx, parameters)

    async def run_schema(self, api, schema, ctx=None, parameters=None):
        await run_process(api, schema, "main", ctx, parameters)

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

