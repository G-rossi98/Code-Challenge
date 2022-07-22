# code-challenge

É necessario baixar a biblioteca psycopg2.

```
pip install psycopg2 
```

O banco de dados utilizado é o mesmo do desafio então, é necessario entrar no diretorio que contem o arquivo docker-compose.yml e executar o comando para subir a imagem no conteiner:

```
docker-compose up -d
```

## step1

Tendo o db do step1 rodando no conteiner vá até o diretorio:

```
./code-challenge
```

e execute o comando:

```
python ./step1/dbstep1.py
```

Aparecerá uma pasta dados contendo todo os arquivos extraidos no formato csv 

## step2

Estando no diretoirio.

```
./code-challenge
```

e com o db do step2 rodando execute o comando:

```
python ./step2/dbstep2.py
```

Aparecerá um arquivo json com o resultado da query. 
