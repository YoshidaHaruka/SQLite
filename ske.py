#!/usr/bin/env python
#coding: utf-8
"""
  A sample program using sqlite3 and csv.
"""
import csv
import sqlite3

def main():
    """Main function."""
    
    # create database
    con = sqlite3.connect(":memory:")
    sql = """create table SKE48 (id integer,
                                 firstN varchar(10),
                                 lastN varchar(10),
                                 team varchar(10),
                                 birthday varchar(20),
                                 blood varchar(2),
                                 height integer,
                                 B integer,
                                 W integer,
                                 H integer,
                                 shoe real,
                                 generation integer
                                 );"""
    con.execute(sql)

    # data reading
    sql = "insert into SKE48 values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    [con.execute(sql, tuple(i)) for i in csv.reader(file("ske.csv", "r"))]

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
    # sql = "select blood, count(height), avg(height) from SKE48 group by blood"
    # sql = "select team, avg(B) from SKE48 group by team having avg(B) > 78"
    sql = "select firstN, lastN, date('now') - date(birthday) as date from SKE48"

    for row in con.execute (sql):
        print row

    # data writing
    writer = csv.writer(file("output.csv", "w"))
    [writer.writerow(list(row)) for row in con.execute(sql)]

    # close database
    con.close()

if __name__ == "__main__":
    main()
