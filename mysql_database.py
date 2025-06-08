from mysql import connector

connection = connector.connect(
        host='localhost',
        user='root',
        password='Riya@2708',
        database='crypto_db'
)

query = """
     INSERT INTO crypto_tables (Name,Symbol,Date,High,Low,Open,Close,Volume, Market cap)
     VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)
     """
values = (['Name'], ['Symbol'], ['Date'],['High'], ['Low'], ['Open'],['Close'], ['Volume'], ['Market cap'] )







