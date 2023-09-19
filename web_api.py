# Status codes
# 200 OK for a successful request with data.
# 201 Created for successful resource creation (e.g., after a POST request).
# 204 No Content for successful requests with no response body (e.g., after a DELETE request).
# 400 Bad Request for client errors (e.g., invalid input data).
# 401 Unauthorized for authentication errors.
# 403 Forbidden for authorization errors.
# 404 Not Found for resource not found errors.
# 500 Internal Server Error for server errors.
from enum import Enum

from fastapi import FastAPI
from process_api.web_api.data import register as register_data
from process_api import process_api
import logging

# Configure the logging
logging.basicConfig(
    filename='myapp.log',  # Specify the log file name
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("test")

app = FastAPI()

register_data(app, process_api, logger)


@app.get("/")
async def root():
    return {"message": "Hello World"}

