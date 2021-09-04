import sqlite3
import pandas as pd
import pandas.io.sql as psql

# sqlite3에 연결
with sqlite3.connect(':memory:') as conn:
    cur = conn.cursor()

    # 샘플 테이블 생성
    cur.execute('CREATE TABLE body (id int, height float, weight float)')

    # 샘플 데이터 삽입
    cur.execute('insert into body  values (1, 165, 56)')
    cur.execute('insert into body  values (2, 177, 67)')
    cur.execute('insert into body  values (3, 168, 59)')
    cur.execute('insert into body  values (4, 171, 65)')
    
    # SELECT문으로 DataFrame 작성
    df = psql.read_sql("SELECT id, height, weight FROM body;", conn, index_col="id")

    print(df)