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
    image_url: HttpUrl | None = None
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
    id: int
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: Optional[Any] = None
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class Category(BaseModel):
    id: int
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: CategoryParent | None = None
    obj_hash: str | None = None
    obj_type: str | None = None


class Faq(BaseModel):
    id: int
    type: str | None = None
    type_text: str | None = None
    question: str | None = None
    answer: str | None = None


class Teacher(BaseModel):
    description: str
    full_name: str | None = None
    image_url: HttpUrl | None = None
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
    image_url: HttpUrl | None = None
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
    id: int
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class CareerCategory(BaseModel):
    title: str | None = None
    slug: str | None = None
    cover: Optional[HttpUrl] = None
    parent: CareerCategoryParent
    id: int
    obj_hash: str | None = None
    obj_type: str | None = None


class Career(BaseModel):
    slug: str | None = None
    title: str | None = None
    slug_id: int | None = None
    prices: Price | None = None
    discount: float | None = None
    image_url: HttpUrl | None = None
    description: str | None = None
    units_count: int | None = None
    required_hours: int | None = None
    no_of_students: int | None = None
    main_category: CareerCategory | None = None
    organization: CareerOrganization | None = None
    teachers: List[CareerTeacher] = []
    specifics: CareerSpecifics | None = None
    id: int
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
    slug_id: int
    slug: str
    version_number: int
    level: Optional[str]
    title: str
    heading: str
    type: str
    has_rate: bool = False
    can_rate: bool = False
    avg_rating: float | None = None
    poster: HttpUrl
    extra_description: str = ""
    content_grouping: ContentGrouping
    course_effort_time: str = ""
    required_hours: int | str
    content_hours: int | str
    project_hours: int | str
    purchase_expire_duration: int | str
    validation_threshold: float | str
    required_projects: bool = False
    ongoing: bool = False
    versioning_info: List = []
    prices: Price | None = None
    auto_examination: int | str
    internal_links: List = []
    certif_organization: Organization | None = None
    publisher: Organization | None = None
    content_rate_count: int | str
    content_approval: int | str
    publish_status: str = "published"
    is_downloadable: str | bool = "yes"
    certification: bool = False
    business_certification: bool = False
    image: HttpUrl
    image_thumbnail_url: HttpUrl
    view_access: int | str
    view_access_text: str
    has_review: bool = False
    has_subtitle: bool = False
    description: str
    prerequisite_course: List
    video_url: VideoUrl
    categories: Category
    prerequisite_description: str
    product_structured_data: str
    faq_structured_data: Optional[str] = None
    free_units_count: int
    units_count: int
    course_faq: List = []
    general_faq: List[Faq]
    course_progress: Optional[Any] = None
    teachers: List[Teacher]
    course_features: List[CourseFeature]
    related_courses: Dict | list
    is_business_course: bool
    meta_data: MetaData
    learning_goals: List[str]
    assignments_count: int
    projects_count: int
    original_version_id: int
    actions: Action
    careers: List[Career]
    latest_update_date: str
    no_of_students: int
    labels: Labels
    published_date: str
    id: int
    obj_hash: str
    obj_type: str
    is_last_version: bool
    course_foruming: bool
    coupon: Optional[str] = None
    affiliate: Optional[str] = None


class Unit(BaseModel):
    id: int
    title: str
    slug: str
    locked: bool
    locked_action: str
    computed_view_access: int
    inactive: bool
    finished: bool
    attachment: bool
    project_required: bool
    description: str
    status: bool
    type: str
    effort_time_in_minutes: str
    effort_time: float | str
    unit_worth: float | str
    indexing: bool = False
    user_score: Optional[float] = None


class Chapter(BaseModel):
    id: int
    title: str
    slug: str
    units_count: int
    total_effort_time: Optional[str]
    total_lecture_effort_time: Optional[str]
    worth: float | str
    desc: str
    locked: bool
    progress: int | float
    score: int | float
    unit_set: List[Unit]


class CourseChaptersModel(BaseModel):
    total_worth: float | str
    chapters: List[Chapter]


class CourseInfo(BaseModel):
    link: str
    course: CourseModel
    chapters: CourseChaptersModel
