from app.config import Settings, get_settings
from app.schemas import ExamplePayload
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/hello")


@router.get("/")
def hello():
    """Hello world router"""
    return {"Hello": "World"}


@router.post("/add")
def add(body: ExamplePayload):
    """How to use the example paylod in an endpoint"""
    return {"new_number": body.first_number + body.second_number}


@router.get("/env")
def get_env(settings: Settings = Depends(get_settings)):
    """Get the environment"""
    return {"env": settings.environment}
