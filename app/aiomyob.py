# -*- coding: utf-8 -*-
import aiomysql
import asyncio
from app.config import Config

class AioMyOB:

    pool = None

    @classmethod
    async def insert(cls, sql, params=None):
        params = params or []
        if not cls.pool:
            cls.pool = await aiomysql.create_pool(**Config.MySqlConfig)
        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(sql, params)
                    conn.commit()
                except Exception as err:
                    conn.rollback()
                    raise err

    @classmethod
    async def update(cls, sql, params=None):
        await cls.insert(sql, params)

    @classmethod
    async def select(cls, sql, params=None, one=True):
        params = params or []
        if not cls.pool:
            cls.pool = await aiomysql.create_pool(**Config.MySqlConfig)
        async with cls.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(sql, params)
                    return await cur.fetchone() if one else cur.fetchall()
                except Exception as err:
                    conn.rollback()
                    raise err

    @classmethod
    async def delete(cls, sql, params=None):
        await cls.insert(sql, params)

if __name__ == "__main__":
    async def main():
        print(await AioMyOB.select("SELECT * FROM hello", []))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
