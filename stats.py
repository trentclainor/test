# -*- coding: utf-8 -*-

import config
import sqlite3


def connect_db(db=config.DATABASE_URI):
    return sqlite3.connect(db)


def init_stat(c):
    r = c.execute("drop table if exists visits")
    if not r:
        return False
    r = c.execute("create table if not exists visits (date DATE NOT NULL, name varchar(255) not null, cnt INTEGER, PRIMARY KEY (date, name))")
    if not r:
        return False
    return True


def set_stat(c, date, name):
    r = c.execute("INSERT OR IGNORE INTO visits VALUES (:date, :name, :cnt)", {
        'date': date.strftime('%Y-%m-%d'),
        'name': name,
        'cnt': 0,
    })
    if not r:
        return False
    r = c.execute("UPDATE visits SET cnt = cnt + 1 WHERE name=:name", {
        'name': name,
    })
    if not r:
        return False
    return True


def get_stats(c):
    r = c.execute("select date, name, cnt from visits group by date, name")
    if not r:
        return False
    return r.fetchall()
