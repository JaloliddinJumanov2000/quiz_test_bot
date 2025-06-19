from utils.db.database import User

async def get_user_db_lang(session, user_id: int) -> str:
    user = session.query(User).filter(User.chat_id == user_id).first()
    if user:
        return user.lang
    return 'uz'