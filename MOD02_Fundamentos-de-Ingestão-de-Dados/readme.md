## Fundamentos de Ingestão de Dados

- Introdução a APIs e a requests
- Tratando erros / retentativas
- Criando logs
- Utilizando o Google Chrome Inspect
- Buscando dados de imóveis

"API é um conjunto de normas que possibilita a comunicação entre plataformas através de uma série de padrões e protocolos(...)"

## Atividade

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

