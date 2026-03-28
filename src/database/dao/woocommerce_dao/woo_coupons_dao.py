from src.database.core.database_core import DBCore


class WooCouponsDao:
    def __init__(self):
        self.db_core = DBCore()
        cursor = self.db_core.create_connection()

    def verify_coupon_existed(self,coupon_title,coupon_id=None):
        if not coupon_id:
            sql = f'SELECT ID FROM wp_posts WHERE post_type="shop_coupon" and post_title="{coupon_title}" LIMIT 1;'
            return self.db_core.execute_select(sql)
        sql=f'SELECT * FROM wp_posts WHERE post_type="shop_coupon" and post_title="{coupon_title}" and ID = {coupon_id};'
        return self.db_core.execute_select(sql)
