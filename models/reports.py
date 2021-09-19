from datetime import datetime
from typing import Optional
from models.location import Location
from pydantic.main import BaseModel
import uuid


class ReportSubmittal(BaseModel):
    """This is what users sends"""

    description: str
    location: Location


class Report(BaseModel):
    """This is what users receives"""

    id: str
    description: str
    location: Location
    created_date: Optional[datetime]
