import mysql.connector

try:

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='testdb_python',
    port=3306
    )
    # print(mydb)
except Exception as e:
    print(e)





cur = mydb.cursor()



class Employee:
    employees=[]
    id=0
    def __init__(self,First_name,Last_name,Age,Department,Salary):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Age=Age
        self.Department=Department
        self.Salary=Salary
        Employee.id+=1
        self.id=Employee.id
        try:
            cur.execute(f"INSERT INTO employees (FirstName, LastName, Age, department, salary) VALUES ('{First_name}', '{Last_name}', {Age}, '{Department}', {Salary})")
            mydb.commit()
            Employee.employees.append(self)
        except Exception as e:  
            print(e) 

    def transfer(self,department):
        self.department=department
        try:
            cur.execute(f"Update employees set department='{department}' where FirstName='{self.First_name}' and LastName='{self.Last_name}'")
            mydb.commit()
        except Exception as e:  
            print(e) 
    
    def fire(self):
        Employee.employees.remove(self)
        try:
            cur.execute(f"delete from employees  where FirstName='{self.First_name}' and LastName='{self.Last_name}' ")
            mydb.commit()
        except Exception as e:  
            print(e) 
    
    def show(self):
        try:
            cur.execute(f"select * from employees where FirstName='{self.First_name}' and LastName='{self.Last_name}'")
            rows = cur.fetchone()
            print(rows[0], rows[1], rows[2],rows[3],rows[4])
            mydb.commit()
        except Exception as e:  
            print(e) 
    
    @classmethod
    def List_employees(cls):
        try:
            cur.execute(f"select * from employees")
            rows = cur.fetchall()
            for row in rows:
                print(row[0], row[1], row[2],row[3],row[4])
            mydb.commit() 
        except Exception as e:  
            print(e) 


while True:
    query_action= input(""" welcome to our company
            to add employee type 'add_emp'
            to show all employees 'show_all_employees'
            to exit press Q
            """)
    if query_action=='add_emp':
        manager=input("If you are manager press “m” || if you are employee press ‘e’")
        if manager=="m":
            first_name=input('please enter the first name: ')
            last_name=input('please enter the last name: ')
            age=int(input('please enter the age: '))
            department=input('please enter the department: ')
            salary=int(input('please enter the salary: '))
            emp=Employee(first_name,last_name,age,department,salary)
        else:
            print("you can not add employee")

            
    if query_action=='show_all_employees':
        Employee.List_employees()
    
    if query_action=='q':
        break