from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base import assert_equal
from config import settings
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):

    logger.info(f"Check create file response")

    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"
    assert_equal(response.file.url, expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")