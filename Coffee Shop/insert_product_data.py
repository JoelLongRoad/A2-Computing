import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    coffee = [("Espresso",1.50),("Latte",1.35),("Mocha",2.40),("Americano",1.50),("Cappacino",1.80)]
    tea = [("Green Tea",1.20),("Black Tea",1.00)("Earl Grey",1.20)]
    for product in product_list:
        insert_data(product)