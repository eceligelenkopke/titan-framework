from src.database.core.database_core import DBCore

class WooOrdersDao:
    def __init__(self):
        self.db_core = DBCore()
        cursor = self.db_core.create_connection()

    def get_all_orders_from_db(self):
        sql = f"SELECT * FROM wp_wc_orders;"
        return self.db_core.execute_select(sql)

    def get_the_latest_order_from_db(self):
        sql = f"SELECT * FROM local.wp_wc_orders ORDER BY date_created_gmt desc LIMIT 1;"
        return self.db_core.execute_select(sql)

    def get_order_by_order_id(self, order_id):
        sql = f"SELECT * FROM wp_wc_orders WHERE ID = {order_id}; "
        return self.db_core.execute_select(sql)[0]

    def get_order_by_customer_id(self,customer_id):
        sql = f"SELECT * FROM wp_wc_orders WHERE customer_id = {customer_id};"
        return self.db_core.execute_select(sql)[0]

    def get_order_by_date_created_desc(self):
        sql = f"SELECT * FROM wp_wc_orders ORDER BY date_created_gmt desc;"
        return self.db_core.execute_select(sql)

    def get_order_by_customer_email(self,customer_email):
        sql = f'SELECT * FROM wp_wc_orders INNER JOIN wp_users where user_email="{customer_email}";'
        return self.db_core.execute_select(sql)

    def get_order_by_billing_email(self,billing_email):
        sql = f'SELECT * FROM wp_wc_orders WHERE billing_email = "{billing_email}";'
        return self.db_core.execute_select(sql)

    def get_order_by_order_status(self,order_status):
        sql = f'SELECT * FROM wp_wc_order_stats where status = "{order_status}";'
        return self.db_core.execute_select(sql)[0]

    def get_total_amount_by_order_id(self, order_id):
        sql = f'SELECT total_amount FROM wp_wc_orders where id ={order_id};'
        return float(self.db_core.execute_select(sql)[0]['total_amount'])
