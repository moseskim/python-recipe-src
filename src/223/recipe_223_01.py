import sqlite3

# example.db에 접속(아니면 DB가 생성됨)
with sqlite3.connect('example.db') as conn:
    # 커서 얻기
    cur = conn.cursor()

    # 테이블 작성
    cur.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')

    # Insert 실행
    cur.execute("INSERT INTO articles VALUES (1,'오늘 아침 식사','생선을 먹었습니다','2020-02-01 00:00:00')")
    cur.execute("INSERT INTO articles VALUES (2,'오늘 점심 식사','카레를 먹었습니다.','2020-02-02 00:00:00')")
    cur.execute("INSERT INTO articles VALUES (?, ?, ?, ?)", (3, '오늘 저녁 식사', '햄버거를 먹었습니다', '2020-02-03 00:00:00'))
    # 커밋
    conn.commit()
