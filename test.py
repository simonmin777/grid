from sample import Grid
import sqlite3

def test_init_01():
    print('In test 01')
    x = Grid()
    assert x.is_valid() is False
    y = Grid([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert y.is_valid() is True

def test_init_02():
    print('In test 02')
    # x = Grid()
    y = Grid([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # assert str(x) == '0, 0, 0, 0, 0, 0, 0, 0, 0'
    assert str(y) == '\n1, 2, 3, \n4, 5, 6, \n7, 8, 9, '

def test_sql_01():
    print('In sql test 01')
    conn = sqlite3.connect('db01')
    curs = conn.cursor()
    # tblcmd = 'create table people (name char(30), job char(10), pay int(4))'
    # curs.execute(tblcmd)
    tblcmd = 'insert into people values (?, ?, ?)'
    rows = [['tom', 'mgr', 10000],
            ['kim', 'adm', 3000],
            ['pat', 'dev', 9000]]
    curs.executemany(tblcmd, rows)
    conn.commit()
    print('curs.rowcount =', curs.rowcount)
    curs.execute('select * from people')
    for row in curs.fetchall():
        print(row)

    assert True is True

# start top level
if __name__ == '__main__':
    test_sql_01()

# end of file
