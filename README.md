# code-challenge
## pre-installed packages required
- Docker
- Git
- Python3
- lib psycopg2

to install lib psycopg2
```
pip install psycopg2 
```

### Cloning repository

to clone the repository use the command:
```
git clone https://github.com/G-rossi98/code-challenge.git
```
### Conteiner with db image 
go to the directory
```
cd ./code-challenge
```
and run below command to create db in conteiner 
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
