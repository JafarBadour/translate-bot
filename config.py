
class config:
    def __init__(self):

        self.TOKEN = ''
        self.NGROK_URL = ''
        self.BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
        self.LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
        self.TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
        self.TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
