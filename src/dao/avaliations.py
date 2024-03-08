from modules.mySqlDB import MySQLDB

class AvaliationsDAO:
    def __init__(self):
        self.db = MySQLDB()

    def fetch_avaliations(self, user_id, first_day, last_day):
        select_query = f"""
          SELECT c.id, c.name, a.* 
            FROM avaliations a INNER JOIN   
                 companies c on c.id = a.companyId
           WHERE c.userId = '{user_id}'
             AND a.createdAt BETWEEN '{first_day}' AND '{last_day}'
        """
        
        return self.db.fetch_data(select_query)
