import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

api_id = os.getenv('ID')
api_hash = os.getenv('hash')
bot_token = os.getenv('token')
target_chats = os.getenv('chats')

message_Welcome = "Welcome to this chat"