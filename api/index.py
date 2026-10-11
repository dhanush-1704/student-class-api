from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Class API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "students.json"


def load_students() -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/api")
def get_students(class_: Optional[list[str]] = Query(default=None, alias="class")):
    students = load_students()
    if class_:
        wanted = set(class_)
        students = [student for student in students if student["class"] in wanted]
    return {"students": students}
