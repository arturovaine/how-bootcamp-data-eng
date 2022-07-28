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
# url = sys.argv[1]
```

"For every invocation of Python, sys.argv is automatically a list of strings representing the arguments (as separated by spaces) on the command-line. The name comes from the C programming convention in which argv and argc represent the command line arguments." 
https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script


```Python
r = requests.get(url, verify=False)
# https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
```

Utilizou-se o paramêtro de verificação com valor `False` devido ao erro de SSL no acesso à API.

O valor de `r` deverá ser `<Response [200]>`, ou seja, requisição bem sucedida, e, diferentemente da resposta `204`, a resposta deve possuir um `body`:

```Python
r.text
```
`r.text` irá retornar o código HTML da página:

```HTML
'{\r\n  "html": "<table class=\\"tabela-resultado lotofacil\\">\\r\\n<thead>\\ ... </thead></tbody>\\r\\n</table>"\r\n}'

```

Para filtrar o corpo da resposta:

```Python
r.text
r_text = r.text.replace('\\r\\n', '')
r_text = r.text.replace('"\r\n}', '')
r_text = r.text.replace('{\r\n  "html": "', '')
r_text
```

Criar dataframe:

```Python
df = pd.read_html(r_text)
```

`type(df)` retorna `list`,

e `type(df[0])` retorna `pandas.core.frame.DataFrame`

É isto, o dataframe a ser analisado está na primeira posição da lista.

A execução da request, no dia da submissão deste readme, retornou uma tabela com 10499 linhas 32 colunas.

Fazer um backup, por precaução:

`df1 = df`

`df=df[0].copy()`

Verificar títulos no cabeçalho:

`df.columns` que deve estar com `\r\n`

Para corrigir:

```Python
new_columns = df.columns
new_columns = list(i.replace('\\r\\n', '') for i in new_columns)
new_columns

df.columns = new_columns # Atribuir novo cabeçalho
df[df['Bola1'] == df['Bola1']] # Para limpar os 'NaN'
```

Na Lotofácil são escolhidos 15 números em 25.
Então, para criar a população de 1 a 25:

`nr_pop = list(range(1,26))`

Os grupos de análise serão:

`nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18]`

`nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]`

`nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]`


"comb" para combinação dos grupos

e variáveis para as frequências:
```Python
comb = []
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0
```

Definir colunas a iterar a contagem de frequência:

```Python
lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
              'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12',
              'Bola13', 'Bola14', 'Bola15']
```              

Iterar contagem:


```Python
for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+str(v_primos)+'np')
```

Frequências calculadas:

```Python
freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]
```

Ordenar pela 2a chave da tupla:

```Python
freq_nr
freq_nr.sort(key=lambda tup: tup[1])
freq_nr[0]  # primeiro
freq_nr[-1]  # ultimo
```

Organizando os resultados:

```Python
counter = collections.Counter(comb)
resultado = pd.DataFrame(counter.items(), columns=['Combinacao', 'Frequencia'])
resultado['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()
resultado = resultado.sort_values(by='p_freq')
```

Imprimir os resultados:

```Python
print('''
O número mais frequente é o:  {}
O número menos frequente é o:  {}
A combinação de Pares, Ímpares e Primos mais frequente é: {} com a frequencia de: {}%
'''.format(freq_nr[-1][0], freq_nr[0][0], resultado['Combinacao'].values[-1], int((resultado['p_freq'].values[-1]*100)*100)/100)
)
```

