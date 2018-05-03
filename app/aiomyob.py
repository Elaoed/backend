# -*- coding: utf-8 -*-
import aiomysql
import asyncio
from app.config import Config

class AioMyOB:

    def __init__(self, loop):
        self.loop = loop
        self.pool = None

    async def insert(self, sql, params):
        if not self.pool:
            self.pool = await aiomysql.create_pool(loop=self.loop, **Config.MySqlConfig)
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(sql, params)
                    conn.commit()
                except Exception as err:
                    conn.rollback()
                    raise err

    async def update(self, sql, params):
        await self.insert(sql, params)

    async def select(self, sql, params, one=True):
        if not self.pool:
            self.pool = await aiomysql.create_pool(loop=self.loop, **Config.MySqlConfig)
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(sql, params)
                    return await cur.fetchone() if one else cur.fetchall()
                except Exception as err:
                    conn.rollback()
                    raise err

    async def delete(self, sql, params):
        await self.insert(sql, params)

if __name__ == "__main__":
    async def main():
        aob = AioMyOB(loop)
        print(await aob.select("SELECT * FROM hello", []))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
