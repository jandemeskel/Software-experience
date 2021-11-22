import sqlite3

# DBOperation class to manage all data into the database. 

class DBOperations:

  #------ SQL FUNCTIONS ------#

  sql_create_table = ("CREATE TABLE EmployeeUoB (ID SMALLINT UNSIGNED PRIMARY KEY, Title VARCHAR(20), Forename VARCHAR(20), Surname VARCHAR(20), Email VARCHAR(100), Salary SMALLINT UNISNGED)")

  sql_insert = "INSERT INTO EmployeeUoB VALUES(?,?,?,?,?,?) "
  sql_select_all = "SELECT * from EmployeeUoB"
  sql_search = "SELECT * from EmployeeUoB where ID = ?"
  sql_update_title = "UPDATE EmployeeUoB SET Title = ? WHERE ID = ?;"
  sql_update_forename = "UPDATE EmployeeUoB SET Forename = ? WHERE ID = ?;"
  sql_update_surname = "UPDATE EmployeeUoB SET Surname = ? WHERE ID = ?;"
  sql_update_email = "UPDATE EmployeeUoB SET Email = ? WHERE ID = ?;"
  sql_update_salary = "UPDATE EmployeeUoB SET Salary = ? WHERE ID = ?;"
  sql_delete_data = "DELETE FROM EmployeeUoB WHERE ID = ?;"
  sql_sum_salary = "SELECT SUM(salary) FROM EmployeeUoB;"

 #------ Initializing function ------#

  def __init__(self):
    try:
      self.conn = sqlite3.connect("EmployeeData.db")
      self.cur = self.conn.cursor()
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

 # Creating a connection between Python and SQL Database #

  def get_connection(self):
    self.conn = sqlite3.connect("EmployeeData.db")
    self.cur = self.conn.cursor()

  # OPTION 1: Creating a table within the database, given it doesnt exist already #

  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  # OPTION 2: Inserting Employee data from input values #

  def insert_data(self):
    try:
      self.get_connection()

      emp = Employee()
      emp.set_employee_id(int(input("Enter Employee ID: ")))
      emp.set_email(str(input("Enter Employee Email: ")))
      emp.set_employee_title(str(input("Enter Employee Title: ")))
      emp.set_forename(str(input("Enter Employee Forename: ")))
      emp.set_surname(str(input("Enter Employee Surname: ")))
      emp.set_salary(str(input("Enter Employee Salary: ")))
      
      

      self.cur.execute(self.sql_insert,tuple(str(emp).split("\n")))

      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # OPTION 3: Ouput all employee data currently in the database #

  def select_all(self):
    try:
      self.get_connection()
      results =  self.cur.execute(self.sql_select_all)
      
      for data in results:
        print(data)

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # OPTION 4: Output a specific employee's via inputting the employee's ID #

  def search_data(self):
    try:
      self.get_connection()
      employeeID = int(input("Enter Employee ID: "))
      self.cur.execute(self.sql_search,tuple(str(employeeID)))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Employee ID: " + str(detail))
          elif index == 1:
            print("Employee Title: " + detail)
          elif index == 2:
            print("Employee Name: " + detail)
          elif index == 3:
            print("Employee Surname: " + detail)
          elif index == 4:
            print("Employee Email: " + detail)
          else:
            print("Salary: "+ str(detail))
      else:
        print ("No Record")
            
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # OPTION 5: Update a particular record of a given row in employee data given the employee ID #
  def update_data(self):
    try:
      self.get_connection()

      employeeID = int(input("Enter ID of the Employee data to be updated: "))

      x = str(input("would you like to change the Forename, Surname, Title, Email or Salary?"))
      
      if x == "title" or x == "Title":
        y = str(input("What would you like to change the title to: "))
        self.cur.execute(self.sql_update_title, (y, employeeID))

      elif x == "forename" or  x == "Forename":
        y = str(input("What would you like to change the Forename to: "))
        self.cur.execute(self.sql_update_forename, (y, employeeID))
      
      elif x == "surname" or x == "Surname":
        y = str(input("What would you like to change the Surname to: "))
        self.cur.execute(self.sql_update_surname, (y, employeeID))

      elif x == "email" or x == "Email":
        y = str(input("What would you like to change the email to: "))
        self.cur.execute(self.sql_update_email, (y, employeeID))
      
      elif x == "salary" or x == "Salary":
        y = int(input("What would you like to change the Salary to: "))
        self.cur.execute(self.sql_update_salary, (y, employeeID))
      
      else:
        print("Invalid input please enter fieldname you would like to update, the following are valid inputs:'Title', 'Forename', 'Surname', 'Email', or 'Salary' ")
        

      self.conn.commit()

      if self.cur.rowcount != 0:
         print('Record successfully updated')
      else:
        print('ID does not exist')


    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  # OPTION 6: Delete all employee data given employee ID #

  def delete_data(self):
    try:
      self.get_connection()

      employeeID = int(input("Enter ID of employee data to be deleted: "))
      self.cur.execute(self.sql_delete_data, str(employeeID))


      self.conn.commit()

      if self.cur.rowcount != 0:
         print('Record successfully deleted')
      else:
        print('ID does not exist')

    except Exception as e:
      print(e)
    finally: 
      self.conn.close()
  
  # OPTION 7 (EXTRA FUNCTIONALITY): Return the total funding required to satisfy employee payroll value #

  def sum_salary(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_sum_salary)
      print("£",float(self.cur.fetchone()[0]))
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

# Employee class to assign and retrieve data within the table. 

class Employee:
  def __init__(self):
    self.employeeID = 0
    self.empTitle = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0.0

  def set_employee_id(self, employeeID):
    self.employeeID = employeeID

  def set_employee_title(self, empTitle):
    self.empTitle = empTitle

  def set_forename(self,forename):
   self.forename = forename
  
  def set_surname(self,surname):
    self.surname = surname

  def set_email(self,email):
    self.email = email
  
  def set_salary(self,salary):
    self.salary = salary
  
  def get_employee_id(self):
    return self.employeeId

  def get_employee_title(self):
    return self.empTitle
  
  def get_forename(self):
    return self.forename
  
  def get_surname(self):
    return self.surname
  
  def get_email(self):
    return self.email
  
  def get_salary(self):
    return self.salary

  def __str__(self):
    return str(self.employeeID)+"\n"+self.empTitle+"\n"+ self.forename+"\n"+self.surname+"\n"+self.email+"\n"+str(self.salary)


# The main function used to parse arguments and implement user interation on the console. 
  
while True:
  print ("\n Menu:")
  print ("**********")
  print (" 1. Create table EmployeeUoB")
  print (" 2. Insert data into EmployeeUoB")
  print (" 3. Select all data into EmployeeUoB")
  print (" 4. Search an employee")
  print (" 5. Update data some records")
  print (" 6. Delete data some records")
  print (" 7. Total payroll value ")
  print (" 8. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    db_ops.sum_salary()
  elif __choose_menu == 8:
    exit(0)
  else:
    print ("Invalid Choice")



