import sqlite3

def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()


if __name__ == "__main__":
    sql = "update ProductType set ProductTypeID = 1 where ProductTypeID = 57"
    sql = "delete from ProductType where ProductTypeID = 1"
    query(sql,())
