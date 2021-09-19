from typing import List
import fastapi
from fastapi.params import Depends

from models.location import Location
from models.reports import Report, ReportSubmittal
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(
    loc: Location = Depends(),  # To use Pydantic model as query parameters, instead of json request, use Depends()
    units: str = 'metric',
):
    try:
        return await openweather_service.get_report(loc.city, loc.state, loc.country, units)

    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)

    except Exception as x:
        print(f"Server crashed while processing request: {x}")
        return fastapi.Response(content="Error processing gyour request.", status_code=500)


@router.get(
    '/api/reports',
    name='all_reports',  # for showing on SwaggerUI docs
    response_model=List[Report],  # again, shows whata resonse looks like on SwaggerUI
)
async def report_get() -> List[Report]:
    return await report_service.get_reports()


@router.post(
    '/api/reports',
    name='add_report',
    status_code=201,  # the status_code in the response if successfully posted
    response_model=Report,
)
async def report_post(report_submittal: ReportSubmittal) -> Report:
    d = report_submittal.description
    loc = report_submittal.location

    return await report_service.add_report(d, loc)
