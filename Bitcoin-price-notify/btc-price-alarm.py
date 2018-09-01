import requests
import notify2

r = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(r.json()['data']['amount'])

notify2.init("Bitcoin Price")
n = notify2.Notification('Live Bitcoin Price', 'BTC => '+str(price)+'$')
n.show()



# from kavenegar import *

# api = KavenegarAPI('YOUR_API_KEY')



# params = {

# 'sender': '100065995',
# 'receptor':'NUMBER_TO_RECEIVE',
# 'message' : 'Bitcoin price: '+str(price)+'$'
# }
# response = api.sms_send(params)

