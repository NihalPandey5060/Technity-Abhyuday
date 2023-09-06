from typing import Final
import telebot
import requests
from key import get_key
from key import get_token




apiKey = get_key()
token = get_token()

# Used .gitignore
# telegram-tb token

tb=telebot.TeleBot(token)      
@tb.message_handler(commands=['movie'])
def getMovie(message):

    tb.reply_to(message, 'Getting movie info...')
    movie_name = message.text.split(' ',1)[1]  
    api_url = "https://www.omdbapi.com/?apikey="+apiKey+"&t=" + movie_name
    response = requests.get(api_url)
    
    if response.status_code == 200:
        tb.reply_to(message, response.text)
    else:
        tb.reply_to(message, 'Sorry, couldn\'t fetch movie information.')
tb.infinity_polling()

