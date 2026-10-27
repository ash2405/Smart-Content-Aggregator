from fastapi import APIRouter, Query, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED

from app.core.dependency import get_db
from app.schemas.source import SourceCreate, SourceResponse
from app.services.source import source_create, source_delete_service, update_source_service
from app.services.source import get_sources_service, get_source_by_id_service

router = APIRouter(
    prefix="/sources",
    tags=["sources"]
)


@router.get('/', response_model=list[SourceResponse])
async def get_sources(limit:int = Query(default=10,ge=10,le=100),
                      skip:int = Query(default=0,ge=0),
                      db: AsyncSession = Depends(get_db)
                      ):
    result = await get_sources_service(db, limit, skip)
    return result

@router.get('/{source_id}', response_model=SourceResponse)
async def get_source_by_id(source_id:int,
                           db: AsyncSession = Depends(get_db)):
    return await get_source_by_id_service(source_id, db)


@router.post("/", 
             response_model=SourceResponse,
             status_code=status.HTTP_201_CREATED)
async def create_source(source:SourceCreate,
                        db: AsyncSession = Depends(get_db)):
    return await source_create(source, db)

@router.put('/{source_id}',response_model=SourceResponse)
async def update_source(source_id:int,
                        source:SourceCreate,
                        db: AsyncSession = Depends(get_db)):
    return await update_source_service(source_id, source, db)

@router.delete('/{source_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_source(source_id:int,
                        db: AsyncSession = Depends(get_db)):
    return await source_delete_service(source_id, db)