import mysql.connector as myssql

def mysql(listed):
    try: 
        mydb = myssql.connect(
            host="localhost",
            user="root",
            password="admin",
            database="tradingview"
        )

        mycursor = mydb.cursor(buffered=True)# buffer is true nabashe misheUnread result found

        mycursor.execute("SHOW TABLES")
        name = 'omidd'
        for table in mycursor:
            if name in table:
                
                price = listed[0]
                print(price)
                price1= listed[1]
                print(price1)
                val = (price,price1)
                mycursor.execute("INSERT INTO omidd (idomid,omidcol)  VALUES (%s,%s)", val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                break
    except (myssql.Error, myssql.Warning) as e:
        print(e)
        return None

def seq():
    while(True):
            prices=[]
            symbols = ["CADAED","AEDAUD"]
            for symbol in symbols: 
                u = input("enter : ") 
                prices.append(u)
            print(prices)
            mysql(prices)
            prices.clear()

if __name__ == "__main__":
    seq()
