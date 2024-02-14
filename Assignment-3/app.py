# import mysql.connector
 
# # Connect to MySQL
# connection = mysql.connector.connect(
#    host = "adb.ctmaa6g0kdvh.ap-southeast-2.rds.amazonaws.com",
#     user = "admin",
#     password = "Admin123",
#     database="macrobuy" 
# )
 
# # Create a table for storing product details
# create_table_query = """
# CREATE TABLE IF NOT EXISTS products (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     product_details JSON
# )
# """
# cursor = connection.cursor()
# cursor.execute(create_table_query)
 
# # Insert sample records into the table
# insert_query = """
# INSERT INTO products (product_details)
# VALUES
#     ('{"productId": "P10102", "category": "Storage Device", "name": "Ultra Store 32 GB", "other_name": "Pen Drive", "weight": "8 Grams"}'),
#     ('{"productId": "P37446", "category": "Cloths", "size": "XL", "colour": "darkred", "material": "satin"}'),
#     ('{"productId": "U3644748", "category": "Food", "expiry": "2 months from MFG", "MFG-date": "10th Jan, 2024"}')
# """
# cursor.execute(insert_query)
# connection.commit()
 
# # Function to search products by productId
# def search_product_by_id(product_id):
#     select_query = f"SELECT * FROM products WHERE JSON_EXTRACT(product_details, '$.productId') = '{product_id}'"
#     cursor.execute(select_query)
#     result = cursor.fetchone()
#     return result
 

# product_id = 'P3744'  
# result = search_product_by_id(product_id)
 
# if result:
#     print("Product found:")
#     print(result)
# else:
#     print("Product not found")
 
# # Close connection
# cursor.close()
# connection.close()

# DynamoDB
import boto3
 
dynamodb=boto3.client('dynamodb')
 
table_name="mytable"
item=dynamodb.get_item(TableName=table_name,Key={'productid':{'S':'U3644748'},'category': {'S':'Food'}})
# s=[]
# s=item.keys()
if 'Item' in item:
    print("Item found",item['Item'])
else:
    print("Item not found")