#%%
import requests
import json
# %%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
res = requests.get(url)
# %%
if res:
  print(res)
else:
  print('Falhou')
# %%
res.text
# %%
dolar = json.loads(res.text)['USDBRL']
dolar

# %%
dolar['bid']

# %%
print( f" 20 dólares hoje custam {round((float(dolar['bid']) * 20), 2)} reais")
# %%
