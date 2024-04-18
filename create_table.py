def create_course():
    return (f'CREATE TABLE Courses (course_id INT PRIMARY KEY NOT NULL ,'
            f'title VARCHAR(100) NOT NULL,credits  INT NOT NULL ,is_prerequisite Bool NOT NULL,'
            f'prerequisite_of_id  BIGINT ,instructor_id BIGINT NOT NULL,'
            f'is_deleted BOOLEAN DEFAULT  false,'
            f'FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id));')

def create_instructor():
    return(f'CREATE TABLE Instructors ( instructor_id INT PRIMARY NOT NULL,'
           f'name VARCHAR(50) NOT NULL,'
           f'specialization  VARCHAR(100) NOT NULL,'
           f'department_id BIGINT NOT NULL,'
           f'is_deleted BOOLEAN DEFAULT true,'
           f'FOREIGN KEY (department_id) REFERENCES Department(department_id));')