#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse
import codecs
import csv
import sys
from datetime import datetime
import time
from timeit import default_timer as timer
try:
    from urllib.request import urlopen
    assert urlopen  # silince pyflakes
except ImportError:
    from urllib2 import urlopen

import config
from stats import connect_db, set_stat, init_stat, get_stats


def timing(f):
    """ Measuring time """

    def wrap(*args):
        """"""
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0))
        return ret
    return wrap


# @timing
def check_passwd(passwd, minlen=6, maxlen=20):
    """ Check passwd have digits, lowercase, uppercase and min, max length """

    has_digits = any(char.isdigit() for char in passwd)
    has_uppercase = any(char.isupper() for char in passwd)
    has_lowercase = any(char.islower() for char in passwd)
    return all((
        has_digits,
        has_uppercase,
        has_lowercase,
        len(passwd) >= minlen,
        len(passwd) <= maxlen,
    ))


# @timing
def get_data(url):
    """ Download .csv file from ftp and return by row
        CSV format 'YY-mm-dd HH:MM:SS,msec;username;password' """

    response = urlopen(url)
    reader = csv.reader(codecs.iterdecode(response, 'utf-8'), delimiter=';')
    for row in reader:
        try:
            row[0] = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S,%f')
            if len(row) == 3:
                yield row
            else:
                raise Exception("CSV format wrong")
        except ValueError:
            print("Date format wrong", file=sys.stderr)
        except Exception as e:
            raise Exception(e)


def save_log(logs, log_file=config.LOG):
    with open(log_file, 'w+') as f:
        f.write("\n".join(logs))
    f.closed


def main(cur, url=config.FTP_URI):
    """ Check users data and save stats and logs"""

    rows = get_data(url)
    logs = {}
    for row in rows:
        set_stat(cur, row[0], row[1])
        if not check_passwd(row[2]):
            logs[row[1]] = row[0]
    save_log(logs)


if __name__ == '__main__':
    start = timer()

    try:
        parser = argparse.ArgumentParser(description='Check user data.')
        parser.add_argument('--stats', action='store_true', help='show stats')
        args = parser.parse_args()

        con = connect_db()
        cur = con.cursor()
        if args.stats:
            stats = get_stats(cur)
            for stat in stats:
                print(stat[0], stat[1])
            con.close()
        else:
            init_stat(cur)
            main(cur)
            con.commit()
    except KeyboardInterrupt:
        print("Import data interrupted", file=sys.stderr)
    end = timer()
    print ("Execution time:", end - start)
