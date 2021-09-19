from datetime import datetime
from uuid import uuid4
from models.reports import Report
from models.location import Location
from typing import List

# in practice we would use a database to store the reports, however for simplicity we will just store it in memory in a list
__reports: List[Report] = []


async def get_reports() -> List[Report]:

    # in practice this would be an async call here as it is reading from a database.
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.now()
    report = Report(id=str(uuid4()), location=location, description=description, created_date=now)

    # simulating saving to the database.
    # this would be an async call too as it is writing to a database.
    __reports.append(report)
    __reports.sort(key=lambda r: r.created_date, reverse=True)
    return report
