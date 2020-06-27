import json, urllib.request
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sum", required=True,
	help="Введите сумму, которую хотите перевести")
ap.add_argument("-si", "--sign", required=True, type=str,
	help="path to output model")
args = vars(ap.parse_args())

def currency(number, sign):
    
    currency_list = ['EUR', 'GBP', 'UAH']
    print("Доступленые валюты для перевода")
    
    for cal in range(len(currency_list)):
        print(currency_list[cal], end=' ')

    if args['sign'] in currency_list:
        try:    
            request = "https://free.currencyconverterapi.com/api/v5/convert?q=USD_"+sign
            #print(request)
            responce = urllib.request.urlopen(request)
            result = json.loads(responce.read())
            currency = result['results']['USD_'+sign]['val']
            print("\nОтношение доллара USD к " +sign + ": "+ str(currency))
            calc = float(currency) * float(number)
            return print('%.2f'%calc, sign)
        except KeyError:       
            print('\nКод валюты не может быть меньше или больше 3х символов')
    else:
        print('\nЭта валюта недоступна')
        


currency(args['sum'], args['sign'])