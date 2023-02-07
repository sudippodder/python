from sql_connection import get_sql_connection

def get_all_product(connection):
  cursor = connection.cursor()
  query =("SELECT pt.product_id,pt.name,pt.unit_id,pt.price,ut.unit_name FROM product_table as pt INNER JOIN unit_table as ut on pt.unit_id=ut.unit_id")
  cursor.execute(query)
  response = []
  for (product_id, name, unit_id, price, unit_name) in cursor:
    response.append(
      {
      'product_id': product_id,
      'name': name,
      'unit_id': unit_id,
      'price': price,
      'unit_name': unit_name
      }
    )
  
  return response

def insert_new_product(connection, product_table):
  cursor = connection.cursor()
  query = ("INSERT INTO `product_table`(`name`, `unit_id`, `price`) VALUES (%s,%s,%s)")
  data = (product_table['name'],product_table['unit_id'],product_table['price'])
  cursor.execute(query,data)
  connection.commit()

  return cursor.lastrowid


def delete_product(connection, product_id):
  cursor = connection.cursor()
  query = ("DELETE FROM `product_table` where product_id=" + str(product_id))
  cursor.execute(query)
  connection.commit()

  return 1

  if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12))