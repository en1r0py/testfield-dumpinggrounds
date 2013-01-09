#!/usr/bin/python
import cgi
import sqlite3


def run_my_query(db, query):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        data = cursor.fetchall()
        print "Query executed."

    except Exception as e:
        print "There was an error executing the query."

    conn.commit()
    conn.close()

    print "<table border=\"1\">"
    for each_r in data:
        print "<tr>"
        for each_c in each_r:
            print "<td>", each_c, "</td>"
        print "</tr>"
    print "</table>"


form_data = cgi.FieldStorage()

print "Content-type: text/html\n\n"
run_my_query(form_data['db'].value, form_data['query'].value)


