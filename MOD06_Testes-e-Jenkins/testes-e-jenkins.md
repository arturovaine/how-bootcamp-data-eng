# Testes e Jenkins

- Por que testar?
- Testes unitários
- Parametrização de Testes
- Fixtures
- Mocks/patches e monkey patches
- Testes de Integração
- Cobertura de Testes
- Jenkins
<br /><br />

## Por que testar? Motivação:

- Ganho de **produtividade** (ao não testar manualmente, prints...)
- **Conformidade**, tranquilidade ao realizar mudanças no código e saber se algo quebrou 
- Testes representam **documentação**
- Descoberta de **bugs** que poderiam passar despercebidos, um **"edge case"**
<br /><br />

### Modos de testes: **White box vs Black Box**

- **Black box**: em testes deste tipo, o desenvolvedor não conhece o funcionamento interno de uma aplicação e só testa se a saída ocorre conforme o esperado. Está com pressa para entregar uma funcionalidade? Escreva pelo menos testes do tipo Black Box.
  
- **White box**: neste tipo, o desenvolvedor cria testes para todos os mecanismos internos de uma aplicação. É o oposto da Black Box. Quer garantir que seu código está robusto e sem bugs? Escreva testes para toda a sua aplicação.
<br /><br />

## Testes unitários, de integração e funcionais

Testes unitário se referem a testes de uma unidade de código: uma função, um método ou classe, de forma isolada de outras partes do código.

Um teste de integração vai interagir com sistemas externos, por exemplo uma API, ou um banco de dados. Esse tipo de teste vai garantir que as conexões estão funcionando como o esperado.

Teste funcionais buscam replicar o que um usuário vai fato ver, digitar e clicar. Não são comuns em Engenharia de Dados, e geralmente são do tipo Black Box.
<br /><br />

## Testes unitários

Todo teste é uma função.

`apis.py`
```Python
class DaySummaryApi(MercadoBitcoinApi):
    type = "day-summary"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f"{self.base_endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}"

(...)
```

Para testar, arquivos devem iniciar ou terminar por "`test`", para que a biblioteca Pytest reconheça o arquivo como fonte de código de teste:

`test_apis.py`
```Python
# Para testar o método get_endpoint:

import datetime
from apis import DaySummaryApi

def test_get_endpoint():
  date = datetime.date(2021, 6, 21)
  api = DaySummaryApi(coin="BTC")

  actual = api._get_endpoint(date=date)
  expected = "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21"
  assert actual == expected # retorna True ou False

```

Para a definição de dependências, é boa prática defini-las em `requirements.txt`:

```
pytest
requests
```

E para a instalação:

```bash
pip install -r requirements.txt
```

Sendo a flag `r`:
> -r, --requirement < filename >

<br />

Para rodar testes, execute no terminal:

- `pytest`, que requer definição do Python PATH para configuração de origem de extração dos dados, módulos; ou é possível executar ...
  
- `python -m pytest` a fim de executar o `pytest` como um módulo/pacote e o Python configura o PATH diretamente, automaticamente.

***Importante:***

***É boa prática criar um teste isoladamente para cada unidade do código, cada situação, cada função...***
<br /><br />

## Parametrização de Testes

Ao longo da implementação de testes é possível que ocorra a necessidade de realizar teste de endpoint com variações de um parâmetro, por exemplo moedas diferentes, neste caso:


```Python
def test_get_endpoint_BTC():
  date = datetime.date(2021, 6, 21)
  api = DaySummaryApi(coin="BTC")
  ...


def test_get_endpoint_ETH():
  date = datetime.date(2021, 6, 21)
  api = DaySummaryApi(coin="ETH")
  ...
```

Para realizar a parametrização dos testes, a fim de evitar repetições (**DRY**-Don't Repeat Yourself), é possível utilizar o módulo `parametrize` do `pytest`:


```Python
import pytest

# Decorador:

@pytest.mark.parametrize(
  # Nomes das colunas a passar como input
  "coin, date, expected",

  # Lista de tupla de casos
  [
    ("BTC", datetime.date(2021, 6, 21), "https://www.mercadobitcoin.net/api/BTC/day-summary/2021/6/21"),
    ("ETH", datetime.date(2021, 6, 21), "https://www.mercadobitcoin.net/api/ETH/day-summary/2021/6/21"),
    ("ETH", datetime.date(2019, 1, 2), "https://www.mercadobitcoin.net/api/ETH/day-summary/2019/1/2")
  ] 
)
def test_get_endpoint(coin, date, expected):
  api = DaySummaryApi(coin=coin)
  actual = api._get_endpoint(date=date)
  assert actual == expected

```
