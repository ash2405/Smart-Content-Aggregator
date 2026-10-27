from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from app.core.config import settings

router = APIRouter(
    prefix="/health-check",
    tags=["Health Check"]
)

@router.get('/',
           summary="Health Check",
           description="Health Check",
           response_description="Health Check")
def health_check():

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "message": f"{settings.app_name} is up and running",
            "version": f"v{settings.app_version}"
        }
    )

# router.get('/db',
#            summary="Database Health Check",
#            description="Database Health Check",
#            response_description="Database Health Check")
# def get_db_health_check():

#     async with AsyncSessionLocal() as session:
#         try:
#             await session.execute(text("SELECT 1"))
#             return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={
#                     "success": True,
#                     "message": "Database is up and running"
#                 }
#             )
#         except Exception as e:
#             return JSONResponse(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 content={
#                     "success": False,
#                     "message": f"Database is down: {str(e)}"
#                 }
#             )