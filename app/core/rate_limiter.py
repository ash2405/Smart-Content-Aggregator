from slowapi import Limiter
from slowapi.util import get_remote_address
from app.core.config import settings

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100/minute"],
    storage_uri=settings.redis_url
)




# Limiter: Rate limiting functionality provide karta hai.
# get_remote_address: Request bhejne wale client ka IP address identify karta hai.
# limiter: Rate limiter ka object create karta hai.

# key_func → Client IP identify karega.
# default_limits → Default 100 requests/minute.
# storage_uri → Redis connection URL; counters Redis mein store honge.