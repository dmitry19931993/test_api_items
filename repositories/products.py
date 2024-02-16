from .base import BaseRepository
from models.products import Product, ProductIn
from typing import List, Optional
from db.products import products


class ProductRepository(BaseRepository):

    async def create(self, p: ProductIn) -> Product:
        product = Product(
            name=p.name,
            description=p.description,
            price=p.price,
            status=p.status
        )

        values = {**product.dict()}
        values.pop("id", None)
        query = products.insert().values(**values)
        product.id = await self.database.execute(query=query)
        return product

    async def update(self, id: int, p: ProductIn) -> Product:
        product = Product(
            name=p.name,
            description=p.description,
            price=p.price,
            status=p.status
        )

        values = {**product.dict()}
        values.pop("id", None)
        query = products.update().where(products.c.id == id).values(**values)
        product.id = await self.database.execute(query=query)
        return product


    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Product]:
        query = products.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int) -> List:
        query = products.delete().where(products.c.id == id)
        return await self.database.fetch_all(query=query)

    async def delete_all(self) -> None:
        query = products.delete()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Product]:
        query = products.select().where(products.c.id == id)
        product = await self.database.fetch_one(query=query)
        if product is None:
            return None
        return product
