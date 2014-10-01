import sqlite3
from datetime import datetime

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table '{0}' already exists, do you wish to recreate it? (y/n): ".format(table_name))
                print()
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print("The '{0}' table will be recreated, all existing data will be lost".format(table_name))
                    print()
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_customer_table():
    sql = """create table Customer
             (CustomerID integer
             FirstName text,
             LastName text,
             AddressLine1 text
             Town text,
             PostCode text ,
             EmailAddress text,
             primary key(CustomerID)
             )"""
    create_table(db_name, "Customer", sql)

def create_customer_order_table():
    sql = """create table CustomerOrder
             (OrderID integer,
             Date YYYY MM DD,
             Time hh mm ss,
             CustomerID integer,
             primary key (OrderID)
             foreign key (CustomerID) references Customer(CustomerID)
             )"""
    create_table(db_name,"CustomerOrder", sql)

def create_order_item_table():
    sql = """create table OrderItem
             (OrderItemID integer,
             OrderID integer,
             ProductID integer,
             Quantity integer,
             primary key (OrderItemID)
             foreign key (OrderID) references CustomerOrder(OrderID)
             foreign key (ProductID) references Product(ProductID)
             )"""
    create_table(db_name, "OrderItem", sql)
    

def create_product_table():
    sql = """create table Product
             (ProductID integer,
             Name text,
             Price real,
             ProductTypeID integer,
             primary key(ProductID)
             foreign key(ProductTypeID) references ProductType(ProductTypeID)
             on update set null on delete set null)"""
    create_table(db_name,"Product",sql)

def create_product_type_table():
    sql = """create table ProductType
           (ProductTypeID integer,
           Description text,
           primary key(ProductTypeID))"""
    create_table(db_name, "ProductType", sql)
    

if __name__ == "__main__":
    db_name = "coffee_shop.db"
    create_customer_table()
    create_customer_order_table()
    create_order_item_table()
    create_product_table()
    create_product_type_table()
