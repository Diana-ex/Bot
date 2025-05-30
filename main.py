from flask import Flask, request
import vk_api
import os

app = Flask(__name__)

GROUP_TOKEN = os.getenv("GROUP_TOKEN")
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()

@app.route('/', methods=['POST'])
def main():
    data = request.json

    if data['type'] == 'confirmation':
        return '6c8bef24'  # Код подтверждения из ВК

    elif data['type'] == 'message_new':
        user_id = data['object']['peer_id']
        message_text = data['object']['text']

        # Отправляем ответ пользователю
        vk.messages.send(
            peer_id=user_id,
            message=f"Вы написали: {message_text}",
            random_id=0
        )

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
