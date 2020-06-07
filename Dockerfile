FROM python:3
ADD . /
RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
#
# docker run --network host -ti jafarbadour/telegram-translator-bot:1