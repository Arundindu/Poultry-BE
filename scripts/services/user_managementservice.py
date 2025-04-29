import base64
import json

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from scripts.constants import app_constants
from scripts.core.handlers.user_managementhandler import UserManagement
from scripts.logging.log_module import logger as log

userService = APIRouter(prefix=app_constants.baseServiceUrl)

user_service = UserManagement()


@userService.post(app_constants.UserManagement.add_user, tags=["Login Service"])
async def add_user_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.add_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.login_check_request, tags=["Login Service"])
async def login_user(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.login_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.activate_user, tags=["Login Service"])
async def activate_user(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.activate_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.deactivate_user, tags=["Login Service"])
async def deActivate_user(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.de_activate_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}

@userService.post(app_constants.UserManagement.delete_user, tags=["Login Service"])
async def delete_user(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.delete_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.diseases_list, tags=["Login Service"])
async def diseases_list(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.disease_list(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while fetching diseases due to " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}

@userService.post(app_constants.UserManagement.market_trend, tags=["Login Service"])
async def market_trend(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.market_trends(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while fetching diseases due to " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.customer_wise_sales, tags=["Login Service"])
async def customer_wise_sales(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.customer_wise_sales_trends(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while fetching diseases due to " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.chick_trend, tags=["Login Service"])
async def chick_trend(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.chick_trends(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while fetching diseases due to " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}


@userService.post(app_constants.UserManagement.unblock_user, tags=["Login Service"])
async def unblock_user(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = user_service.unblock_user(json_object)

        resp = PlainTextResponse(content=base64.b64encode(json.dumps(response).encode()),
                                 headers={'Content-Type': 'text/plain; charset=utf-8',
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while fetching diseases due to " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}