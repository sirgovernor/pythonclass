import sqlite3
conn=sqlite3.connect('mitmidmornig.db')
print("open database successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (1,'Erick',30,'eMobilis','male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (2,'Miri',22,'Kiambu','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (3,'Vincent',60,'Nairobi','male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (4,'Victoria',28,'Mombasa','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (5,'Vitalis',25,'Kisumu','male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)values (6,'nick',50,'kanga','male')")

conn.commit()
print("recodes added successfully")
conn.close()