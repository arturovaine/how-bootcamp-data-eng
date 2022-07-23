# SQL 

- Criar um banco de dados com docker
- Select + Where + Group by
- CTEs + Window functions
- Deduplicar dados
- Criar, atualizar e deletar tabelas e views
- Acessar um banco de dados com Python
- Conectar a uma ferramento de BI


<br>

## Docker
<br>

Dockerfile

```Dockerfile
FROM httpd
COPY ./web /usr/local/apache2/htdocs/
EXPOSE 80
```

- "httpd" se refere a uma imagem de servidor Apache, sem indicar versão, indico a mais recente

- COPY (origem) (destino), copiando conteúdo para a pasta raiz do servidor, para o servidor exibir

- EXPOSE para abrir a porta do container

```bash
docker build -t web_apache .
```
"." para referenciar a pasta na qual estou executando

Step 1/3: FROM httpd -> buscar umagem, realizar download se necessário
Step 2/3: COPY... -> copiar o conteúdo do endereço indicado, para o endereço do servidor indicado
Step 3/3: EXPOSE...-> definir que a porta indicada deve ficar aberta

Para verificar que imagens estão disponíveis, já carregadas anteriormente:

```bash
docker image ls
```

Para rodar a aplicação/subir o servidor:
```bash
docker run -p 80:80 web_apache
```
tag `-p` de port, para indicar, em ordem, a porta que será aberta na máquina local, e a porta do container a ser mapeado
e a imagem a utilizar, no caso o servidor apache, `web_apache`

Para que a aplicação rode desacoplada do terminal, incluir tag `-d`, de "detach":

```bash
docker run -d -p 80:80 web_apache
```
