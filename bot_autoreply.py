import os
import time
import requests

BOT_TOKEN = os.environ['BOT_TOKEN']  # <- из переменных окружения
URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

last_update_id = None

while True:
    try:
        response = requests.get(f'{URL}/getUpdates', params={'offset': last_update_id, 'timeout': 10})
        data = response.json()

        for result in data.get('result', []):
            update_id = result['update_id']
            chat_id = result['message']['chat']['id']
            text = result['message'].get('text', '')

            if last_update_id is None or update_id > last_update_id:
                print(f'📩 Новое сообщение от {chat_id}: {text}')
                requests.post(f'{URL}/sendMessage', data={
                    'chat_id': chat_id,
                    'text': WELCOME_MESSAGE
                })
                last_update_id = update_id + 1

        time.sleep(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
