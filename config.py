<<<<<<< HEAD
import os
basedir = os.path.abspath(os.path.dirname(__file__))

FTP_URI = 'ftp://USER:PASS@HOST/users.csv'
# FTP_URI = 'ftp://trent:r0uefh1r@localhost/users6.csv'
DATABASE_URI = os.path.join(basedir, 'stats.db')
LOG = os.path.join(basedir, 'checker.log')
DEBUG = True
# DEBUG = False


TEST_FTP_URI = 'file://' + os.path.join(basedir, 'fixtures', 'users.csv')
TEST_DATABASE_URI = os.path.join(basedir, 'test.db')
TEST_LOG = os.path.join(basedir, 'test_checker.log')
||||||| merged common ancestors
=======
import os
basedir = os.path.abspath(os.path.dirname(__file__))

FTP_URI = 'ftp://USER:PASS@HOST/users.csv'
DATABASE_URI = os.path.join(basedir, 'stats.db')
LOG = os.path.join(basedir, 'checker.log')

TEST_FTP_URI = 'file://' + os.path.join(basedir, 'fixtures', 'users.csv')
TEST_DATABASE_URI = os.path.join(basedir, 'test.db')
TEST_LOG = os.path.join(basedir, 'test_checker.log')
>>>>>>> 92cf4ab0ffc57688ce6d13f0cbbf3bd99937ecef
