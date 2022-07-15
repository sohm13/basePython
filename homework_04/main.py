"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import os
import aiohttp, asyncio
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select
from sqlalchemy.engine.result import Result

from jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL
from models import User, Post, Session, Base, engine
import json


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
  response = {'status': '', 'error': '', 'data': ''}
  async with session.get(url) as resp:
    response['status'] = resp.status
    response['data'] =  await resp.json()
  return response

async def fetch_users_data(session: aiohttp.ClientSession) -> list[dict]:
    url = USERS_DATA_URL
    users = await fetch_json(session, url)
    return users['data']
  
async def fetch_posts_data(session: aiohttp.ClientSession) -> list[dict]:
  url = POSTS_DATA_URL
  posts = await fetch_json(session, url)
  return posts['data']

async def create_table():
  async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
  print('created new table')

async def add_users(session: AsyncSession, users: list[dict]):
  for user in users:
    _user = User(name=user.get('name'), username=user.get('username'), email=user.get('email'))
    session.add(_user)
  await session.commit()
  print('added users')

async def add_posts(session: AsyncSession, posts: list[dict]):
  for post in posts:
    stmt = select(User).where(User.id == post.get('userId'))
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
      continue
    _post = Post(user=user, title=post.get('title'), body=post.get('body'))
    session.add(_post)
  await session.commit()
  print('added posts')


async def async_main():
  users_data: list[dict] = []
  posts_data: list[dict] = []
  async with aiohttp.ClientSession() as session:
    users_data, posts_data = await asyncio.gather(
              fetch_users_data(session),
              fetch_posts_data(session)
    )

  await create_table()
  async with Session() as session:
    await add_users(session, users_data)
    await add_posts(session, posts_data)


def main():
    if 'nt' in os.name:
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())




if __name__ == "__main__":
    main()
