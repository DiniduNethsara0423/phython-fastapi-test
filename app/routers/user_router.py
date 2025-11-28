from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse

"""Deprecated module

This module was moved to `app.routes.user_route`. Keep this placeholder
to avoid accidental imports during transitions.
"""

# NOTE: router moved to `app.routes.user_route`
