CREATE_TABLE = """CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    kcal int,
    ml int,
    description text,
    is_fruit boolean);"""

INSERT_PRODUCT = "INSERT INTO products (name, kcal, ml, description, is_fruit) VALUES (%s, %s, %s, %s, %s)"

SELECT_FRUIT = "SELECT * FROM products WHERE is_fruit = True"

SELECT_VEGETABLES = "SELECT * FROM products WHERE is_fruit = false"
