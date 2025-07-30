from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any


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


class Organization(BaseModel):
    organization_id: int | None = None
    name: str | None = None
    image_url: HttpUrl | None | str = None
    slug: str | None = None


class ContentGrouping(BaseModel):
    index: str | None = None
    name: str | None = None


class Price(BaseModel):
    real: int | None = None
    discounted: float | None = None


class VideoUrl(BaseModel):
    lq: HttpUrl | None = None
    hq: HttpUrl | None = None
    caption: str | None = None


class CategoryParent(BaseModel):
    id: int | None = None
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: Optional[Any] = None
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class Category(BaseModel):
    id: int | None = None
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: CategoryParent | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class Faq(BaseModel):
    id: int | None = None
    type: str | None = None
    type_text: str | None = None
    question: str | None = None
    answer: str | None = None


class Teacher(BaseModel):
    description: str = ""
    full_name: str | None = None
    image_url: HttpUrl | None | str = None
    landing_view: bool | None = None
    slug: str | None = None
    teacher_id: int | None = None
    student_count: int | None = None
    course_count: int | None = None
    id: int | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class CourseFeature(BaseModel):
    id: int
    modified_date: str | None = None
    created_date: str | None = None
    title: str | None = None
    description: str | None = None
    tiny_title: str | None = None
    tiny_description: str | None = None
    image: HttpUrl | None = None
    importance: int | None = None
    pricing_pop_up: bool | None = None


class MetaData(BaseModel):
    indexing: bool | None = None
    title: str | None = None
    description: str | None = None
    keywords: Optional[str] = None
    og_title: str | None = None
    og_description: str | None = None
    og_image: HttpUrl | None = None
    og_video: HttpUrl | None = None
    price: int | None = None
    product_id: int | None = None
    canonical_address: HttpUrl | None = None


class CareerOrganization(BaseModel):
    slug: str | None = None
    name: str | None = None
    image_url: HttpUrl | None | str = None
    id: int | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class CareerTeacher(BaseModel):
    slug: str | None = None
    full_name: str | None = None
    teacher_id: int | None = None
    landing_view: bool | None = None
    id: int | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class CareerSpecifics(BaseModel):
    courses_count: int | None = None


class CareerCategoryParent(BaseModel):
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: Optional[Any] = None
    id: int | None = None
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class CareerCategory(BaseModel):
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: CareerCategoryParent | None = None
    id: int | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class Career(BaseModel):
    slug: str | None = None
    title: str | None = None
    slug_id: int | None = None
    prices: Price | None = None
    discount: float | None = None
    image_url: HttpUrl | None | str = None
    description: str | None = None
    units_count: int | None = None
    required_hours: int | None = None
    no_of_students: int | None = None
    main_category: CareerCategory | None = None
    organization: CareerOrganization | None = None
    teachers: List[CareerTeacher] = []
    specifics: CareerSpecifics | None = None
    id: int | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class Action(BaseModel):
    call_to_action: str | None = None
    call_to_action_text: str | None = None


class Label(BaseModel):
    key: str | None = None
    value: str | None = None


class Labels(BaseModel):
    main: Optional[Label] = None
    business: Optional[Label] = None


class CourseModel(BaseModel):
    slug_id: int | None = None
    slug: str = ""
    version_number: int = 0
    level: Optional[str] = ""
    title: str = ""
    heading: str = ""
    type: str = ""
    has_rate: bool = False
    can_rate: bool = False
    avg_rating: float | None = None
    poster: HttpUrl | None = None
    extra_description: str = ""
    content_grouping: ContentGrouping | None = None
    course_effort_time: str = ""
    required_hours: int | str = 0
    content_hours: int | str = 0
    project_hours: int | str = 0
    purchase_expire_duration: int | str = 0
    validation_threshold: float | str = 0
    required_projects: bool = False
    ongoing: bool = False
    versioning_info: List = []
    prices: Price | None = None
    auto_examination: int | str = ""
    internal_links: List = []
    certif_organization: Organization | None = None
    publisher: Organization | None = None
    content_rate_count: int | str = ""
    content_approval: int | str = ""
    publish_status: str = "published"
    is_downloadable: str | bool = "yes"
    certification: bool = False
    business_certification: bool = False
    image: HttpUrl | None = None
    image_thumbnail_url: HttpUrl | None = None
    view_access: int | str = ""
    view_access_text: str = ""
    has_review: bool = False
    has_subtitle: bool = False
    description: str = ""
    prerequisite_course: List = []
    video_url: VideoUrl | None = None
    categories: Category | None = None
    prerequisite_description: str = ""
    product_structured_data: str = ""
    faq_structured_data: Optional[str] = None
    free_units_count: int = 0
    units_count: int = 0
    course_faq: List = []
    general_faq: List[Faq] = []
    course_progress: Optional[Any] = None
    teachers: List[Teacher] = []
    course_features: List[CourseFeature] = []
    related_courses: Dict | list | None = None
    is_business_course: bool = False
    meta_data: MetaData | None = None
    learning_goals: List[str] = []
    assignments_count: int = 0
    projects_count: int = 0
    original_version_id: int = 0
    actions: Action | None = None
    careers: List[Career] = []
    latest_update_date: str|None = ""
    no_of_students: int = 0
    labels: Labels | None = None
    published_date: str|None = ""
    id: int | None = None
    obj_hash: str = ""
    obj_type: str = ""
    is_last_version: bool = False
    course_foruming: bool = False
    coupon: Optional[str] = None
    affiliate: Optional[str] = None


class Unit(BaseModel):
    id: int | None = None
    title: str = ""
    slug: str = ""
    locked: bool = False
    locked_action: str = ""
    computed_view_access: int = 0
    inactive: bool = False
    finished: bool = False
    attachment: bool = False
    project_required: bool = False
    description: str = ""
    status: bool = False
    type: str = ""
    effort_time_in_minutes: str
    effort_time: float | str
    unit_worth: float | str
    indexing: bool = False
    user_score: Optional[float] = None


class Chapter(BaseModel):
    id: int | None = None
    title: str = ""
    slug: str = ""
    units_count: int = 0
    total_effort_time: Optional[str] = "0"
    total_lecture_effort_time: Optional[str] = "0"
    worth: float | str = 0
    desc: str = ""
    locked: bool = False
    progress: int | float = 0
    score: int | float = 0
    unit_set: List[Unit]


class CourseChaptersModel(BaseModel):
    total_worth: float | str = 0
    chapters: List[Chapter]


class CourseInfo(BaseModel):
    link: str
    course: CourseModel
    chapters: CourseChaptersModel
