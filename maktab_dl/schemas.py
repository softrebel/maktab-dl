from pydantic import BaseModel,HttpUrl
from typing import List, Optional, Dict, Any



class LoginResponse(BaseModel):
    status: str
    message: str


class UserInfo(BaseModel):
    is_staff: bool
    user_id: int
    email: str
    phone: str
    business_admin: bool
    team_admin: bool
    business_student: bool


class Organization(BaseModel):
    organization_id: int
    name: str
    image_url: HttpUrl
    slug: str


class ContentGrouping(BaseModel):
    index: str
    name: str


class Price(BaseModel):
    real: int
    discounted: float


class VideoUrl(BaseModel):
    lq: HttpUrl
    hq: HttpUrl
    caption: str


class CategoryParent(BaseModel):
    id: int
    title: str
    slug: str
    cover: Optional[HttpUrl] = None
    parent: Optional[Any] = None
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class Category(BaseModel):
    id: int
    title: str
    slug: str
    cover: Optional[HttpUrl] = None
    parent: CategoryParent
    obj_hash: str
    obj_type: str


class Faq(BaseModel):
    id: int
    type: str
    type_text: str
    question: str
    answer: str


class Teacher(BaseModel):
    description: str
    full_name: str
    image_url: HttpUrl
    landing_view: bool
    slug: str
    teacher_id: int
    student_count: int
    course_count: int
    id: int
    obj_hash: str
    obj_type: str


class CourseFeature(BaseModel):
    id: int
    modified_date: str
    created_date: str
    title: str
    description: str
    tiny_title: str
    tiny_description: str
    image: HttpUrl
    importance: int
    pricing_pop_up: bool


class MetaData(BaseModel):
    indexing: bool
    title: str
    description: str
    keywords: Optional[str] = None
    og_title: str
    og_description: str
    og_image: HttpUrl
    og_video: HttpUrl
    price: int
    product_id: int
    canonical_address: HttpUrl


class CareerOrganization(BaseModel):
    slug: str
    name: str
    image_url: HttpUrl
    id: int
    obj_hash: str
    obj_type: str


class CareerTeacher(BaseModel):
    slug: str
    full_name: str
    teacher_id: int
    landing_view: bool
    id: int
    obj_hash: str
    obj_type: str


class CareerSpecifics(BaseModel):
    courses_count: int


class CareerCategoryParent(BaseModel):
    title: str
    slug: str
    cover: Optional[HttpUrl] = None
    parent: Optional[Any] = None
    id: int
    obj_hash: Optional[str] = None
    obj_type: Optional[str] = None


class CareerCategory(BaseModel):
    title: str
    slug: str
    cover: Optional[HttpUrl] = None
    parent: CareerCategoryParent
    id: int
    obj_hash: str
    obj_type: str


class Career(BaseModel):
    slug: str
    title: str
    slug_id: int
    prices: Price
    discount: float
    image_url: HttpUrl
    description: str
    units_count: int
    required_hours: int
    no_of_students: int
    main_category: CareerCategory
    organization: CareerOrganization
    teachers: List[CareerTeacher]
    specifics: CareerSpecifics
    id: int
    obj_hash: str
    obj_type: str


class Action(BaseModel):
    call_to_action: str
    call_to_action_text: str


class Label(BaseModel):
    key: str
    value: str


class Labels(BaseModel):
    main: Optional[Label]
    business: Optional[Label] = None


class CourseModel(BaseModel):
    slug_id: int
    slug: str
    version_number: int
    level: Optional[str]
    title: str
    heading: str
    type: str
    has_rate: bool
    can_rate: bool
    avg_rating: float
    poster: HttpUrl
    extra_description: str
    content_grouping: ContentGrouping
    course_effort_time: str
    required_hours: int | str
    content_hours: int | str
    project_hours: int | str
    purchase_expire_duration: int
    validation_threshold: float
    required_projects: bool
    ongoing: bool
    versioning_info: List
    prices: Price
    auto_examination: int
    internal_links: List
    certif_organization: Organization
    publisher: Organization
    content_rate_count: int
    content_approval: int
    publish_status: str
    is_downloadable: str
    certification: bool
    business_certification: bool
    image: HttpUrl
    image_thumbnail_url: HttpUrl
    view_access: int
    view_access_text: str
    has_review: bool
    has_subtitle: bool
    description: str
    prerequisite_course: List
    video_url: VideoUrl
    categories: Category
    prerequisite_description: str
    product_structured_data: str
    faq_structured_data: Optional[str] = None
    free_units_count: int
    units_count: int
    course_faq: List
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
    effort_time: float
    unit_worth: float
    indexing: bool
    user_score: Optional[float] = None


class Chapter(BaseModel):
    id: int
    title: str
    slug: str
    units_count: int
    total_effort_time: Optional[str]
    total_lecture_effort_time: Optional[str]
    worth: float
    desc: str
    locked: bool
    progress: int | float
    score: int | float
    unit_set: List[Unit]


class CourseChaptersModel(BaseModel):
    total_worth: float
    chapters: List[Chapter]


class CourseInfo(BaseModel):
    link: str
    course: CourseModel
    chapters: CourseChaptersModel
