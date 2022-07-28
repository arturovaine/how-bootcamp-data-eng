#%%
import requests
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
