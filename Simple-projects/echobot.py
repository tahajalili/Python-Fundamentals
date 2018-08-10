import requests
from time import sleep


TOKEN = "615579401:AAHLZv3hI-FiBpboa7DWMejTOt7ZERawags"
url = "https://api.telegram.org/bot{}/".format(TOKEN)

name = None
data = None
events = dict()

def get_updates_json(request):  
	params = {'timeout': 50, 'offset': None}
	response = requests.get(request + 'getUpdates', data=params)
	return response.json()


def last_update(data):  
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]

def last_message(data):
	result = get_updates_json(url)['result'][-1]['message']['text']
	return result

def last_sender(data):
	first_name = get_updates_json(url)['result'][-1]['message']['from']['first_name']
	last_name = get_updates_json(url)['result'][-1]['message']['from']['last_name']
	user_id = get_updates_json(url)['result'][-1]['message']['from']['username']
	datas = [first_name,last_name,user_id]
	return datas
	

def get_chat_id(update):  
	chat_id = update['message']['chat']['id']
	return chat_id

def send_message(chat, text):  
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response



# print(last_sender(last_update(get_updates_json(url))))



def main():  
	update_id = last_update(get_updates_json(url))['update_id']
	messaage = last_message(last_update(get_updates_json(url)))
	sender = last_sender(last_update(get_updates_json(url)))
	while True:
		if update_id == last_update(get_updates_json(url))['update_id']:
			send_message("530603331", messaage+"\nsender "+sender[0]+'\n'+sender[1]+' '+sender[2])
			update_id += 1
				
	sleep(1)       
	  
	

if __name__ == '__main__':  
	main()

