import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
users_new = []

api_id = os.getenv('ID')
api_hash = os.getenv('hash')
bot_token = os.getenv('token')
url_database = os.getenv('database')
target_chats = [-834545163,271924178]
message_Welcome = "Bienvenido para ingresar al canal escriba su numero unico"