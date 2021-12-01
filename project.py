# -----------------------------------------------------------
# MYSQL python databse project
#
# Name:
# Date:
# Description: mysql.connector helps to connect with mysql server
#              and with help of that we created a database and reading out data.
# -----------------------------------------------------------
import mysql.connector

# Create brand new database 
def createDatabase():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE mydatabase");

# main program loop 
# it will ask for options and perforn following tasks
def loop():
  x=0
  while(x!="5"):
    print("Enter the Following options to get details")
    print("1. GET all Customers")
    print("2. GET all Publishers")
    print("3. GET all Books")
    print("4. GET Report on Order")
    print("5. Quit")
    # asking user to choose option 
    x = input("Enter any following options: ")
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234",
      database="mydatabase"
      )
    mycursor=mydb.cursor()
    if(x=="1"):
      # fetch total data of all Customer
      mycursor.execute("Select * from Customers");
      res=mycursor.fetchall()
      for x in res:
        print(x)
    elif (x=="2"):
      # fetch total data of all Publishers
      mycursor.execute("Select * from Publishers");
      res=mycursor.fetchall()
      for x in res:
        print(x)
    elif(x=="3"):
      # fetch total data of all Books
      mycursor.execute("Select * from Books");
      res=mycursor.fetchall()
      for x in res:
        print(x)
    elif(x=="4"):
      # asking user to provide ordernum to get details
      num=input("Enter Ordernum to get details: ")
      selectcustid = """SELECT custID FROM Orders
                      WHERE ordernum=%s """
      mycursor.execute(selectcustid,(num,))
      # fetchone used for fetching only one row from the table
      custID = mycursor.fetchone()
      customerdetails = """SELECT Name, Address FROM Customers
                    WHERE custID=%s"""
      mycursor.execute(customerdetails,custID)
      customerdetailresult = mycursor.fetchone()
      print("ORDER DETAILS OF ORDERNUMBER "+num+" :")
      print("CustonerName: "+customerdetailresult[0]+", Address: "+customerdetailresult[1]);
      getisbnnumbers="""SELECT isbn FROM OrderList 
                      WHERE ordernum=%s"""
      mycursor.execute(getisbnnumbers,(num,))
      # fetchall used for fetching all data as list of tuples
      isbnnumbers=mycursor.fetchall()
      for x in isbnnumbers:
        getbookdetails="""SELECT title, author, PublisherID from Books
                        WHERE isbn=%s"""
        mycursor.execute(getbookdetails,x)
        bookdetail=mycursor.fetchone()
        getpublisherName ="""SELECT Name FROM Publishers
                            WHERE PublisherID=%s"""
        mycursor.execute(getpublisherName,(bookdetail[2],))
        publisherName = mycursor.fetchone()
        print("Book Title :"+bookdetail[0]+", Author: "+bookdetail[1]+", PublisherID: "+((str(bookdetail[2])))+", Publisher Name: "+publisherName[0])
    elif(x=="5"):
      exit
    else:
      print("Select valid option")

# at first tring to connect with the existing database 
# if not present then create new database inside expect block
try:
  # Connecting with existing database
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
  )
  mycursor=mydb.cursor()
  # start main programme loop 
  loop()
