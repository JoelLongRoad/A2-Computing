import sqlite3

def insert_data(values):
    with sqlite3.connect("cineworld_kit_list.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Type, Price, Quantity) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    kit_list_visual = []
    for product in product_list:
        insert_data(product)
