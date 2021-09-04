import sqlite3

with sqlite3.connect('example.db') as conn:
    conn.row_factory = sqlite3.Row
    # 커서 얻기
    cur = conn.cursor()

    # 1. 커서를 이터레이터(iterator)로 사용
    print("-------------------- 1 --------------------")
    cur.execute('select * from articles')
    for row in cur:
        # row 객체로 데이터를 얻을 수 있음. 튜플 타입의 결과를 얻음.
        print(row["id"])

    # 2. fetchall로 결과 리스트를 얻음
    print("-------------------- 2 --------------------")
    cur.execute('select * from articles')
    for row in cur.fetchall():
        print(row["id"])

    # 3. fetchone으로 한 레코드씩 결과를 얻음
    print("-------------------- 3 --------------------")
    cur.execute('select * from articles')
    print(cur.fetchone()["id"])  # 1번째 레코드를 얻음
    print(cur.fetchone()["id"])  # 2번째 레코드를 얻음
