from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import services
from app.core.security import get_password_hash
from app.models import User
# from app.schemas.requests import UserCreateRequest, UserUpdatePasswordRequest
from app.schemas.responses import UserResponse

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def read_current_user(
    current_user: User = Depends(services.get_current_user),
):
    """Get current user"""
    return current_user
