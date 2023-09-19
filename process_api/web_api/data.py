import json

from process_api.modules.data import DataModule
from fastapi import Body


def register(app, process_api, logger):
    DataModule.register(process_api)

    @app.put("/data/{name}")
    async def put_data(name: str, data: str = Body(..., embed=False)):
        parsed_data = json.loads(data)

        await process_api.call("data", "load", {"name": name, "source": parsed_data})

        return {
            "status_code": 201,
            "message": f"Data {name} loaded successfully",
        }

    @app.get("/data/{name}")
    async def get_data(name: str):
        try:
            data = process_api.call("data", "get", {"name": name})

            return {
                "status_code": 200,
                "message": f"Data {name} fetched successfully",
                "data": data,
            }
        except Exception as e:
            logger.error(e)

            return {
                "status_code": 404,
                "message": f"Data {name} not found",
                "error": str(e),
            }
