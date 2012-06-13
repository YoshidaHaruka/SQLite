#!/usr/bin/env python
#coding: utf-8
"""
  A sample program using sqlite3 and csv.
"""
import csv
import sqlite3
import cPickle as pickle
from datetime import date
from dateutil.relativedelta import relativedelta


class Person(object):
    """The person class."""
    def __init__(self, id, name, team):
        """Initialize function.

        Keyword arguments:
        id       -- string (like '12')
        name     -- string (like 'Rena Matsui')
        team     -- string (like 'S')

        """
        self.id = id
        self.name = name
        self.name_l, self.name_f = name.split(' ')
        self.team = team
        
    def __conform__(self, protocol):
        """Returns value for SQLite3."""
        if protocol is sqlite3.PrepareProtocol:
            return "%d;%s;%s" % (self.id, self.name, self.team)

    def __str__(self):
        '''Variables display function.'''
        retval = self.name_l + ' ' + self.name_f + ' (' + self.team + ')'
        return retval

def main():
    """Main function."""

    # read data from csv file
    inputData = csv.reader(file("ske.csv", "r"))

    # create database with auto-commit mode
    con = sqlite3.connect(":memory:", isolation_level = None)
    with con:
        sql = """create table if not exists SKE48 (
                    id integer,
                    firstN text,
                    lastN text,
                    team text,
                    birthday text,
                    blood varchar(2),
                    height integer,
                    B integer,
                    W integer,
                    H integer,
                    shoe real,
                    generation integer,
                    object blob);"""
        con.execute(sql)

        # insert data to database
        pickleList = []
        sql = "insert into SKE48 values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        for i in inputData:
            obj = Person(int(i[0]), i[2] + ' ' + i[1], i[3])
            i.append(obj)
            con.execute(sql, tuple(i))
            pickleList.append(obj)

        # sql = "select * from SKE48"
        # sql = "select firstN, lastN from SKE48"
        # sql = "select * from SKE48 where blood = 'O'"
        # sql = "select firstN, lastN, height from SKE48 where height < 160"
        # sql = "select * from SKE48 where blood = 'O' OR blood = 'A'"
        # sql = "select * from SKE48 where height between 150 AND 160"
        # sql = "select * from SKE48 where firstN like 'A%i'"
        # sql = "select * from SKE48 where firstN like 'A%i' order by H"
        # sql = "select * from SKE48 where firstN like 'A%i' order by H ASC"
        # sql = "select * from SKE48 where firstN like 'A%i' order by H DESC"
        # sql = "select blood,count(height),avg(height) from SKE48 group by blood"
        # sql = "select team, avg(B) from SKE48 group by team having avg(B) > 78"
        # sql = "select firstN, date('now') - date(birthday) as date from SKE48"
        sql = "select object from SKE48"

        for row in con.execute (sql):
            print row

        # write selected data to csv file
        writer = csv.writer(file("output.csv", "w"))
        for row in con.execute(sql):
            writer.writerow(list(row))

        # serialize data to pickle file
        pickle.dump(pickleList, open('output.dmp', 'w'))

        # close database (con is automatically closed by using 'with statement')
        # con.close()


if __name__ == "__main__":
    main()
