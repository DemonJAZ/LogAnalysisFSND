#!/usr/bin/env python2.7
import psycopg2


def connect():
    return psycopg2.connect("dbname=news")


def top_Article_View():
    db = connect()
    c = db.cursor()
    c.execute("SELECT title,view FROM top_gossing ORDER BY view DESC LIMIT 3")
    tops = c.fetchall()
    db.close()
    for (title, count) in tops:
        print("   {} - {} views".format(title, count))


def top_authors():
    db = connect()
    c = db.cursor()
    c.execute("SELECT authors.name,sum(top_gossing.view) as view " +
              "from top_gossing join authors on top_gossing.author " +
              "= authors.id GROUP BY authors.name ORDER BY view DESC;")
    tops = c.fetchall()
    db.close()
    for (author, count) in tops:
        print("   {} - {} views".format(author, count))


def errors_found():
    db = connect()
    c = db.cursor()
    c.execute("select time ,(total_errors/total_views)*100 as errors " +
              "from daily_requests order by errors desc;")
    total = c.fetchone()
    db.close()
    print("   {} - {} %".format(str(total[0]), round(float(total[1]), 2)))


print "Top 3 Articles:"
top_Article_View()
print "\n\n\n"
print "Top Authors:"
top_authors()
print "\n\n\n"
print "Percentage of errors on 01-07-2016:"
errors_found()
