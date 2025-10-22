from fastapi import APIRouter

router = APIRouter(prefix="/products",
                tags=["products"],
                responses={404 : {"message" : "No encontrado"}})

@router.get("/info")
async def products():
    return "productos info"