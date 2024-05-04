import mysql.connector


def main():
    connection = create_connection()
    student_cursor = connection.cursor()
    create_table(connection, student_cursor)  # Make sure student_cursor is defined before it's used
    insert_student(connection, student_cursor)
    select_all_students(student_cursor)
    
    student_cursor.close()
    connection.close()
def create_connection():
    
        connection = mysql.connector.connect(
            user="",
            password="",
            host="localhost",
            database="University"
        )
        print("Connected to MySQL database")
        return connection
   


def create_table(connection,student_cursor):
    print("Creating table...")
    
    student_create = ('CREATE TABLE Student ('
                      'Id INT PRIMARY KEY, '
                      'Name VARCHAR(50), '
                      'Email VARCHAR(100),'
                      'Age INT,'
                      'Year VARCHAR(30) )')
    
    student_cursor.execute(student_create)
    connection.commit()

   
    
    
   

def insert_student(connection, student_cursor):
    StudentInsert = "INSERT INTO Student (Id, Name, Email, Age, Year) VALUES (%s, %s, %s, %s, %s)"
    rows = (30, "Air India", "gh@yahoo.net", 23, "Freshman")
    rows2 = (31, "Air Indiaa", "gh@yahoo.nets", 23, "Freshman")
    student_cursor.execute(StudentInsert, rows)
    student_cursor.execute(StudentInsert, rows2)
    connection.commit()

     
def select_all_students(student_cursor):
     student_cursor.execute("SELECT * FROM Student")
     students = student_cursor.fetchall()
     print("All Students:")
     for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Email:", student[2])
        print("Age:", student[3])
        print("Year:", student[4])
        print()



if __name__ == "__main__": main()


