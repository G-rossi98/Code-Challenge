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

to clone the repository use the command
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

in the same directory, run the command run the first step where, the script will read the data from the csv file and database and rewrite them on the local disk

```
python ./step1/dbstep1.py
```

## step2

in the same directory, run the command to run the second step where, the script will read the data from local disk and put it in a new database and then have a json output file with the data

```
python ./step2/dbstep2.py
```
