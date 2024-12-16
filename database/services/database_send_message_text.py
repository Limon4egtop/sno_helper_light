from typing import Optional

from sqlalchemy import select, func

from database.db.base import get_session
from database.models import SendMessageText


async def get_message_by_id(id: int) -> Optional[SendMessageText]:
    """Получить сообщение по id"""
    async for session in get_session():
        query = select(SendMessageText).where(SendMessageText.id == id)
        result = await session.execute(query)
        msg_text = result.scalars().first()
        return msg_text