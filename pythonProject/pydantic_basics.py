import uuid
from pydantic import BaseModel, Field, HttpUrl, EmailStr, computed_field, ValidationError
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str

    @computed_field
    def username(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def get_username(self) -> str:
        return f"{self.firstName} {self.lastName}"

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "title"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str ="description"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course_id",
    title="playwright",
    maxScore=100,
    minScore=10,
    description="playwright",
    estimatedTime="1 week",
    previewFile=FileSchema(
        id="file_id",
        filename="file.png",
        directory="courses",
        url="http://localhost:8000/"
    ),
    createdByUser=UserSchema(
        id="user-id",
        email="user@example.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
)

print(course_default_model)


course_dict = {
    "id": "course_id",
    "title": "playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "playwright",
    "estimatedTime": "1 week",
     "previewFile": {
        "id": "file_id",
        "filename": "file.png",
        "directory": "courses",
        "url":"http://localhost:8000/"
     },
    "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
  }

course_dict_modal = CourseSchema(**course_dict)
print(course_dict_modal)

course_json = """
{
    "id": "course_id",
    "title": "playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "playwright",
    "estimatedTime": "1 week",
     "previewFile": {
        "id": "file_id",
        "filename": "file.png",
        "directory": "courses",
        "url":"http://localhost:8000/"
     },
    "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
"""
course_json_modal = CourseSchema.model_validate_json(course_json)
# print(course_json_modal)
# print(course_json_modal.model_dump(by_alias=True))
# print(course_json_modal.model_dump_json(by_alias=True))

user = UserSchema(
        id="user-id",
        email="user@example.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
)

print(user.get_username())
print(user.username)

