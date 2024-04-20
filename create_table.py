from  connection import Connection
def create_table():
        conn=Connection.connect('localhost','postgres',5060,'TY@%57rk','universitydb')
        
        query="""create table student(
                student_id int constraint PK_Student_student_id primary key,
                name varchar(50) not null,
                date_of_birth date not null,
                is_deleted bool);
                
                create table department(
                department_id int constraint PK_Department_department_id primary key,
                name varchar(100) not null,
                is_deleted bool);
                
                CREATE TABLE Instructors ( instructor_id INT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                specialization  VARCHAR(100) NOT NULL,
                department_id BIGINT NOT NULL,
                is_deleted BOOLEAN DEFAULT true,
                FOREIGN KEY (department_id) REFERENCES Department(department_id));
        
                CREATE TABLE Courses (course_id INT PRIMARY KEY,
                title VARCHAR(100) NOT NULL,credits  INT NOT NULL ,is_prerequisite Bool NOT NULL,
                prerequisite_of_id  BIGINT ,instructor_id BIGINT NOT NULL,
                is_deleted BOOLEAN DEFAULT  false,
                FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id));
                
                create table StudentRegistration
                (
                registration_id int primary key,
                student_id int not null ,
                course_id int not null ,
                registration_date date not null ,
                is_deleted boolean ,
                foreign key(student_id) references Student(student_id) ,
                foreign key(course_id) references Courses(course_id)
                );"""
        
        Connection.insert_query(query,conn)