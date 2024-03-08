from modules.mySqlDB import MySQLDB

class UserRatingsDAO:
    def __init__(self):
        self.db = MySQLDB()

    def fetch_user_ratings(self):
        select_query = """SELECT 
                a.userId,
                AVG(a.stars) as pontGeneral,
                AVG(b.stars) as pontDaily,
                COUNT(DISTINCT a.stars) as volGeneral,
                COUNT(DISTINCT b.stars) as volDaily
            FROM (
                SELECT 
                    a.stars,
                    c.userId
                FROM avaliations a
                LEFT JOIN companies c ON c.id = a.companyId
            ) AS a left join
            (
                SELECT 
                    a.stars,
                    c.userId
                FROM avaliations a
                LEFT JOIN companies c ON c.id = a.companyId
            WHERE a.createdAt  > CURDATE() - INTERVAL 1 DAY 
            ) AS b on b.userId = a.userId
            GROUP BY 
                userId"""
        
        return self.db.fetch_data(select_query)
