from enum import Enum


class UserRole(str, Enum):
    FARMER = "farmer"
    WORKER = "worker"
    CONTRACTOR = "contractor"


class TaskType(str, Enum):
    SOWING = "SOWING"
    TRANSPLANTING = "TRANSPLANTING"
    WEEDING = "WEEDING"
    SPRAYING = "SPRAYING"
    HARVESTING = "HARVESTING"
    THRESHING = "THRESHING"
    LOADING = "LOADING"
    PRUNING = "PRUNING"
    IRRIGATION = "IRRIGATION"
    OTHER = "OTHER"


class SkillType(str, Enum):
    SOWING = "SOWING"
    TRANSPLANTING = "TRANSPLANTING"
    WEEDING = "WEEDING"
    MANUAL_SPRAYING = "MANUAL_SPRAYING"
    MACHINE_SPRAYING = "MACHINE_SPRAYING"
    COTTON_PICKING = "COTTON_PICKING"
    GRAPE_HARVESTING = "GRAPE_HARVESTING"
    PADDY_HARVESTING = "PADDY_HARVESTING"
    SUGARCANE_CUTTING = "SUGARCANE_CUTTING"
    TRACTOR_DRIVING = "TRACTOR_DRIVING"
    DRONE_OPERATION = "DRONE_OPERATION"
    PRUNING = "PRUNING"
    IRRIGATION = "IRRIGATION"
    LOADING_UNLOADING = "LOADING_UNLOADING"
    OTHER = "OTHER"


class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CHECKED_IN = "CHECKED_IN"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    HELD_IN_ESCROW = "HELD_IN_ESCROW"
    RELEASED = "RELEASED"
    REFUNDED = "REFUNDED"
    FAILED = "FAILED"


class PaymentMode(str, Enum):
    UPI = "UPI"
    CASH = "CASH"
    WALLET = "WALLET"


class JobStatus(str, Enum):
    DRAFT = "DRAFT"
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ServiceType(str, Enum):
    DRONE_SPRAY = "DRONE_SPRAY"
    TRACTOR = "TRACTOR"
    HARVESTER = "HARVESTER"
    OTHER = "OTHER"


class NotificationType(str, Enum):
    JOB_ALERT = "JOB_ALERT"
    BOOKING_UPDATE = "BOOKING_UPDATE"
    PAYMENT = "PAYMENT"
    REMINDER = "REMINDER"
    OUTBREAK_WARNING = "OUTBREAK_WARNING"


class NotificationChannel(str, Enum):
    PUSH = "PUSH"
    SMS = "SMS"
    WHATSAPP = "WHATSAPP"


class UrgencyLevel(str, Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"


class BadgeLevel(str, Enum):
    NONE = "NONE"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"


INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Delhi", "Jammu & Kashmir", "Ladakh",
]

SUPPORTED_LANGUAGES = {
    "hi": "हिंदी (Hindi)",
    "mr": "मराठी (Marathi)",
    "gu": "ગુજરાતી (Gujarati)",
    "pa": "ਪੰਜਾਬੀ (Punjabi)",
    "ta": "தமிழ் (Tamil)",
    "te": "తెలుగు (Telugu)",
    "kn": "ಕನ್ನಡ (Kannada)",
    "bn": "বাংলা (Bengali)",
    "en": "English",
}

DEFAULT_SEARCH_RADIUS_KM = 15
MAX_SEARCH_RADIUS_KM = 50
GEOFENCE_RADIUS_METERS = 100
