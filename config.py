class config:
    def __init__(self):
        with open('configs.conf', 'r') as f:
            ls = f.readlines()

            ls = list(map(lambda x: x.replace('\n', '').split(';'), ls))
            ls = dict(ls)
            try:
                self.TOKEN = ls['telegram-api-token']
            except:
                print('Err: problem with telegram api token check configs.conf file')
            try:
                self.NGROK_URL = ls['ngrok-link']
            except:
                print('Err: problem with telegram api token check configs.conf file')

        self.BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(self.TOKEN)
        self.LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(self.NGROK_URL)
        self.TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(self.BASE_TELEGRAM_URL,
                                                                       self.LOCAL_WEBHOOK_ENDPOINT)
        self.TELEGRAM_SEND_MESSAGE_URL = self.BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'



    def get_TELEGRAM_INIT_WEBHOOK_URL(self):
        self.__init__()
        print(self.TELEGRAM_INIT_WEBHOOK_URL)
        return self.TELEGRAM_INIT_WEBHOOK_URL

    def get_LOCAL_WEBHOOK_ENDPOINT(self):
        self.__init__()
        return self.LOCAL_WEBHOOK_ENDPOINT

    def get_TELEGRAM_SEND_MESSAGE_URL(self):
        self.__init__()
        return self.TELEGRAM_SEND_MESSAGE_URL


if __name__ == '__main__':
    con = config()
    print(con.BASE_TELEGRAM_URL)
