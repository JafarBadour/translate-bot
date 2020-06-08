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

    try:
        bot.parse_webhook_data(req)
        success = bot.action()
    except:
        success = None
    return jsonify(success=success)  # TODO: Success should reflect the success of the reply


@app.route('/sup')
def sup():
    return '<h1>Hi</h1>'


if __name__ == '__main__':
    # ngrokserver = input('Run ./ngrok http 5000\n and tell me what is it:\n')
    # f = open('configs.conf', 'r')
    # x = f.readlines()
    # x[1] = ';'.join([x[1].split(';')[0], ngrokserver])
    # open('configs.conf', 'w').write(''.join(x))
    app.run(port=5000, debug=True)

# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0>/getme
# check webhook url: https://api.telegram.org/bot822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0/getWebhookInfo
