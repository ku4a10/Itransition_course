import json, re, psycopg2

#Fix the json format and load the data
with open('task1/data/task1_d.json', 'r', encoding='utf-8') as f:
    raw_data = f.read()
    converted_data = re.sub(r':(\w+)=>', r'"\1":', raw_data) 
    data = json.loads(converted_data)

for item in data:
    price = item['price']

    if price.startswith('$'):
        item['currency'] = 'USD'
    elif price.startswith('€'):
        item['currency'] = 'EUR'

    price = price[1:]  
    price = price.replace(',', '')  

    item['price'] = round(float(price), 2)

#Connect to the database
conn = psycopg2.connect(
    database="books_db",
    user="postgres",
    password="Admin",
    host="localhost",
    port=5432
)

cursor = conn.cursor()
cursor.execute('''
    DROP TABLE IF EXISTS books;
               
    CREATE TABLE books(
    id VARCHAR(25) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    currency VARCHAR(3) NOT NULL,
    price NUMERIC(10,2) NOT NULL
    );
''')

for item in data:
        cursor.execute(
            '''INSERT INTO books(id, title, author, genre, publisher, year, currency, price) 
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''',
            (
                item['id'],
                item['title'], 
                item['author'], 
                item['genre'], 
                item['publisher'], 
                item['year'],
                item['currency'], 
                item['price']
            )
        )
conn.commit()
cursor.close()
conn.close()