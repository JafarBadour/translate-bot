# python-telegram-bot
Telegram bot compatible with Python 3.7. Webhooks with ngrok to Telegram bot message stream, conditional responses.

Currently under development - 4/13/2019

## Instructions For Use:
Download ngrok into the project root directory: https://ngrok.com/download

Navigate the the root directory in terminal, run:

> ./ngrok http 5000

Add your telegram bot token to the TOKEN variable in config.py

Add your ngrok https url to the NGROK_URL variable in config.py

Configure conditional actions based on Telegram message text in telegram_bot.py TelegramBot.action class method

Run the app server however you have python3.7 set to PATH:
> $ python3.7 app.py

# Docker version
You should run

```shell script
sudo docker pull jafarbadour/telegram-translator-bot:latest
./ngrok http 5000
```
Now you should get the tunnel url and then insert it after running this command
```shell script
sudo docker run --network host -ti jafarbadour/telegram-translator-bot:latest
```


You should manually put the ngrok url in configs.conf
