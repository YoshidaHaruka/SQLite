#!/usr/bin/env python
#coding: utf-8
"""
  Table joing example using sqlite3.

  __ http://himagine.s20.xrea.com/access/fulljoin.html
"""
import sqlite3

tableA = [(1, 100), (3, 300), (4, 400), (7, 700), (8, 800)]
tableB = [(1, 1000), (2, 2000), (4, 4000), (5, 5000), (6, 6000), (8, 8000)]
namesA = [(1, "Ando"), (3, "Inoue"), (4, "Ueda"), (7, "Endo"), (8, "Ono")]

if __name__ == "__main__":
    """Main function."""

    # create database with aut-commit mode
    con = sqlite3.connect(":memory:", isolation_level = None)
    with con:
        sql = """create table if not exists nameA (
                    customID integer,
                    value text);"""
        con.execute(sql)
        [con.execute("insert into nameA values (?, ?)", i) for i in namesA]

        sql = """create table if not exists shopA (
                    customID integer,
                    value integer);"""
        con.execute(sql)
        [con.execute("insert into shopA values (?, ?)", i) for i in tableA]

        sql = """create table if not exists shopB (
                    customID integer,
                    value integer);"""
        con.execute(sql)
        [con.execute("insert into shopB values (?, ?)", i) for i in tableB]

        # sql = "select * from shopA"
        # for row in con.execute(sql):
        #     print row

        # sql = "select b.value from shopB b"
        # for row in con.execute(sql):
        #     print row

        # 結合 (これも内部結合ぽい？)
        sql = """SELECT a.customID, n.value FROM shopA a, nameA n
                 WHERE a.customID = n.customID
              """
        print "JOIN"
        for row in con.execute(sql):
            print row

        # 内部結合 (共通しないユーザーは出てこない)
        sql = """SELECT a.customID, a.value + b.value FROM shopA a
                 INNER JOIN shopB b ON a.customID=b.customID
              """
        print "INNER JOIN"
        for row in con.execute(sql):
            print row

        # 左外部結合
        sql = """SELECT a.customID, a.value + b.value FROM shopA a
                 LEFT OUTER JOIN shopB b ON a.customID=b.customID
              """
        print "LEFT OUTER JOIN"
        for row in con.execute(sql):
            print row

        # 右外部結合、と全外部結合は sqlite3 では support されてないぽ。
        # まぁでも RIGHT OUTER JOIN と FULL OUTER JOIN をすれば良いぽ。
