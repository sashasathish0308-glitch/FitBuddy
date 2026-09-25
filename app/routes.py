from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.get("/bmi")
def bmi(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="bmi.html",
        context={}
    )


@router.get("/workout")
def workout(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="workout.html",
        context={}
    )


@router.get("/diet")
def diet(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="diet.html",
        context={}
    )