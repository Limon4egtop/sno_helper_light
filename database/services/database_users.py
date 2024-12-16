from typing import Optional
from datetime import datetime

from sqlalchemy import select, func

from database.db.base import get_session
from database.models import User


async def get_user_by_tg_id(tg_id: int) -> Optional[User]:
    """Получить пользователя по Telegram ID"""
    async for session in get_session():
        query = select(User).where(User.telegram_id == tg_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return user


async def check_existing_user(tg_id: int) -> bool:
    """Проверить существование пользователя по Telegram ID"""
    async for session in get_session():
        result = await session.execute(select(func.count()).where(User.telegram_id == tg_id))
        count = result.scalar()
        return count > 0


async def add_user(tg_user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None,
                   username: Optional[str] = None, start_at: Optional[datetime] = datetime.now()) -> User:
    """Добавить нового пользователя без информации о нем. Только Telegram ID"""
    async for session in get_session():
        new_user = User(telegram_id=tg_user_id, first_name=first_name, last_name=last_name,
                        username=username, start_at=start_at)
        session.add(new_user)
        await session.commit()


async def update_user_profile(tg_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None,
                              username: Optional[str] = None):
    """Обновить информацию профиля пользователя"""
    async for session in get_session():
        query = select(User).where(User.telegram_id == tg_id)
        result = await session.execute(query)
        user = result.scalars().first()

        if not user:
            return False

        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if username is not None:
            user.username = username

        session.add(user)
        await session.commit()
        return True

