import sqlite3

# DB에 접속
with sqlite3.connect('example.db') as conn:
    # 커서 얻기
    cur = conn.cursor()

    # 1. 커서를 이터레이터(iterator)로 사용
    print("-------------------- 1 --------------------")
    cur.execute('select * from articles')
    for row in cur:
        # row 객체로 데이터를 얻을 수 있음. 튜플 타입의 결과를 얻음.
        print(row)
        # 튜플 타입이므로 지정한 컬럼을 얻을 때는 인덱스로 지정함.
        print(row[0])

    # 2. fetchall로 결과 리스트를 얻음
    print("-------------------- 2 --------------------")
    cur.execute('select * from articles')
    for row in cur.fetchall():
        print(row)

    # 3. fetchone으로 한 레코드씩 결과를 얻음
    print("-------------------- 3 --------------------")
    cur.execute('select * from articles')
    print(cur.fetchone())  # 1번째 레코드를 얻음
    print(cur.fetchone())  # 2번째 레코드를 얻음
