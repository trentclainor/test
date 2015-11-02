# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
# import datetime

import config
from checker import check_passwd, get_data, save_log
from stats import connect_db, set_stat, init_stat, sqlite3


class Test(unittest.TestCase):

    def setUp(self):
        self.con = connect_db(config.TEST_DATABASE_URI)
        self.assertIsInstance(self.con, sqlite3.Connection)
        self.cur = self.con.cursor()
        self.assertIsInstance(self.cur, sqlite3.Cursor)
        r = init_stat(self.cur)
        self.assertTrue(r)

    def tearDown(self):
        self.con.close()

    def test_passwd(self):
        """ Test good/bad password """
        self.assertTrue(check_passwd('11Qaaa'))
        self.assertFalse(check_passwd('aaaQaaa'))
        self.assertFalse(check_passwd('111111'))
        self.assertFalse(check_passwd('111aaa'))
        self.assertFalse(check_passwd('1aQaa'))
        self.assertFalse(check_passwd('1aQ'))

    def test_write_db(self):
        init_stat(self.cur)
        date = datetime.now()
        name = u'test'
        r = set_stat(self.cur, date, name)
        self.assertTrue(r)
        self.con.commit()
        r = self.cur.execute('select date,name,cnt from visits where name=:name', {'date': date.strftime('%Y-%m-%d'), 'name': name}).fetchone()
        self.assertEqual(r, (date.strftime('%Y-%m-%d'), name, 1))

    def test_csv(self):
        init_stat(self.cur)
        rows = get_data(config.TEST_FTP_URI)
        logs = {}
        cnt = 0
        for row in rows:
            cnt += 1
            self.assertIsInstance(row[0], datetime)
            self.assertIsInstance(row[1], str)
            logs[row[1]] = row[0]
            if cnt == 3:
                self.assertFalse(check_passwd(row[2]))
            else:
                self.assertTrue(check_passwd(row[2]))
        save_log(logs, config.TEST_LOG)
        with open(config.TEST_LOG) as f:
            x = f.read()
            self.assertEqual(x, 'user2\nuser3\nuser1')
        f.closed


if __name__ == '__main__':
    unittest.main()