except mysql.connector.Error:
  # creteing new database due to exception throw
  createDatabase()
  # connecting to the brand new database created
  print("Creating database and connect")
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
  )
  # pointing cursor to execute mysql opertaions 
  mycursor=mydb.cursor()
  # defining customer table structure
  createCustomerTable = """CREATE TABLE Customers
                    ( custID int,
                      Name VARCHAR(255),
                      Address VARCHAR(255),
                      Age int,
                      Income double,
                      LoginId VARCHAR(255),
                      Password VARCHAR(255)
                    );"""
  # insertion command for Customer table
  insertCustomers = """INSERT INTO Customers
                    ( custID ,Name,Address,Age,Income,LoginId,Password) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
  customerValues = [
    (1, 'Kate Simmons', '555 Pine Street, Louisville, KY 40252', 20, 15000.00, 'katie', 'katie12'),
    (2, 'Dan Smith', '3333 Market St Apt 7, Frederick, MD 20101', 45, 60000.00, 'danny68', 'dannyboy'),
    (3, 'John Doe', '92 Unknown Ave, Big Town, IN 51211', 50, 45000.00, 'anonymous', 'mystery'),
    (4, 'Jane Doe', '92 Unknown Ave, Big Town, IN 51211', 48, 48000.00, 'ladyanon', 'guesswho'),
    (5, 'Robert Chirwa', '222 Clearwater Blvd, London, KS 71414', 98, 20000, 'robert', 'oldman'),
    (6, 'Juan Gomez', '87 Mickey Mouse Rd, Orlando, FL 32222', 33, 102000.00, 'john', 'disney'),
    (7, 'Bugs Bunny', '714 Warner, Hollywood, CA 90111', 62, 75000.00, 'bugs', 'rabbit'),
    (8, 'Frodo Buggins', '1 Foods Ave, Middle Earth, ND 76543', 32, 10000.00, 'frodo', 'ringbearer'),
    (9, 'Andre Ritchie', '444 Preston, Louisville, KY 40211', 22, 25000.00, 'andre', 'youngman'),
    (10, 'Duffy Duck', '14 TNT Road, Acme, CA 90152', 27, 32000.00, 'duffy', 'ladybird'),
    (11, 'Kaka', '555 Pine Street, Louisville, KY 40252', 18, 17000.00, 'kaka', 'soccerboy'),
    (12, 'Stella Torvards', '111 Broadway, Cincinnati, OH 50428', 42, 50000.00, 'sissy', 'theboss'),
    (13, 'Tricia Codd', '46 Relational Algebra, Database City, MA 01234', 70, 125000.00, 'codd', 'daughter'),
    (14, 'James Yourdon', '678 System Design St, San Francisco, CA 90404', 55, 95000.00, 'yourdon', 'richman')
      ]
  # defining Publishers table structure
  createPublishersTable = """CREATE TABLE Publishers
                        ( PublisherID int,
                          Name VARCHAR(255),
                          Address VARCHAR(255),
                          Discount int
                          );"""
  # insertion command for Publisher table
  insertPublishers = """INSERT INTO Publishers
                    ( PublisherID , Name, Address, Discount) VALUES (%s,%s,%s,%s)"""
  publisherValues=[
    (1, 'Addison-Wesley', '123 East Rutherford, New Jersey, NJ 11426, USA', 2),
    (2, 'McGraw-Hill', '725 Main St, Baltimore, MD 21333, USA', 4),
    (3, 'Wiley', '411 42nd St, New York, NY 10141, USA', 3),
    (4, 'Elsevier', '83rd Phillips Straat, Rotterdam, Netherlands', 1),
    (5, 'Longman', '63 Piccardly Square, London, England 4GK231', 7),
    (6, 'Course Technology', '38 Harvard Road, Boston, MA 05211, USA', 6),
    (7, 'Jones & Bartlett', '500 Waterfron Road, Chicago, IL 60149, USA', 6),
    (8, 'Penguin', '80 Plantation House, Blantyre, Malawi', 5),
    (9, 'City Publications', '111 Mohammad Ali Blvd, Louisville, KY 40252, USA', 10),
    (10, 'Simon & Schuster', '300 Hollywood Blvd, Los Angeles, CA 90152, USA', 8),
    (11, 'CRC', '46 Queen Elizabeth Av, Toronto, Canada T32VK9', 1),
    (12, 'Pearson', '330 Hudson Street, New York, NY 10013', 1),
      ]
  # defining Books table structure
  createBooksTable = """CREATE TABLE Books
                        ( isbn BIGINT,
                          title VARCHAR(255),
                          author VARCHAR(255),
                          qty_in_stock int,
                          price double,
                          cost double,
                          year int,
                          PublisherID int
                          );"""
  # insertion command for Books Table
  insertBooks = """INSERT INTO Books
                    ( isbn, title, author, qty_in_stock,price, cost, year, PublisherID ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
  bookvalues= [
    (97899590597, 'The Water Dancer', 'Ta-Nehisi Coates', 70, 28.00, 20.00, 2019, 5),
    (32132132132, 'Peace Corps', 'Jack and Angene Wilson', 50, 15.00, 12.00, 2011, 9),
    (97942335221, 'Fundamentals of Database Systems', 'Ramez Elmasri', 100, 125.00, 100.00, 2011, 1),
    (64814414414, 'Legal Issues of Computer Security', 'Joanna Gramma', 20, 60.00, 55.00, 2012, 7),
    (12345678901, 'Discrete Mathematics', 'Kenneth Rosen', 200, 212.69, 175.00, 2019, 2),
    (44444444444, 'Visual Basic: Step by Step', 'Malik', 100, 38.75, 35.00, 2007, 6),
    (98013200025, 'Cryptography', 'Stinson', 10, 105.00, 75.00, 2008, 11),
    (27224421166, 'C++ Programming Language', 'Stroustrup', 300, 62.50, 50.00, 2013, 1),
    (33421111222, 'Steve Jobs', 'Walter Isaacson', 1000, 47.45, 40.25, 2011, 10),
    (43433333444, 'Software Engineering', 'Frank Tsui', 70, 53.53, 43.43, 2009, 7),
    (58729955411, 'Computer Security', 'Frank Conklin', 30, 82.75, 80, 2010, 3),
    (62588811432, 'Things Fall Apart', 'Chinua Achebe', 5, 12.00, 10.00, 1968, 5),
    (77744555663, 'No Easy Task', 'Aubrey Kayira', 2, 7.00, 5.00, 1970, 8),
    (97812345678, 'Computer Networks', 'Peterson', 8, 112.00, 100.00, 2004, 1),
    (87062662662, 'Differential Equations', 'Perko', 12, 95.00, 90.00, 2000, 4),
    (70626626621, 'Computers in Action 9th Ed', 'Parsley', 500, 130.00, 90.00, 2013, 2),
    (97804444321, 'Starting out with Python 4th Ed', 'Gaddis', 150, 120.00, 96.00, 2020, 12)
  ]
  # defining Orders table structure
  createOrdersTable = """CREATE TABLE Orders
                        ( ordernum int,
                          custID int,
                          Cardnum BIGINT,
                          Cardmonth int,
                          Cardyear int,
                          Orderdate VARCHAR(255),
                          Shipdate VARCHAR(255)
                          );"""  
  # insertion command for Orders Table 
  insertOrders = """INSERT INTO Orders
                    ( ordernum, custID, Cardnum, Cardmonth,Cardyear, Orderdate, Shipdate ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""    
  ordervalues=[
    (1, 10, 4141111122223333, 7, 2020, '2020-1-26', '2020-1-31'),
    (2, 1, 5082414100414242, 6, 2020, '2020-2-14', '2020-2-21'),
    (3, 8, 6011222233334444, 9, 2020, '2020-2-10', '2020-2-12'),
    (4, 12, 312814774182131, 8, 2020, '2020-1-30', '2020-2-4'),
    (5, 2, 4044400400001018, 3, 2020, '2020-2-20', '2020-2-25'),
    (6, 5, 5155001415631012, 10, 2020, '2020-2-22', '2020-2-26' )
  ]
  # defining OrderList table structure
  createOrdersListTable = """CREATE TABLE OrderList
                        ( ordernum int,
                          isbn BIGINT,
                          Quantity int
                          );"""
  # insertion command for OrderList Table
  insertOrdersList = """INSERT INTO OrderList
                    ( ordernum, isbn, Quantity) VALUES (%s,%s,%s)"""    
  orderListvalues=[
    (1, 62588811432, 3),
    (1, 97942335221, 1),
    (1, 32132132132, 15),
    (2, 27224421166, 1),
    (3, 33421111222, 2),
    (3, 12345678901, 1),
    (4, 27224421166, 1),
    (5, 33421111222, 2),
    (6, 12345678901, 1)
    ]
  # creating Customers Table
  mycursor.execute(createCustomerTable)
  # inert command executes with values list
  mycursor.executemany(insertCustomers,customerValues)
  # commiting changes
  mydb.commit()

  # creating Publishers Table
  mycursor.execute(createPublishersTable)
  # inert command executes with values list
  mycursor.executemany(insertPublishers,publisherValues)
  # commiting changes
  mydb.commit()

  # creating Books Table
  mycursor.execute(createBooksTable)
  # inert command executes with values list
  mycursor.executemany(insertBooks,bookvalues)
  # commiting changes
  mydb.commit()

  # creating Orders Table
  mycursor.execute(createOrdersTable)
  # inert command executes with values list
  mycursor.executemany(insertOrders,ordervalues)
  # commiting Changes
  mydb.commit()

  # Creating OrderList Changes
  mycursor.execute(createOrdersListTable)
  # inert command executes with values list
  mycursor.executemany(insertOrdersList,orderListvalues)
  # commiting changes
  mydb.commit()

  # start main programme loop 
  loop()




