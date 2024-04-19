# from connection import Connection

def show(conn, table_name:str):
    # conn=Connection.connect('localhost','postgres',5648,'1380ACreZA46','universitydb')
    cursor = conn.cursor()
    cursor.execute(f"select * from {table_name}")
    rows = cursor.fetchall()
    conn.commit()
    for row in rows:
        print(row)  

def delete(conn, table_name:str, id:str):
    # conn=Connection.connect('localhost','postgres',5648,'1380ACreZA46','universitydb')
    cursor = conn.cursor()
    cursor.execute(f"update {table_name} set is_deleted=True where {table_name}_id={id}")
    conn.commit()

def update(conn, table_name:str, column:str, new_value:str, id:str):
    # conn=Connection.connect('localhost','postgres',5648,'1380ACreZA46','universitydb')
    cursor = conn.cursor()
    cursor.execute(f"update {table_name} set {column}={new_value} where {table_name}_id={id}")
    conn.commit()

def insert(conn, table_name:str, *args):
    cursor = conn.cursor()
    cursor.execute(f"insert into {table_name} values({','.join(args)})")
    conn.commit()