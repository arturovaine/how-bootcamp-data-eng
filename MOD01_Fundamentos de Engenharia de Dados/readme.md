## Atividade

- Ler um arquivo de dados de um dataframe
- Tratar a informação recebida
- Selecionar os dados necessários
- Extrair informações dos dados
- Automatizar o processo

### _Exercício 1

A rede oficial de apostas na loteria é gerenciada pela Caixa Econômica Federal e a mesma disponibiliza todos os dados dos sorteios para consulta pública em seu site 

A proposta do exercício é coletar esses dados e levantar as informações da LotoFácil
- Qual o número mais sorteado e o menos sorteado?
- Quais combinações de números Pares(p), Ímpares(i) e Primos(np) saem por sorteio?

---
## Ambiente virtual

"O módulo venv fornece suporte para a criação de 'ambientes virtuais' leves com seus próprios diretórios de site, opcionalmente isolados dos diretórios de site do sistema. Cada ambiente virtual possui seu próprio binário Python (que corresponde à versão do binário usado para criar esse ambiente) e pode ter seu próprio conjunto independente de pacotes Python instalados nos diretórios do site."

https://docs.python.org/pt-br/3/library/venv.html

### Instalação:


`pip install virtualenv`

ou

`sudo apt install python3-venv`


### Iniciar ambiente virtual:

`virtualenv .venv`

ou 

`python3 -m venv .venv`

### Ativar o ambiente:

`source .venv/bin/activate`

## Python


Importar bibliotecas:

```Python
import requests
import pandas as pd
import collections
import sys
```

- [Requests](https://pypi.org/project/requests/)

"Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!"

- [pandas](https://pandas.pydata.org/docs/)

"pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language."

- [collections](https://docs.python.org/3/library/collections.html)

"This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple."

collections' classes:

namedtuple(), deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString

- [sys](https://docs.python.org/3/library/sys.html)

System-specific parameters and functions

"This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available."

---

### Setar endpoint


```Python
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
url = sys.argv[1]
```

```Python
r = requests.get(url)
```


