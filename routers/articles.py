from fastapi import APIRouter, Query, Path, Body
from typing import Optional
from models.user import User
from models.article import Article

router = APIRouter()


@router.get('/articles/')
async def read_articles(
        q: Optional[str] = Query(
            None,
            # alias='item-query',
            title='Query string',
            description="Query string for the items to search in the database that have a good match",
            in_length=3)
):
    articles = {"article": [{"article_id": "foo"}, {"article_id": "bar"}]}
    if q:
        articles.update({"q": q})
    return articles


@router.get('/articles/{article_id}/')
# 必須パラメータでない場合、Noneを指定する
# 公式英訳のため以下メモ
# gt = greater than
# ge = greater than or equal
# lt = less than
# le = less than or equal
async def read_article(
        *,
        q: str,
        article_id: int = Path(..., title="The ID of the item to get", ge=2, le=4),
        # q: Optional[str] = Query(None, min_length=3, max_length=15, regex="^querystring$"),
        short: bool = False):
    article = {"article_id": article_id}
    # article = {"article": [{"article_id": "foo"}, {"article_id": "bar"}]}
    if q:
        article.update({"q": q})
    if not short:
        article.update(
            {"description": "test"}
        )
    return article


@router.post('/articles/')
async def create_article(article: Article):
    article_dict = article.dict()
    if article.author:
        author_with_id = article.author + article.id
        article_dict.update({"author_with_id": author_with_id})
    return article_dict


@router.put('/articles/{article_id}')
async def update_article(
        *,
        article: Article,
        user: User,
        article_id: int = Path(None, title="The ID of the item to get", ge=10, le=1000),
        importance: int = Body(...),
        q: Optional[str] = None):
    result = {"article_id": article_id, "article": article, "user": user, 'importance': importance}
    if q:
        result.update({"q": q})
    return result
