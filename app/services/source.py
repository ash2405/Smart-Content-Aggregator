from app.exceptions.exceptions_log import ConflictException, NotFoundException
from app.models.source import Source
from app.schemas.source import SourceCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.source import get_source_by_name, create_source_item, get_sources_list, update_source_item
from app.repositories.source import get_source_by_id

async def source_create(source: SourceCreate, db: AsyncSession):

    sourceItem = await get_source_by_name(source, db)

    if sourceItem is not None:
        raise ConflictException("Source with this name already exists.")

    try:
        createdItem = Source(
            name=source.name,
            url=str(source.url),
        )

        result = await create_source_item(createdItem, db)

        await db.commit()
        await db.refresh(result)
        return result

    except Exception:
        await db.rollback()
        raise 

async def get_sources_service(db: AsyncSession, limit:int, skip:int):
    return await get_sources_list(db, limit, skip)

async def get_source_by_id_service(source_id: int, db: AsyncSession):
    result  = await get_source_by_id(source_id,db)
    if result is None:
        raise NotFoundException(f"Source with id {source_id} not found.")
    return result

async def update_source_service(source_id:int, source:SourceCreate, db:AsyncSession):
    existing_source = await get_source_by_id(source_id, db)

    if existing_source is None:
        raise NotFoundException(f"Source with id {source_id} not found.")

    sourceItem = await get_source_by_name(source, db)

    if sourceItem is not None and sourceItem.id != source_id:
        raise ConflictException("Source with this name already exists.")

    try:
        updated_source = await update_source_item(data=source, source=existing_source, db=db)
        await db.commit()
        await db.refresh(updated_source)
        return updated_source
    except Exception:
        await db.rollback()
        raise

async def source_delete_service(source_id:int, db:AsyncSession):
    existing_source = await get_source_by_id(source_id, db)
    if existing_source is None:
        raise NotFoundException(f"Source with id {source_id} not found.")

    try:
        await db.delete(existing_source)
        await db.commit()
        return {"message": f"Source with id {source_id} has been deleted."}
    except Exception:
        await db.rollback()
        raise