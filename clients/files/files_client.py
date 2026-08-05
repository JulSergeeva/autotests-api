from pathlib import Path
from clients.api_client import APIClient
from httpx import Response

from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class FilesClient(APIClient):
    def get_file_api(self, file_id: str) -> Response:
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        # Преобразуем входящий путь в Path-объект
        file_path = Path(request.upload_file)

        # Если путь относительный — резолвим его относительно корня проекта
        if not file_path.is_absolute():
            file_path = PROJECT_ROOT / file_path

        # Открываем и гарантированно закрываем файл с помощью context manager
        with open(file_path, "rb") as file_bytes:
            return self.post(
                "/api/v1/files",
                data=request.model_dump(by_alias=True, exclude={'upload_file'}),
                files={"upload_file": file_bytes}
            )

    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
