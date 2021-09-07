import sqlite3
con = sqlite3.connect ('9950.db')

cur = con.cursor()

pH =[('01', '-1.0000', '-1.0000', '-1.0000', 'Pass'),
     ('02', '+4.5000', '+4.5000', '+4.5000', 'Pass'),
     ('04', '+8.5000', '+8.5000', '+8.5000', 'Pass'),
     ('03', '+7.0000', '+7.0000', '+7.0000', 'Pass'),
     ('05', '+15.000', '+15.000', '+15.000', 'Pass')]

# create table
con.execute("CREATE TABLE pH (ID integer, Input real, Expected real, Actual real, Results text)")

# Insert a row of data
#cur.execute("INSERT INTO CH2 VALUES ('01', '-1.0000','-1.0000','-1.0000', 'Pass')")
#("INSERT INTO CH2 VALUES ('02', '+4.0000','+4.0000','+4.0000', 'Pass')")

con.executemany("insert into pH values (?, ?, ?, ?, ?)", pH)

for row in cur.execute('SELECT * FROM pH ORDER BY Input'):
    print(row)

    #cur.execute("SELECT * FROM pH")

    #print(cur.fetchall())
# Save (commit) the changes
con.commit()

print ('databse file is created')
con.close