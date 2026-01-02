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
                                          'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                          'Access-Control-Allow-Origin': '*'})
        return resp

    except Exception as e:
        log.error("Exception occurred while adding the user " + str(e))
        resp = {'status': 'failed'}
        return base64.b64encode(json.dumps(resp).encode()), {'Content-Type': 'text/plain; charset=utf-8',
                                                             'Server': "DCSR", 'X-Content-Type-Options': "nosniff",
                                                             'Access-Control-Allow-Origin': '*'}

@TabService.post(app_constants.UserManagement.fetch_tab_header_data, tags=["Login Service"])
async def fetch_user_settings_tab_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.fetch_settings_tab_header_data(json_object)

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

@TabService.post(app_constants.UserManagement.save_bird_price, tags=["Login Service"])
async def save_bird_price(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.save_bird_price_data(json_object)

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


@TabService.post(app_constants.UserManagement.save_hens_availability, tags=["Login Service"])
async def save_hens_availability(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.save_hens_availability_data(json_object)

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


@TabService.post(app_constants.UserManagement.sheds_availability, tags=["Login Service"])
async def sheds_availability(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.sheds_availability_data(json_object)

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


@TabService.post(app_constants.UserManagement.sheds_table_data, tags=["Login Service"])
async def sheds_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.sheds_table_data(json_object)

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

@TabService.post(app_constants.UserManagement.feed_consumption_data, tags=["Login Service"])
async def feed_consumption_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.feed_consumption_data(json_object)

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

@TabService.post(app_constants.UserManagement.feed_consumption_table_data, tags=["Login Service"])
async def feed_consumption_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.feed_consumption_table_data(json_object)

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

@TabService.post(app_constants.UserManagement.user_setup_data, tags=["Login Service"])
async def feed_consumption_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.user_setup_data(json_object)

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

@TabService.post(app_constants.UserManagement.user_setup_table_data, tags=["Login Service"])
async def user_setup_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.user_setup_table_data(json_object)

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

@TabService.post(app_constants.UserManagement.order_hens_data, tags=["Login Service"])
async def order_hens_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.order_hens_data(json_object)

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

@TabService.post(app_constants.UserManagement.sales_data, tags=["Login Service"])
async def sales_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.sales_data(json_object)

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


@TabService.post(app_constants.UserManagement.sales_table_data, tags=["Login Service"])
async def sales_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.sales_table_data(json_object)

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


@TabService.post(app_constants.UserManagement.order_hens_data, tags=["Login Service"])
async def order_hens_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.order_hens_data(json_object)

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

@TabService.post(app_constants.UserManagement.order_hens_table_data, tags=["Login Service"])
async def order_hens_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.order_hens_table_data(json_object)

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



@TabService.post(app_constants.UserManagement.birds_price_table_data, tags=["Login Service"])
async def birds_price_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.birds_price_table(json_object)

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


@TabService.post(app_constants.UserManagement.public_data, tags=["Login Service"])
async def public_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.public_data(json_object)

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


@TabService.post(app_constants.UserManagement.chick_price_data, tags=["Login Service"])
async def chick_price_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.chick_price(json_object)

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

@TabService.post(app_constants.UserManagement.chick_price_table_data, tags=["Login Service"])
async def chick_price_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.chick_price_table(json_object)

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


@TabService.post(app_constants.UserManagement.mortality_data, tags=["Login Service"])
async def mortality_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.mortality(json_object)

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

@TabService.post(app_constants.UserManagement.mortality_table_data, tags=["Login Service"])
async def mortality_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.mortality_table(json_object)

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



@TabService.post(app_constants.UserManagement.diseases_data, tags=["Login Service"])
async def diseases_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.diseases(json_object)

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

@TabService.post(app_constants.UserManagement.diseases_table_data, tags=["Login Service"])
async def diseases_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.diseases_table(json_object)

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


@TabService.post(app_constants.UserManagement.delete_settings_tab_details, tags=["Login Service"])
async def delete_settings_tab_details(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.delete_settings_details(json_object)

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

@TabService.post(app_constants.UserManagement.blockedUsers_table_data, tags=["Login Service"])
async def blockedUsers_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.blockedUsersTable(json_object)

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

@TabService.post(app_constants.UserManagement.dashboard_table_data, tags=["Login Service"])
async def dashboard_table_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.dashboardTableData(json_object)

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

@TabService.post(app_constants.UserManagement.get_side_bar_data, tags=["Login Service"])
async def get_side_bar_data(request: Request):
    try:
        input_data = await request.body()
        json_string = base64.b64decode(input_data)
        json_object = json.loads(json_string)
        response = tab_service.side_bar_data(json_object)

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
