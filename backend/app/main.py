from fastapi import FastAPI
from app.api import auth
from fastapi.openapi.docs import get_swagger_ui_html


app = FastAPI()
# ✅ Sample root endpoint
# @app.get("/", summary="Welcome Route", response_description="API Welcome Message")
# async def custom_swagger_ui():
#     return get_swagger_ui_html(
#         openapi_url="/",
#         title="SmartProcure API Docs"
#     )
app.include_router(auth.router)
