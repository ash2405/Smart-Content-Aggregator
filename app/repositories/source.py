

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.source import Source
from app.schemas.source import SourceCreate

async def get_source_by_name(source: SourceCreate, db: AsyncSession)-> Source | None:
    result = await db.execute(
        select(Source).where((Source.name == source.name) | (Source.url == str(source.url)))
    )
    return result.scalar_one_or_none()


async def create_source_item(source: SourceCreate, db: AsyncSession):
    db.add(source)
    return source

async def get_source_by_id(source_id: int, db: AsyncSession)-> Source | None:
    result = await db.execute(
        select(Source).where(Source.id == source_id)
    )
    return result.scalar_one_or_none()

async def get_sources_list(db: AsyncSession,limit: int,skip: int)-> list[Source] | None:
    result = await db.execute(
        select(Source)
        .order_by(Source.id)
        .limit(limit)
        .offset(skip)
    )
    return list(result.scalars().all())

async def update_source_item(data:SourceCreate,source: Source,db:AsyncSession)-> Source:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "url":
            setattr(source,field,str(value))
        else:
            setattr(source,field,value)

    await db.flush()
    return source
    