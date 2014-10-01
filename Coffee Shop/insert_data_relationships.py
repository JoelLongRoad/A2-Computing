import sqlite3

def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def insert_product_type(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql,record)

def insert_product_data(records):
    sql = "insert into Product (Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql,record)

if __name__ == "__main__":
    product_types = [("Coffee",),("Tea",),("Cold Drinks",),("Other",)]
    
    insert_product_type(product_types)
    
    products = [("Americano",1.75,1),("Cappucino",1.95,1),("Caffe Latte",1.95,1),("Espresso",1.65,1),("Macchiato",1.75,1),("Mocha",2.25,1),("Breakfast Tea",1.50,2),("Earl Grey",1.50,2),("Darjeeling",1.65,2),("Fruit/Herbal Tea",1.75,2),("Soya Milk",0.25,2),("Milk",0.75,3),("Fruit Juices",1.40,3),("Still Water",1.20,3),("Sparkling Water",1.20,3),("Cans",1.00,3),("Coffee Milkshake",2.45,4),("Banana Milkshake",1.95,4),("Hot Chocolate",1.95,4),("Hot Orange Chocolate",2.00,4)]
               
    insert_product_data(products)
