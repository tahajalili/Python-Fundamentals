# Bitcoin Price Notifier

### How it works:

+ This program use [Requests](http://docs.python-requests.org/en/master/) library to receive date from 
+ [Coin Base](https://developers.coinbase.com/docs/wallet/guides/price-data) API.
+ It takes data from the API and process the JSON formatted data to extract the price value from it.
+ After that, it uses [Kavenegar SMS service](http://github.com/kavenegar) to send the price with SMS.

### How to use:

1.You must have **Python 3 installed on your machine**.

2.You should sign-up in [Kavenegar](http://kavenegar.com). 

3.You should install kavenegar module:
#### linux and mac:

```python
pip3 install kavenegar
```
#### windows:

```python
pip install kavenegar
```

4.Get your API key in [Coin Base](https://developers.coinbase.com/docs/wallet/guides/price-data).

5.Set your own API key in the code.

6.Enjoy!

### Feel Free to Contribute and improve my code.
#### Any idea is welcome at : 
⋅⋅* http://twitter.com/tahajalili 
⋅⋅* tahajalili@gmail.com

