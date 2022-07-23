# SQL 

- Criando um banco de dados com docker
- Select + Where + Group by
- CTEs + Window functions
- Deduplicando dados
- Criando, atualizando e deletando tabelas e views
- Acessando um banco de dados com Python
- Conectandoa uma ferramento de BI


<br>

## Docker
<br>

Dockerfile

```Dockerfile
FROM httpd
COPY ./web /usr/local/apache2/htdocs/
EXPOSE 
```

- "httpd" se refere a uma imagem de servidor Apache, sem indicar versão, indico a mais recente

- COPY (origem) (destino), copiando conteúdo para a pasta raiz do servidor, para o servidor exibir

- EXPOSE para abrir a porta do container

```bash
docker build -t web_apache .
```
"." para referenciar a pasta na qual estou executando

