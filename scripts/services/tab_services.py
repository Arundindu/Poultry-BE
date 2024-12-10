import base64
import json

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from scripts.constants import app_constants
from scripts.core.handlers.tab_access import TabManagement
from scripts.logging.log_module import logger as log

TabService = APIRouter(prefix=app_constants.baseServiceUrl)

tab_service = TabManagement()


@TabService.post(app_constants.UserManagement.add_tab, tags=["Login Service"])
async def add_user_settings_tab_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.add_tab(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@TabService.post(app_constants.UserManagement.fetch_tab_data, tags=["Login Service"])
async def fetch_user_settings_tab_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.fetch_settings_tab_data(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "GLens", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}
