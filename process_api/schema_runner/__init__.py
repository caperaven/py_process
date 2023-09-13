import json

# Purpose: SchemaRunner class
# Run processes using a json file to define the intent.
# You can register schemas and templates to be used in the json file.
# Templates define reusable processes.
# You can also add a schema to the store if you want to use a greater schema to call other processes.

async def process_parameters(process, param_def, parameters):
    parameters_def = process.get("parameters_def")

    pass


async def run_process(api, process, parameters):
    # make a copy of the process
    process = process.copy()

    if "parameters_def" in process:
        await process_parameters(process, parameters)
    pass


async def load_json(filename):
    with open(filename, 'r') as json_file:
        data_dict = json.load(json_file)
        return data_dict


async def run_schema(api, json):
    sequence = json.get('sequence', None)
    main = json.get('main', None)

    if sequence is not None:
        for process in sequence:
            instance = json.get(process, None)
            if instance is not None:
                await run_process(api, instance)

    elif main is not None:
        await run_process(api, main)

    pass


class SchemaRunner:
    templates = {}
    schemas = {}

    async def run_from_file(self, api, filename, ctx=None):
        schema = await load_json(filename)
        return schema

    async def run_schema(self, api, json):
        await run_process(api, json)

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

