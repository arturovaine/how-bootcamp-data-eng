## Fundamentos de Ingestão de Dados

- Introdução a APIs e a requests
- Tratando erros / retentativas
- Criando logs
- Utilizando o Google Chrome Inspect
- Buscando dados de imóveis

"API é um conjunto de normas que possibilita a comunicação entre plataformas através de uma série de padrões e protocolos(...)"

## API Requests

Na pasta da atividade, criar um ambiente virtual:

`virtualenv .venv`

E ativar:

`source .venv/bin/activate`

Intalar requests:

`pip install requests`

Ambiente virtual é importante não só para blindar o projeto a ser desenvolvido, mas carregar somente os pacotes a serem mesmo utilizados em caso de publicação.

Se necessário, atualizar o `pip`, gerenciador de pacotes:

`pip install --upgrade pip`

Então, em novo arquivo `main.py`, iniciar:

```Python
#%%
import requests

#%%
x = [
  12,
  13,
  41,
  51
]
```

`#%%` permite a divisão do código como no notebook jupyter.

<!-- pip install -U ipykernel -->

```Python
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
```


## Erros e retentativas

