
import os, re, csv, json
import psycopg2
from config import config

def connect():
    connection = None
    try:
        params = config()
        print("Connection to the database step2 ... ")
        connection = psycopg2.connect(**params)

        cur = connection.cursor()

        way, name, pre = archive_search()

        print("Sending the data to the database ...")
        create_tables(cur, way, name)

        print("Writing json output file ...")
        query_orders(cur, name)
        print("Done.")
        return
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    

    finally:
        if connection is not None:
            connection.commit()
            cur.close()
            connection.close()
            print("Database connection finished.")


def archive_search():
    main_path = "./dados"
    way = []
    for root, dirs, files in os.walk(main_path):
        for name in files:
            a = os.path.join(root, name)
            way.append(a)

    archive = []
    for i in range(len(way)):
        name1 = os.path.split(way[i])
        name2 = os.path.basename(name1[0])
        name2 = re.sub("[-]", "_", name2)
        name1 = os.path.splitext(name1[1])
        name = f"{name1[0]}_{name2}"
        archive.append(name)

    return way, archive, name2

def read_csv(a, way):
    
    way = way[a]
    archive = []
    with open(way, "r", encoding='UTF-8') as csvfile:
        r = csv.reader(csvfile, delimiter=",")
        for linha in r:
            archive.append(linha)

    return archive

def create_tables(cur, way, name):
    
    for i in range(len(name)):
        colum = read_csv(i, way)[0]
        query = ("CREATE TABLE IF NOT EXISTS {} ()").format(name[i],)
        cur.execute(query)
        
        for k in range(len(colum)):
            query3 = ("ALTER TABLE {} ADD COLUMN IF NOT EXISTS {} text").format(name[i],colum[k],)
            cur.execute(query3)

        query3 = ("SELECT * FROM {}").format(name[i])
        cur.execute(query3)
        result= cur.fetchone()
        
        if result == None:
            copy_sql = ("COPY {} FROM stdin WITH CSV DELIMITER as ','").format(name[i],)

            with open(way[i], 'r') as f:
                next(f)
                cur.copy_expert(sql=copy_sql, file=f)
    return name

def query_orders(cur, names):
    
    indices = ["orders", "order_details"]
    gg=[]
    order_ids = []

    for name in names:
        
        if indices[0] in name:
            if order_ids == []:
                cur.execute(("SELECT order_id FROM {}").format(name))        
                order_ids = cur.fetchall()
                
            dictionary = {}
            for order_id in order_ids:
                tt = []
                products = {}
                cur.execute(("SELECT * FROM {} WHERE order_id IN (%s)").format(name), (order_id,))
                columns = [[desc[0] for desc in cur.description]]
                results = cur.fetchone()
                
                for column in columns: 
                    results = dict(zip(column, results))

                day = name.replace(indices[0],"")
                details = f"{indices[1]}{day}"
                cur.execute(("SELECT * FROM {} WHERE order_id IN (%s)").format(details), (order_id,))
                columns_details = [[desc[0] for desc in cur.description]]
                results_details= cur.fetchall()
                
                for column_detail in columns_details:
                    for result_detail in results_details:
                        tt.append((dict(zip(column_detail, result_detail))))
                
                products.update({"product":tt})
                dictionary.update({"data":{day[1:].replace("_","-"):{**results, **products}}})
                
                gg.append(dictionary["data"])
            
            json_file(gg)           


def json_file(data):
    with open("./result-query.json", 'w', encoding="UTF-8") as fp:
        json.dump(data, fp) 

    

def executeif():
    try:
        archive_search()
        connect()
    except UnboundLocalError as error:
        print("Run Step1 before Step2.")

if __name__ == "__main__":
    #connect()
    executeif()
