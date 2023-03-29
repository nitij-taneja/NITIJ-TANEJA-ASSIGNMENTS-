'''Q1. What is a database? Differentiate between SQL and NoSQL databases.

A database is an organized collection of structured or unstructured data that can be accessed, managed, and updated in a systematical
way. Databases are used to store and manage data for various applications, ranging from small-scale personal applications to large 
scale enterprise systems.

SQL and NoSQL are two different types of databases that differ in their structure, data model, and query language:

SQL databases: SQL stands for Structured Query Language, which is a language used to manage and manipulate relational databases.
SQL databases store data in a structured manner, using tables with predefined columns and data types. Each table has a unique key,
and the data is stored in rows that correspond to records in the table. SQL databases are highly structured and provide a high
level of data integrity and consistency. Some examples of SQL databases include MySQL, Oracle, and PostgreSQL.

NoSQL databases: NoSQL stands for "not only SQL", which means that NoSQL databases are not limited to SQL query language. NoSQL
databases store data in a non-structured or semi-structured manner, using documents, key-value pairs, or graphs. NoSQL databases
are highly scalable and can handle large volumes of data with ease. NoSQL databases provide greater flexibility and agility than 
SQL databases, but at the cost of reduced data integrity and consistency. Some examples of NoSQL databases include MongoDB, 
Cassandra, and Redis.

In summary, SQL databases are highly structured, provide high data integrity and consistency, and use SQL as a query language.
NoSQL databases are highly scalable, provide greater flexibility and agility, and use non-structured or semi-structured data 
models.



Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

DDL stands for Data Definition Language, which is a set of SQL commands used to create, modify, and delete database objects such
as tables, indexes, and constraints. DDL is used to define the structure of a database and its objects.

The following are some of the commonly used DDL commands and their usage:

CREATE: The CREATE command is used to create a new database object such as a table, index, or view. For example, to create a new 
table named "Studnets1" with columns for roll number, name we can use the following SQL statement: 
CREATE DATABASE NITIJ;
CREATE TABLE if not exists NITIJ.Student1(ROLL_NO INT, NAME VARCHAR(50));
CREATE TABLE if not exists NITIJ.Student2(ROLL_NO INT, NAME VARCHAR(50));

DROP: The DROP command is used to delete an existing database object such as a table, index, or view. For example, to delete the 
"Studnet1" table created above, we can use the following SQL statement: 
DROP TABLE Student1;

ALTER: The ALTER command is used to modify the structure of an existing database object such as a table or index. For example, to
add a new column "Branch" to the "Student2" table created above, we can use the following SQL statement: 
ALTER TABLE Student2
ADD BRANCH varchar(30);

TRUNCATE: The TRUNCATE command is used to delete all data from a table without deleting the table itself. For example, to delete 
all data from the "Student2" table created above, we can use the following SQL statement:
TRUNCATE TABLE Student2;


Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

DML stands for Data Manipulation Language, which is a set of SQL commands used to insert, update, and delete data in a database 
table. DML commands are used to modify the data stored in a table.

The following are some of the commonly used DML commands and their usage:

INSERT: The INSERT command is used to insert new data into a table. For example, to insert a new row into the "Student2" table with 
ROLL NO 1, name "John", and BRANCH "DATA SCIENCE", we can use the following SQL statement: 
INSERT INTO NITIJ.Student2 value(1, 'John', 'Data Science');

UPDATE: The UPDATE command is used to update existing data in a table. For example, to update the Branch of the studnet with 
roll number 1 to "cyber security", we can use the following SQL statement: 
UPDATE Student2
SET BRANCH='Cyber Security'
where ROLL_NO=1;

DELETE: The DELETE command is used to delete data from a table. For example, to delete the student with roll no 1 from the student2 
table, we can use the following SQL statement:
DELETE FROM Student2 
where ROLL_NO=1;


Q4. What is DQL? Explain SELECT with an example.

DQL stands for Data Query Language, which is a set of SQL commands used to retrieve data from a database table. DQL commands are 
used to query the data stored in a table.

The most commonly used DQL command is SELECT. The SELECT command is used to retrieve data from one or more tables. Here's an 
example of how to use the SELECT command:
SELECT * FROM NITIJ.Student2;


Q5. Explain Primary Key and Foreign Key.

A primary key is a unique identifier for each row in a table. It is a column or combination of columns that uniquely identifies 
each record in a table. The primary key constraint ensures that the values in the primary key column(s) are unique and not null. 
For example, in a "Studnet2" table, the "roll_no" column can be the primary key if each student has a unique roll number.

A foreign key is a column or combination of columns in one table that refers to the primary key of another table. It establishes a 
relationship between two tables, where the values in the foreign key column(s) of one table match the values in the primary key 
column(s) of another table. For example, in a "marks" table, the "roll_number" column can be a foreign key that refers to the 
"roll_no" column of the "student2" table, indicating which user placed each order.


Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.'''
import mysql.connector
mydb=mysql.connector.connect(
  host = "localhost",
  user ="abc",
  password = "password"
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for x in mycursor:
  print(x)


'''
The cursor() method in Python is used to create a cursor object, which allows us to execute SQL commands on the database. The 
cursor object provides methods to execute SQL commands, fetch data from the database, and handle transactions.

The execute() method is used to execute SQL commands on the database using the cursor object. It takes an SQL query as its 
argument and returns the result of the query. For example, to execute a SELECT query on a MySQL database using the cursor object.


Q7. Give the order of execution of SQL clauses in an SQL query.

SELECT: Specifies the columns to be retrieved from the database table. 
FROM: Specifies the table from which to retrieve the data. 
JOIN: Combines multiple tables based on a common column. 
WHERE: Filters the data based on certain conditions. GROUP 
BY: Groups the data based on one or more
'''
