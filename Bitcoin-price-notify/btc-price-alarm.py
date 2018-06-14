import requests
from kavenegar import *

api = KavenegarAPI('YOUR_API_KEY')

r = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(r.json()['data']['amount'])

params = {

'sender': '100065995',
'receptor':'NUMBER_TO_RECEIVE',
'message' : 'Bitcoin price: '+str(price)+'$'
}
response = api.sms_send(params)

