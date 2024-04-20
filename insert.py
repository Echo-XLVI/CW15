from connection import Connection

def insert_rows():
        conn=Connection.connect('localhost','postgres',5060,'TY@%57rk','universitydb')

        query="""insert into student values 
                (1,'reza','2001-08-06'),
                (2,'zahra','2000-11-09'),
                (3,'mehrzad','2005-05-20');

                insert into department values
                (1,'math'),
                (2,'physic'),
                (3,'art') ;

                INSERT INTO Instructors VALUES (1,'ali','math',1,false),
                                              (2,'reza','physics',2,false),
                                              (3,'mohammad','math',1,false);

                INSERT INTO Courses VALUES (1,'mathmathic',2,false,null,1,false),
                                           (2,'mathmathic2',2,true,1,2,false),
                                           (3,'physics',2,false,null,3,false);

                INSERT into StudentRegistration VALUES(1,2,1,'2024-4-18'),
                                                      (2,3,3,'2024-3-18'),
                                                      (3,2,2,'2024-2-18');"""

        Connection.insert_query(query,conn)