"""
This is the main script where Fast API application is initialized and routes are registered.
"""
import gc
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from scripts.constants import app_constants
from scripts.services.user_managementservice import userService
from scripts.services.tab_services import TabService
gc.collect()

tags_meta = [{"name": "loginCheckRequest","description": "User login service"}]
app = FastAPI(
    title="Personal Project",
    version="v1.0",
    description="UserManagement",
    openapi_tags=tags_meta,
    # root_path=app_constants.baseServiceUrl
)

# Register Routes
app.include_router(userService)
app.include_router(TabService)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)
