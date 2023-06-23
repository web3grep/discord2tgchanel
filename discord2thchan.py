import requests
from sys import stderr
from json import loads
from time import sleep
import getch
from loguru import logger

def take_chat_id():
	r = requests.get(f'https://api.telegram.org/bot{tgbot_key}/getUpdates?offset=-1')
	try:
		chat_id = {channel_id}
		nickname = r.json()['result'][0]['message']['chat']['first_name']
	except Exception as error:
		print(f'Error: {error}\n {r.json()}')
		exit(':(')
	check_posts(None, chat_id, nickname)


def check_posts(old_msg_id, chat_id, nickname):
	logger.opt(colors=True).success(f'Tg acc is <green>{nickname}</green>. The bot has been successfully launched, waiting for new posts.')
	while True:
		try:
			r = requests.get(f'https://discord.com/api/v9/channels/{ds_chatid}/messages?limit=1', headers={'authorization': ds_token})
			new_msg_id = loads(r.text)[0]['id']
			if old_msg_id == None or int(old_msg_id) != int(new_msg_id):
				msg_text = loads(r.text)[0]['content']
				if old_msg_id != None:
					logger.success('A new post. The information was successfully sent to Telegram')
					if len(msg_text) > 0:
						for i in range(repeat_num):
							requests.post(f'https://api.telegram.org/bot{tgbot_key}/sendMessage',
										  json={'chat_id': {channel_username}, 'text': f'New post:\n{str(msg_text)}'})
							sleep(1)

					else:
						requests.post(f'https://api.telegram.org/bot{tgbot_key}/sendMessage',
									  json={'chat_id': {channel_username}, 'text': 'New post: empty'})
				old_msg_id = new_msg_id
		except:
			pass


logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

tgbot_key = 'TG_TOKEN' #str
ds_token = 'DS_TOKEN'  #str
ds_chatid = DS_CHANNEL_ID #последний номер в адресной строке без кавычек
repeat_num = 1
channel_username = '@CHANNEL_USERNAME'
channel_id = 'CHANNEL_ID'

take_chat_id()
