from models.products import Product, ProductIn
from models.users import User
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.products import ProductRepository
from .depends import get_product_repository, get_current_user


router = APIRouter()

@router.get("/")
async def read_products(
    limit: int = 100,
    skip: int = 0,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    return await products.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Product)
async def create_product(
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    return await products.create(p=p)

@router.put("/", response_model=Product)
async def update_product(
    id: int,
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    product = await products.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if product is None:
        raise not_found_exception

    return await products.update(id=id, p=p)

@router.get("/product_id")
async def read_product(
    id: int,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    product = await products.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if product is None:
        raise not_found_exception

    return await products.get_by_id(id=id)

@router.delete("/")
async def delete_product(
    id: int,
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    product = await products.get_by_id(id=id)
    not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if product is None:
        raise not_found_exception
    await products.delete(id=id)
    return {"status": True}

@router.delete("/all")
async def delete_product_all(
    products: ProductRepository = Depends(get_product_repository),
    current_user: User = Depends(get_current_user)):
    await products.delete_all()
    return {"status": True}