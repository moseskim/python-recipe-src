import MySQLdb

# 연결 정보
con_info = {"user":"db user", "passwd":"db password", "host":"localhost", "db":"sample", "charset":"utf8"}

# DB 연결
with MySQLdb.connect(**con_info) as con:

    # 커서 얻기
    with con.cursor() as cur:

        # 쿼리 실행
        sql = "select id, body, post_code, created from posts where id > %s and post_code in %s"
        cur.execute(sql, (1, [1, 2, 3], ))

        # 실행 결과를 모두 얻음
        rows = cur.fetchall()
            
        # 한 레코드씩 표시
        for row in rows:
            print(row)
