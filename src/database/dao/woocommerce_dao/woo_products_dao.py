import random
from src.database.core.database_core import DBCore
class WooProductsDao:
    def __init__(self):
        self.db_core = DBCore()
        cursor = self.db_core.create_connection()

    def get_product_from_database_by_id(self,product_id):
        sql = f'SELECT * FROM wp_posts WHERE post_type = "product" AND ID = {product_id};'
        db_result = self.db_core.execute_select(sql)
        if not db_result:
            return None
        else:
            return db_result[0]
    def get_all_products_from_database(self):
        sql = f'SELECT * FROM wp_posts WHERE post_type = "product";'
        return self.db_core.execute_select(sql)

    def get_the_latest_product_from_database(self):
        sql = 'SELECT * FROM wp_posts WHERE post_type = "product" ORDER BY post_modified desc LIMIT 1;'
        return self.db_core.execute_select(sql)[0]


    def get_a_regular_price_by_id(self,product_id):
        sql = f'SELECT meta_value FROM wp_postmeta where meta_key= "_regular_price" and post_id ={product_id}'
        return self.db_core.execute_select(sql)[0]['meta_value']
    def get_the_stock_quantity_via_product_id(self,product_id):
        sql = f'SELECT stock_quantity FROM wp_wc_product_meta_lookup where product_id = {product_id};'
        return self.db_core.execute_select(sql)[0]['stock_quantity']