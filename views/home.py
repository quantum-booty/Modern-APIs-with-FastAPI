import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from services import report_service

router = fastapi.APIRouter()


templates = Jinja2Templates('templates')


@router.get('/', include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}
    return templates.TemplateResponse('home/index.html', data)


@router.get(
    '/favicon.ico',
    include_in_schema=False,  # this option hides this get method from SwaggerUI (because it is not important)
)
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
