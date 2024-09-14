# Создать в БД SQLite таблицу с несколькими колонками (3-5 колонок) из  XLSX-таблицы (Sample-sales-data-excl). Заполнить их соответствующими данными, a) задавая в программы несколько INSERT (не менее 10) с конкретными значениями.
#     б) загружая в цикле непосредственно из XLSX-таблицы (+3 балла)
    
# Построить запросы SELECT
# 1) Для выборки записей по некоторому критерию одного (или 2-х) значений
#          SELECT a, b FROM t1 WHERE c>100 AND d=4
# 2)Сгруппировать данные по одному из параметров, подсчитав сумму значений по другому параметру. 
#          SELECT a, SUM(b) FROM t1 GROUP BY  c
# Варианты: самостоятельно выбрать колонки и данные
import pandas as pd
import sqlite3 as sq

#usecols - читаем только некоторые колонки
df = pd.read_excel('Sample-sales-data-excel.xlsx',sheet_name='Orders',header=0,usecols=['Category','Sub-Category','Sales','Quantity','Profit'])

# #задание бессмысленное, так как есть прямые функции в pandas для записи в sql
# # тут мы возвращаем типы данных для автоматизации, хотя при считывании в xlsx уже писали...
# def dtypes_to_sqlite(dtype):
#     if pd.api.types.is_integer_dtype(dtype):
#         return 'INTEGER'
#     elif pd.api.types.is_float_dtype(dtype):
#         return 'REAL'
#     else:
#         return 'TEXT'

# fields_types = ', '.join([f'"{field}" {dtypes_to_sqlite(dtype)}' for field, dtype in zip(df.columns,df.dtypes)])

# with sq.connect("xl_to_db.db") as con:
#     cur = con.cursor()
# #     создаем бд
#     cur.execute(f"""
#     CREATE TABLE IF NOT EXISTS orders (
#         {fields_types}
#     )""")
#     cur.execute(f"INSERT INTO orders (

#     )")

with sq.connect("xl_to_db.db") as con:
    cur = con.cursor()

    df.to_sql(name="orders",con=con,if_exists='replace',index=False)

    #1
    a = pd.read_sql_query("""
    SELECT Category, Sales 
    FROM orders 
    WHERE Quantity > 10 AND Profit > 100
    """, con)
    print(a)
    
    #2
    b = pd.read_sql_query("""
    SELECT Category, SUM(Sales) 
    FROM orders 
    GROUP BY Category
    """, con)
    print(b)