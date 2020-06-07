from flask import Flask, request, jsonify

from telegram_bot import TelegramBot
from config import config

configs = config()
app = Flask(__name__)
print(TelegramBot.init_webhook(configs.get_TELEGRAM_INIT_WEBHOOK_URL()))


@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    print(req)
    bot.parse_webhook_data(req)
    try:
        success = bot.action()
    except:
        pass
    return jsonify(success=success)  # TODO: Success should reflect the success of the reply


@app.route('/sup')
def sup():
    return '<h1>Hi</h1>'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0>/getme
# check webhook url: https://api.telegram.org/bot822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0/getWebhookInfo
