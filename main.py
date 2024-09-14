from flask import Flask, request
import db
app = Flask(__name__)

@app.route("/")

def text():
   return  "assignment class 17"

@app.route("/category", methods=['POST'])

def add_category():
    
    db_conn = db.mysqlconnect()
    data = request.get_json()
    cur = db_conn.cursor()
    name = data['name']
    cur.execute(f"INSERT INTO category (name) VALUES ('{name}')")
    db_conn.commit()
    db.disconnect(db_conn)
    return data
      
@app.route("/product", methods=['POST'])

def add_product():
    
    db_conn = db.mysqlconnect()
    data = request.get_json()
    cur = db_conn.cursor()
    name = data['name']
    cat_id = data['cat_id']
    cur.execute(f"INSERT INTO product (name, cat_id) VALUES ('{name}', '{cat_id}')")
    db_conn.commit()
    db.disconnect(db_conn)
    return data

@app.route("/product/<id>", methods=['PUT'])
def update_product(id):
    db_conn = db.mysqlconnect()
    data = request.get_json()
    cur = db_conn.cursor()
    new_name = data['name']
    cur.execute(f"UPDATE product SET name = '{new_name}' WHERE id = {id}")
    db_conn.commit()
    db.disconnect(db_conn)
    return data

@app.route("/product/<id>", methods=['DELETE'])
def delete_product(id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute(f"DELETE FROM product WHERE id = '{id}'")
    db_conn.commit()
    db.disconnect(db_conn)
    return "deleted"

@app.route("/category", methods=['GET'])
def display_category():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM category")
    category = cur.fetchall()
    db.disconnect(db_conn)
    return category


@app.route("/product", methods=['GET'])
def display_product():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM product")
    product = cur.fetchall()
    db.disconnect(db_conn)
    return product


@app.route("/all", methods=['GET'])
def display_both():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute("select c.name as category_name, p.name as product_name from category as c left join product as p on c.id = p.cat_id")
    combine_cat_pro = cur.fetchall()
    db.disconnect(db_conn)
    return combine_cat_pro


@app.route("/product_count", methods=['GET'])
def total_product():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute("select count(*) as product_count from product")
    product_count = cur.fetchall()
    db.disconnect(db_conn)
    return product_count

app.run(
    debug=True,
    port=3000
)


