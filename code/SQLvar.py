import sqlite3

def deletef(con,name):
	with con:
		cursor=con.cursor()
		sql=f"delete from hist where name='{name}'"
		cursor.execute(sql)
		con.commit()

def create_connection(db_name):
	connection = sqlite3.connect(db_name)
	return connection
    
def write_data_to_db(con, data):
	query='insert into hist values(?,?)'
	with con as conn:
		cur=conn.cursor()
		try:
			if get_from_db(conn,data[0])==[]:
				cur.execute(query, data)
			else:
				pass
		except:
			pass
def get_from_db(connection, query):
	sql_some=f"SELECT * FROM hist WHERE name LIKE '%{query}%'"
	cursor=connection.cursor()
	cursor.execute(sql_some)
	return cursor.fetchall()
def update(con,fro,to):
	with con:
		query=f"UPDATE hist SET definition ='{to}' WHERE name= '{fro}'"
		cursor=con.cursor()
		cursor.execute(query)
		con.commit()
