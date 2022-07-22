import psycopg2
import csv, re, os 
from config import config
from datetime import datetime, timezone, timedelta

def connect():
    connection = None
    try:
        params = config()
        print("Connection to the database ...")
        connection = psycopg2.connect(**params)

        cur = connection.cursor()
        cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        tables = cur.fetchall()
        filetype = "postgres"
        print("extracting data and writing data to disk ...")
        for i in range(len(tables)):
            table = str(tables[i])
            table = re.sub("[(',)]", "", table)
            query = ("SELECT * FROM {}").format(table)
            cur.execute(query)
            column_names = [[desc[0] for desc in cur.description]]
            result = cur.fetchall()
        
            column_names.extend(result)
            
            write_csv(table, column_names, filetype, day)
            read_csv()
        print("Done.")
        return
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            cur.close()
            connection.close()

            print("Database connection finished.")

def read_csv():
    path = "step1/data/order_details.csv"
    archive = []
    filetype = "csv"
    name = os.path.basename(path).replace(".csv", "")
    with open(path, "r", encoding='UTF-8') as csvfile:
        r = csv.reader(csvfile, delimiter=",")
        for linha in r:
            archive.append(linha)
    
    write_csv(name, archive, filetype, day)

    return 


def write_csv(name, result, filetype, day):
    path = f"dados/{filetype}/{name}/{day}/"
    if not os.path.exists(path):
        os.makedirs(path)

    with open(f"{path}/{name}.csv", "w", newline='', encoding="utf-8") as csvfile:
        w = csv.writer(csvfile, delimiter=",")
    
        for i in range(len(result)):
        
            w.writerow(result[i])

   
def time():
    fuso = timedelta(hours = -3)
    now = datetime.now(tz=timezone(fuso))
    date_time_str = now.strftime("%Y-%m-%d")
    
    return date_time_str


def day():
    fuso = timedelta(hours = -3)
    now = datetime.now(tz=timezone(fuso))
    date_time_str = now.strftime("%d/%m/%Y")
    while True:
        try:
            x = input("Enter the date of the desired day in the format dd/mm/yy.\n")
            time_1 = datetime.strptime(x,"%d/%m/%Y")
            time_2 = datetime.strptime(date_time_str,"%d/%m/%Y")
            time_interval = time_2 - time_1
            time_interval = ((str(time_interval)).split(" "))[0]
            
            if time_interval > "0":
                break
            else:
                print("Please enter an earlier date.")
        except ValueError:
            print("Use only in dd/mm/yy format.")

    x = x.replace("/", "-")
    
    return x
    
if __name__ == "__main__":
        day = day()
        connect()
        
        