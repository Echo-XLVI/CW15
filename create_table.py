def create_course():
    return (f'CREATE TABLE Courses (course_id INT PRIMARY KEY ,'
            f'title VARCHAR(100),credits  INT ,is_prerequisite Bool,'
            f'prerequisite_of_id  BIGINT ,instructor_id BIGINT,'
            f'is_deleted BOOLEAN DEFAULT  false,'
            f'FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id));')

def create_instructor():
    return(f'CREATE TABLE Instructors ( instructor_id INT PRIMARY,'
           f'name VARCHAR(50),'
           f'specialization  VARCHAR(100),'
           f'department_id BIGINT,'
           f'is_deleted BOOLEAN DEFAULT true,'
           f'FOREIGN KEY (department_id) REFERENCES Department(department_id));')