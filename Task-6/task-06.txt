from typing import Final
import telebot
import requests

token: Final ='6333824276:AAEcDTYjzk2TMSGFKXqCnR48wECFWklsrgs'  # telegram-tb token

omdb_key='5da395eb1edb6485b675e67dfbb34b9d'                     # omdb token



tb=telebot.TeleBot(token)      
@tb.message_handler(commands=['movie'])
def getMovie(message):

    tb.reply_to(message, 'Getting movie info...')
    movie_name = message.text.split(' ',1)[1]  
    api_url = "https://www.omdbapi.com/?apikey=af752dc1&t="+movie_name
    response = requests.get(api_url)
    
    if response.status_code == 200:
        tb.reply_to(message, response.text)
    else:
        tb.reply_to(message, 'Sorry, couldnt get movie information.')




tb.infinity_polling()

