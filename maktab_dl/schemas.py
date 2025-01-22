from pydantic import BaseModel
from typing import List, Optional


class LoginResponse(BaseModel):
    status: str
    message: str


class UserInfo(BaseModel):
    is_staff: bool = False
    user_id: int | None = None
    email: str | None = None
    phone: str | None = None
    business_admin: bool = False
    team_admin: bool = False
    business_student: bool = False


class CourseModel(BaseModel):
    slug_id: int | None = None
    slug: str = ""
    version_number: int | None = None
    level: Optional[str] = None
    title: str = ""
    heading: str = ""
    type: str = ""
    description: str = ""


class Unit(BaseModel):
    id: int
    title: str = ""
    slug: str = ""
    inactive: bool = False
    attachment: bool = False
    project_required: bool = False
    description: str = ""
    status: bool | str = True
    type: str = ""


class Chapter(BaseModel):
    id: int
    title: str = ""
    slug: str = ""
    unit_set: List[Unit] = []


class CourseChaptersModel(BaseModel):
    total_worth: float | str = 0
    chapters: List[Chapter] = []


class CourseInfo(BaseModel):
    link: str = ""
    course: CourseModel
    chapters: CourseChaptersModel
