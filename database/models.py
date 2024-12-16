from datetime import datetime
from sqlalchemy import Column, BigInteger, Text, String, TIMESTAMP
from database.db.base import Base


class User(Base):
    extend_existing = True

    __tablename__ = "users"

    telegram_id = Column(BigInteger, primary_key=True,  nullable=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255))
    start_at = Column(TIMESTAMP, default=datetime.now())



class SendMessageText(Base):
    extend_existing = True

    __tablename__ = "send_message_text"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    description = Column(String(255))
    text = Column(Text)

    def __init__(self, id, description, text):
        self.id = id
        self.description = description
        self.text = text