from modules.mySqlDB import MySQLDB

class UsersDAO:
    def __init__(self):
        self.db = MySQLDB()

    def fetch_users(self):
        select_query = """
          SELECT id, name, email, validated, profile
            FROM users
        """
        
        return self.db.fetch_data(select_query)

    def update_user_profile(self, email):
        """
        Update user profile

        :param email: User's email
        """
        update_query = """
            UPDATE users
               SET validated = 1,
                   profile = 'pro_user'
             WHERE email = %s
        """
        update_params = [email]
        self.db.execute_query(update_query, update_params)
