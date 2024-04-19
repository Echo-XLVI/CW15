import psycopg2

class Connection:

    @staticmethod
    def connect(db_host:str, db_user:str, db_port:int, db_password:str, db_database:str) -> object:
        return psycopg2.connect(user=db_user,port=db_port,password=db_password,host=db_host,database=db_database)
    
    @staticmethod
    def insert_query(query:str,connection:object) -> list:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()     