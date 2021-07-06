from pyrogram.types import Chat


def get_chat_id(chat: Chat):
    if chat.title and chat.title.startswith('CHStock Music: ') and chat.title[16:].isnumeric():
        return int(chat.title[13:])
    return chat.id
