from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def alllist():
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = '''
            select 
                a.no, a.title, a.contents, a.hit, a.reg_date, a.g_no, a.o_no, a.depth
                from board a, user b
                where a.user_no = b.no
            order by a.g_no desc, a.o_no desc, a.depth asc
            '''
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f"connect is failed. {e}")

def findbyno(postno):
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = '''
            select 
                a.no, a.title, a.contents, a.hit, a.reg_date, a.g_no, a.o_no, a.depth, a.user_no
                from board a, user b
                where a.user_no = b.no
                and a.no = %s
            '''
        cursor.execute(sql, (postno, ))

        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

    except OperationalError as e:
        print(f"connect is failed. {e}")


def write(title, content, user_no):
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = 'insert into board values(null, %s, %s, 0, now(), IFNULL((select max(g_no) from board a), 0) + 1, 1, 0, %s)'
        count = cursor.execute(sql, (title, content, user_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def update(title, contents, postno):
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = 'update board set title = %s, contents = %s where no = %s'
        count = cursor.execute(sql, (title, contents, postno))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'error: {e}')

def delete(postno):
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = 'delete from board where no = %s'
        count = cursor.execute(sql, (postno, ))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'error: {e}')



def reply():
    pass

def comment():
    pass

def count():
    pass

def increment_hit(postno):
    try:
        db = conn()

        cursor = db.cursor()

        sql = 'update board set hit = hit+1 where no = %s'
        count = cursor.execute(sql, (postno, ))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'error: {e}')



def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')
