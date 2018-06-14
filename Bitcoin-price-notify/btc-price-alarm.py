import requests
from kavenegar import *

api = KavenegarAPI('4A6E43704C687458316F7A2B5656564E3750644B3055677A6F4C7164774E6F47')

r = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(r.json()['data']['amount'])

params = {

'sender': '100065995',
'receptor':'09125278727',
'message' : 'Bitcoin price: '+str(price)+'$'
}
response = api.sms_send(params)
#print('At this moment BitCoin is %.2f dollars.' % price)
