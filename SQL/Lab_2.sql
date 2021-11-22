.header ON
.mode column

CREATE TABLE Item (
ItemName VARCHAR (30) NOT NULL,
ItemType CHAR(1) NOT NULL,
ItemColour VARCHAR(10),
PRIMARY KEY (ItemName));

CREATE TABLE Employee (
EmployeeNumber SMALLINT UNSIGNED NOT NULL ,
EmployeeName VARCHAR(10) NOT NULL ,
EmployeeSalary INTEGER UNSIGNED NOT NULL ,
DepartmentName VARCHAR(10) NOT NULL REFERENCES
Department,
BossNumber SMALLINT UNSIGNED NOT NULL REFERENCES
Employee,
PRIMARY KEY (EmployeeNumber));

CREATE TABLE Department (
DepartmentName VARCHAR(10) NOT NULL,
DepartmentFloor SMALLINT UNSIGNED NOT NULL,
DepartmentPhone SMALLINT UNSIGNED NOT NULL,
EmployeeNumber SMALLINT UNSIGNED NOT NULL REFERENCES
Employee,
PRIMARY KEY (DepartmentName));

CREATE TABLE Sale (
SaleNumber INTEGER UNSIGNED NOT NULL,
SaleQuantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
ItemName VARCHAR(30) NOT NULL REFERENCES Item,
DepartmentName VARCHAR(10) NOT NULL REFERENCES
Department,
PRIMARY KEY (SaleNumber));

CREATE TABLE Supplier (
SupplierNumber INTEGER UNSIGNED NOT NULL,
SupplierName VARCHAR(30) NOT NULL,
PRIMARY KEY (SupplierNumber));

CREATE TABLE Delivery (
DeliveryNumber INTEGER UNSIGNED NOT NULL,
DeliveryQuantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
ItemName VARCHAR(30) NOT NULL REFERENCES Item,
DepartmentName VARCHAR(10) NOT NULL REFERENCES
Department,
SupplierNumber INTEGER UNSIGNED NOT NULL REFERENCES
Supplier,
PRIMARY KEY (DeliveryNumber));

.separator "\t"
.import item.txt Item
.import delivery.txt Delivery
.import department.txt Department
.import sale.txt Sale
.import supplier.txt Supplier
.import employee.txt Employee

---- Q1.1 -----

.print Q1-1: List the green items of type 'C'
.print
SELECT ItemName FROM Item WHERE ItemColour = 'Green' AND ItemType = 'C';
.print

---- Q1.2 -----

.print Q1-2: What are the names of brown items sold by the Recreation Department?
.print
SELECT DISTINCT ItemName FROM ((Sale NATURAL JOIN Department) NATURAL JOIN Item) WHERE ItemColour = 'Brown' AND DepartmentName = 'Recreation';
.print 

---- Q1.3 -----

.print Q1-3: Which suppliers deliver compasses?
.print
SELECT DISTINCT Supplier.SupplierName From Delivery, Supplier WHERE Supplier.SupplierNumber = Delivery.SupplierNumber AND ItemName = 'Compass';
.print

---- Q1.4 -----

.print Q1-4: What items are delivered to the Books department?
.print
SELECT DISTINCT ItemName FROM Delivery WHERE DepartmentName = 'Books';
.print

---- Q1.5 -----

.print Q1-5: What are the numbers and names of those employees who earn more than their managers?

.print
SELECT DISTINCT staff.EmployeeNumber, staff.EmployeeName FROM Employee AS staff WHERE EmployeeSalary > (SELECT EmployeeSalary FROM Employee WHERE EmployeeNumber = staff.BossNumber);
.print

---- Q1.6 -----

.print Q1-6: What are the names of employees who are in the same department as their manager (as an employee), reporting the name of the employee, the department and the manager?
.print
SELECT DISTINCT staff.EmployeeName, staff.DepartmentName, manager.EmployeeName FROM Employee AS staff, Employee AS manager WHERE staff.DepartmentName = (SELECT DepartmentName FROM Employee WHERE EmployeeNumber = staff.BossNumber) AND manager.EmployeeName = (SELECT EmployeeName FROM Employee WHERE EmployeeNumber = staff.BossNumber);
.print

---- Q1.7 -----

.print Q1-7: List the departments having an average salary of over £25000.
.print
SELECT DISTINCT staff.DepartmentName FROM Employee as staff GROUP BY stafF.DepartmentName HAVING AVG(EmployeeSalary) > 25000;
.print

---- Q1.8 -----

.print Q1-8: List the name, salary and manager of the employees of the Marketing department who have a salary of over £25000.


.print
SELECT staff.EmployeeName, staff.EmployeeSalary, manager.EmployeeName FROM Employee AS staff, Employee AS manager WHERE staff.DepartmentName = 'Marketing' AND staff.EmployeeSalary > 25000  AND manager.EmployeeName = (SELECT EmployeeName FROM Employee WHERE EmployeeNumber = staff.BossNumber);
.print

---- Q1.9 -----
.print Q1-9: For each item, give its type, the departments that sell the item and the floor location of these departments.
.print
SELECT DISTINCT ItemName, ItemType, DepartmentName, DepartmentFloor From ((Sale NATURAL JOIN Item) NATURAL JOIN Department) WHERE Item.ItemName = sale.ItemName ORDER BY ItemName;
.print

---- Q1.10 -----

.print Q1-10:  What suppliers deliver a total quantity of items of types 'C' and 'N' that is altogether greater than 100?

.print
.print No Applicable Case
SELECT DISTINCT SupplierName FROM Delivery, Supplier, Item GROUP BY SupplierName HAVING SUM(DeliveryQuantity) > 100 AND ItemType = 'C' OR ItemType = 'N' ORDER BY SupplierName;
.print

---- Q2.1 -----

.print Q2-1: Find the suppliers that do not deliver compasses.
.print
SELECT DISTINCT SupplierName FROM Delivery NATURAL JOIN Supplier WHERE SupplierName NOT IN (SELECT DISTINCT SupplierName FROM Delivery NATURAL JOIN Supplier WHERE ItemName = 'Compass' ORDER BY SupplierName) ORDER BY SupplierName;
.print

---- Q2.2 -----

.print Q2-2: Find the name of the highest-paid employee in the Marketing Department
 
.print
SELECT EmployeeName FROM Employee GROUP BY EmployeeName HAVING EmployeeSalary = (SELECT MAX(EmployeeSalary) FROM Employee WHERE DepartmentName = 'Marketing');
.print

---- Q2.3 -----

.print Q2-3: Find the names of the suppliers that do not supply compasses or geo-positioning systems
.print
SELECT DISTINCT SupplierName FROM Delivery NATURAL JOIN Supplier WHERE SupplierName NOT IN (SELECT DISTINCT SupplierName FROM Delivery NATURAL JOIN Supplier WHERE ItemName = 'Compass' OR ItemName = 'Geo positioning system') ORDER BY SupplierName;
.print

---- Q2.4 -----

.print Q2-4: Find the number of employees with a salary under £10000
.print
SELECT COUNT(EmployeeName) FROM Employee WHERE EmployeeSalary < 10000;
.print

---- Q2.5 -----

.print Q2-5: List the departments on the second floor that contain more than one employee
.print

SELECT DepartmentName FROM Department WHERE DepartmentName IN (SELECT DepartmentName FROM Employee GROUP BY DepartmentName HAVING COUNT(EmployeeName) >1) AND DepartmentFloor = 2;


