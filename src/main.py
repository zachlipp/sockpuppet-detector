from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

from model import get_hashtag_accounts, get_similar_screen_names


class Post(BaseModel):
    id: UUID
    created_at: datetime
    author_id: UUID
    is_repost: bool
    text: str
    hashtags: List[str]


class Account(BaseModel):
    id: UUID
    created_at: datetime
    screen_name: str


class ModelInput(BaseModel):
    posts: List[Post]
    accounts: List[Account]
    hashtag: str
    min_similarity: float


app = FastAPI()


@app.get("/")
async def get_hashtag_sockpuppets(data: ModelInput):
    posts = [p.dict() for p in data.posts]
    accounts = [a.dict() for a in data.accounts]
    hashtag_users = get_hashtag_accounts(posts, data.hashtag)
    similar_names = get_similar_screen_names(accounts, data.min_similarity)
    return {"similar_names": similar_names}
