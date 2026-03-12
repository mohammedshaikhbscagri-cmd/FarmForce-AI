from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.user import User  # noqa: E402, F401
from app.models.job import Job  # noqa: E402, F401
from app.models.booking import Booking  # noqa: E402, F401
from app.models.payment import Payment  # noqa: E402, F401
from app.models.review import Review  # noqa: E402, F401
from app.models.skill import WorkerSkill  # noqa: E402, F401
from app.models.farm import FarmerFarm  # noqa: E402, F401
from app.models.service import Service  # noqa: E402, F401
from app.models.notification import Notification  # noqa: E402, F401
