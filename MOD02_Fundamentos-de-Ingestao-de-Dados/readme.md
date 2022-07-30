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

```Python
def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    #url = 'https://economia.awesomeapi.com.br/last/{}'.format(moeda)
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
```


```Python
# %%
cotacao(20, 'USD-BRL')

# %%
cotacao(20, 'JPY-BRL')
```

```Python
# %%
try:
    cotacao(20, 'Rhuan')
except:
    pass

# %%
try:
    10/0
except Exception as e:
    print(e)
else:
    print("ok")

```


```Python
# %%

def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
```



```Python
# %%
    lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "RPL-BRL",
        "JPY-BRL",
    ]
```



```Python

multi_moeda(20, "USD-BRL")
# %%


def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func


@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
```


```Python
#%%

multi_moeda(20, "USD-BRL")
multi_moeda(20, "EUR-BRL")
multi_moeda(20, "BTC-BRL")
multi_moeda(20, "RPL-BRL")
multi_moeda(20, "JPY-BRL")


```


Para não precisar utilizar "try-except", é possívei utilizar um decorador:

```Python
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func
```

- `args` : arguments
- `kargs` : key arguments


```Python
# %%
import backoff
import random

```

```Python
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"
```


```Python
# %%
test_func()

# %%
test_func(42)

# %%
test_func(42, 51, nome="rhuan")
```


```Python
#%%
import logging

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

```


```Python
# %%

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f" RND: {rnd} ")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"


# %%
test_func()

# %%


## Criando logs

```