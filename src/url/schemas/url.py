from typing import Optional, Self

from pydantic import BaseModel, model_validator

import hashlib

from src.coder.sha256_coder import Sha256Coder

POSTFIX_LENGTH = 8

class UrlPairEncoded(BaseModel):
    long_url: str
    short_url: Optional[str]

    @model_validator(mode='after')
    @classmethod
    def getting_short_url(cls, obj: Self) -> Self:
        if obj.short_url is None:
            obj.short_url = Sha256Coder.get_short_url(url=obj.long_url, length=POSTFIX_LENGTH)
        elif len(obj.short_url) > 10:
            raise ValueError('Shorturl is too long')
        return obj