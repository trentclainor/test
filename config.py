import os
basedir = os.path.abspath(os.path.dirname(__file__))

FTP_URI = 'ftp://USER:PASS@HOST/users.csv'
DATABASE_URI = os.path.join(basedir, 'stats.db')
LOG = os.path.join(basedir, 'checker.log')

TEST_FTP_URI = 'file://' + os.path.join(basedir, 'fixtures', 'users.csv')
TEST_DATABASE_URI = os.path.join(basedir, 'test.db')
TEST_LOG = os.path.join(basedir, 'test_checker.log')
