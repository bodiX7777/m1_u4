import telebot
import time 
from telebot import types
from settings import TG_API_TOKEN
bot = telebot.TeleBot(TG_API_TOKEN)
users = {}
freeid = None
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.reply_to(message, f'Hi! I am a bot {bot.get_me().first_name}!')
    bot.send_message(message.chat.id, 'Just use /find command!')

@bot.message_handler(commands=['find'])
def find(message: types.Message):
    if message.chat.id not in users:
        bot.send_message(message.chat.id, 'Finding...')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Wait a bit...')
        time.sleep(2)
        bot.send_message(message.chat.id, 'My loading is successfully completed!')
        bot.send_message(message.chat.id, 'What do you want to do next?')
        time.sleep(2)
        bot.send_message(message.chat.id, '/stop - stop the search,/search - find new films,/watch1 - give you a website where you can watch films,/recommend - recommend films for you')
@bot.message_handler(commands=['stop', 'search', 'recommend'])
def actions(message: types.Message):
    if message.chat.id not in users:
        if message.text == '/stop':
            bot.send_message(message.chat.id, 'Search stopped!')
        elif message.text == '/search':
            bot.send_message(message.chat.id, 'Finding new films...')
            bot.send_message(message.chat.id, 'Which genres do you prefer?')
            bot.send_message(message.chat.id, '/action = Action = fights, chases, battles.')
            bot.send_message(message.chat.id, '/adventure = Adventure = journeys, exploration, quests.')
            bot.send_message(message.chat.id, '/comedy = Comedy = funny, made to make you laugh.')
            bot.send_message(message.chat.id, '/horror = Horror = scary, dark atmosphere.')
            bot.send_message(message.chat.id, '/fantasy = Fantasy = magic, mythical worlds, supernatural.')
            time.sleep(2)
