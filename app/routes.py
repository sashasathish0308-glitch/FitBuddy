import sqlite3

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .ai.gemini import generate_ai_response


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# =========================================================
# REQUEST MODELS
# =========================================================

class ProfileRequest(BaseModel):
    name: str
    age: int
    gender: str


class WorkoutRequest(BaseModel):
    age: int
    level: str
    goal: str


class DietRequest(BaseModel):
    age: int
    preference: str
    goal: str


# =========================================================
# HOME
# =========================================================

@router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# =========================================================
# BMI
# =========================================================

@router.get("/bmi")
def bmi(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="bmi.html",
        context={}
    )


# =========================================================
# WORKOUT
# =========================================================

@router.get("/workout")
def workout(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="workout.html",
        context={}
    )


# =========================================================
# DIET
# =========================================================

@router.get("/diet")
def diet(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="diet.html",
        context={}
    )


# =========================================================
# SAVE PROFILE
# =========================================================

@router.post("/save-profile")
def save_profile(data: ProfileRequest):

    if not data.name.strip():

        return {
            "success": False,
            "error": "Name is required."
        }

    if data.age < 18:

        return {
            "success": False,
            "error": (
                "This FitBuddy demo is intended "
                "for adults aged 18 and above."
            )
        }

    try:

        conn = sqlite3.connect("fitbuddy.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (name, age, gender)
            VALUES (?, ?, ?)
            """,
            (
                data.name.strip(),
                data.age,
                data.gender
            )
        )

        conn.commit()

        user_id = cursor.lastrowid

        conn.close()

        return {
            "success": True,
            "message": "Profile saved successfully!",
            "user_id": user_id
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# =========================================================
# GENERATE WORKOUT
# =========================================================

@router.post("/generate-workout")
def generate_workout(data: WorkoutRequest):

    if data.age < 18:

        return {
            "success": False,
            "error": (
                "This FitBuddy AI demo is intended "
                "for adults aged 18 and above."
            )
        }

    prompt = f"""
You are generating a general wellness exercise example
for an adult user.

Age: {data.age}
Fitness level: {data.level}
Goal: {data.goal}

Create a simple 7-day general wellness activity schedule.

Keep it moderate and safe.

Include rest and recovery days.

Do not provide medical advice.

Do not recommend extreme exercise
or unsafe activities.

Format the response clearly by day.
"""

    try:

        result = generate_ai_response(prompt)

        return {
            "success": True,
            "workout": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# =========================================================
# GENERATE DIET
# =========================================================

@router.post("/generate-diet")
def generate_diet(data: DietRequest):

    if data.age < 18:

        return {
            "success": False,
            "error": (
                "This FitBuddy AI demo is intended "
                "for adults aged 18 and above."
            )
        }

    prompt = f"""
You are generating a general healthy eating example
for an adult user.

Age: {data.age}
Diet preference: {data.preference}
Goal: {data.goal}

Create a simple 7-day general healthy eating example.

For each day include:

Breakfast
Lunch
Dinner
Healthy snack

Keep the suggestions balanced and general.

Do not provide medical advice.

Do not recommend extreme diets.

Do not recommend restrictive eating.

Format the response clearly by day.
"""

    try:

        result = generate_ai_response(prompt)

        return {
            "success": True,
            "diet": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }