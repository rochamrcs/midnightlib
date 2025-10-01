from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from midnightlib.database import get_session, sanitization
from midnightlib.models import User
from midnightlib.schemas import UserList, UserPublic, UserSchema
from midnightlib.security import get_password_hash

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/conta',
status_code=HTTPStatus.CREATED,
response_model=UserPublic)
async def create_user(
    user: UserSchema,
    session: Session = Depends(get_session)
    ):

    db_user = await session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Email already exists',
            )

    password_encrypt = get_password_hash(user.password)
    username_sanitization = sanitization(user.username)
    email_sanitization = sanitization(user.email)

    db_user = User(
        username=username_sanitization,
        password=password_encrypt,
        email=email_sanitization
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.put('/conta/{user.id}', response_model=UserPublic)
async def update_user(
    user_id: int,
    user: UserSchema,
    session: Session = Depends(get_session),
):
    db_user = await session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    try:

        password_encrypt = get_password_hash(user.password)
        username_sanitization = sanitization(user.username)
        email_sanitization = sanitization(user.email)

        db_user.username = username_sanitization
        db_user.password = password_encrypt
        db_user.email = email_sanitization

        await session.commit()
        await session.refresh(db_user)

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists',
        )


@router.get('/list_user/', response_model=UserList)
async def read_users(session: AsyncSession = Depends(get_session)):
    result = await session.scalars(select(User))
    users = result.all()
    return {"users": users}


@router.delete('/conta/{user_id}')
async def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    await session.delete(db_user)
    await session.commit()

    return {'message': 'User has been deleted with success'}