@bot.message_handler(commands=['action', 'adventure', 'comedy', 'horror', 'fantasy', 'trailer', 'watch1', 'trailer1', 'trailer2', 'trailer3', 'trailer4'])
def actions(message: types.Message):
    if message.chat.id not in users:
            if message.text == '/action':
                bot.send_message(message.chat.id, 'You selected Action genre.')
                bot.send_message(message.chat.id, 'This are films I found for you: Kung Fu Panda (2008),How to Train Your Dragon (2010),Sonic the Hedgehog (2020)')
                bot.send_message(message.chat.id, 'New films found!')
                bot.send_message(message.chat.id, 'Do you want to watch a trailer = /trailer or get a link to watch the film? = /watch or another genre? = /search')
                if message.text == '/trailer':
                    bot.send_message(message.chat.id, 'Here is a trailer for you:')
                    bot.send_message(message.chat.id, 'Kung Fu Panda Trailer: https://www.youtube.com/watch?v=PXi3Mv6KMzY')
                    bot.send_message(message.chat.id, 'How to Train Your Dragon Trailer: https://www.youtube.com/watch?v=naXUDQY2vBM')
                    bot.send_message(message.chat.id, 'Sonic the Hedgehog Trailer: https://www.youtube.com/watch?v=J8hzJxb0rpc')
                if message.text == '/watch1':
                    bot.send_message(message.chat.id, 'You can watch films at these websites:')
                    bot.send_message(message.chat.id, '1. Netflix: https://www.netflix.com')
                    bot.send_message(message.chat.id, '2. Amazon Prime Video: https://www.primevideo.com')
                    bot.send_message(message.chat.id, '3. Hulu: https://www.hulu.com')
            if message.text == '/adventure':
                bot.send_message(message.chat.id, 'You selected Adventure genre.')
                bot.send_message(message.chat.id, 'This are films I found for you: Moana (2016),The Jungle Book (2016),Harry Potter and the Sorcerer’s/Philosopher’s Stone (2001)')
                bot.send_message(message.chat.id, 'New films found!')
                bot.send_message(message.chat.id, 'Do you want to watch a trailer = /trailer1 or get a link to watch the film? = /watch or another genre? = /search')
                if message.text == '/trailer1':
                    bot.send_message(message.chat.id, 'Here is a trailer for you:')
                    bot.send_message(message.chat.id, 'Moana Trailer: https://www.youtube.com/watch?v=LKFuXETZUsI')
                    bot.send_message(message.chat.id, 'The Jungle Book Trailer: https://www.youtube.com/watch?v=5mkm22yO-bs')
                    bot.send_message(message.chat.id, 'Harry Potter and the Sorcerer’s/Philosopher’s Stone Trailer: https://www.youtube.com/watch?v=VyHV0BRtdxo')
                if message.text == '/watch1':
                    bot.send_message(message.chat.id, 'You can watch films at these websites:')
                    bot.send_message(message.chat.id, '1. Netflix: https://www.netflix.com')
                    bot.send_message(message.chat.id, '2. Amazon Prime Video: https://www.primevideo.com')
                    bot.send_message(message.chat.id, '3. Hulu: https://www.hulu.com')
            if message.text == '/comedy':
                bot.send_message(message.chat.id, 'You selected Comedy genre.')
                bot.send_message(message.chat.id, 'This are films I found for you: Despicable Me (2010),Home Alone (1990),Diary of a Wimpy Kid (2010)')
                bot.send_message(message.chat.id, 'New films found!')
                bot.send_message(message.chat.id, 'Do you want to watch a trailer = /trailer2 or get a link to watch the film? = /watch or another genre? = /search')
                if message.text == '/trailer2':
                    bot.send_message(message.chat.id, 'Here is a trailer for you:')
                    bot.send_message(message.chat.id, 'Despicable Me Trailer: https://www.youtube.com/watch?v=sUkZFetWYY0')
                    bot.send_message(message.chat.id, 'Home Alone Trailer: https://www.youtube.com/watch?v=CK2B1r6aX6M')
                    bot.send_message(message.chat.id, 'Diary of a Wimpy Kid Trailer: https://www.youtube.com/watch?v=1gY6k7rZ2cA')
                if message.text == '/watch1':
                    bot.send_message(message.chat.id, 'You can watch films at these websites:')
                    bot.send_message(message.chat.id, '1. Netflix: https://www.netflix.com')
                    bot.send_message(message.chat.id, '2. Amazon Prime Video: https://www.primevideo.com')
                    bot.send_message(message.chat.id, '3. Hulu: https://www.hulu.com')
            if message.text == '/horror':
                bot.send_message(message.chat.id, 'You selected Horror genre.')
                bot.send_message(message.chat.id, 'This are films I found for you: Goosebumps (2015), Monster House (2006), Hotel Transylvania (2012)')
                bot.send_message(message.chat.id, 'New films found!')
                bot.send_message(message.chat.id, 'Do you want to watch a trailer = /trailer3 or get a link to watch the film? = /watch or another genre? = /search')
                if message.text == '/trailer3':
                    bot.send_message(message.chat.id, 'Here is a trailer for you:')
                    bot.send_message(message.chat.id, 'Goosebumps Trailer: https://www.youtube.com/watch?v=8Zfx0Z1Z2Wo')
                    bot.send_message(message.chat.id, 'Monster House Trailer: https://www.youtube.com/watch?v=8v3wQYdTo8g')
                    bot.send_message(message.chat.id, 'Hotel Transylvania Trailer: https://youtu.be/jgdl2mxX9W0?si=Xpr5Z7b5H-7FLV-l')
                if message.text == '/watch1':
                    bot.send_message(message.chat.id, 'You can watch films at these websites:')
                    bot.send_message(message.chat.id, '1. Netflix: https://www.netflix.com')
                    bot.send_message(message.chat.id, '2. Amazon Prime Video: https://www.primevideo.com')
                    bot.send_message(message.chat.id, '3. Hulu: https://www.hulu.com')
            if message.text == '/fantasy':
                bot.send_message(message.chat.id, 'You selected Fantasy genre.')
                bot.send_message(message.chat.id, 'This are films I found for you: The Chronicles of Narnia: The Lion, the Witch and the Wardrobe (2005),Alice in Wonderland (2010),The Lord of the Rings: The Fellowship of the Ring (2001)')
                bot.send_message(message.chat.id, 'New films found!')
                bot.send_message(message.chat.id, 'Do you want to watch a trailer = /trailer4 or get a link to watch the film? = /watch or another genre? = /search')
                if message.text == '/trailer4':
                    bot.send_message(message.chat.id, 'Here is a trailer for you:')
                    bot.send_message(message.chat.id, 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe Trailer: https://www.youtube.com/watch?v=JpK0jZ9zL4E')
                    bot.send_message(message.chat.id, 'Alice in Wonderland Trailer: https://www.youtube.com/watch?v=naXUDQY2vBM')
                    bot.send_message(message.chat.id, 'The Lord of the Rings: The Fellowship of the Ring Trailer: https://www.youtube.com/watch?v=V75dMMIW2B4')
                if message.text == '/watch1':
                    bot.send_message(message.chat.id, 'You can watch films at these websites:')
                    bot.send_message(message.chat.id, '1. Netflix: https://www.netflix.com')
                    bot.send_message(message.chat.id, '2. Amazon Prime Video: https://www.primevideo.com')
                    bot.send_message(message.chat.id, '3. Hulu: https://www.hulu.com')
            
            elif message.text == '/watch':
                bot.send_message(message.chat.id, 'You can watch films at these websites:')
            elif message.text == '/recommend':
                bot.send_message(message.chat.id, 'I recommend you to watch Inception, The Matrix, and Interstellar!')
            else:
                bot.send_message(message.chat.id, 'You are already in a session!')
bot.polling()        