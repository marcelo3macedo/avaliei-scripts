import uuid, logging
from modules.mySqlDB import MySQLDB

class KpisDAO:
    def __init__(self):
        self.db = MySQLDB()

    def insert_kpi_data(self, userId, volDaily, volGeneral, pontDaily, pontGeneral):
        """
        Inserts data into the kpis table.

        :param userId: User's ID
        :param volDaily: Daily volume
        :param volGeneral: General volume
        :param pontDaily: Daily points
        :param pontGeneral: General points
        """
        exists_query = "SELECT COUNT(*) as count FROM kpis WHERE userId = %s"
        exists_params = (userId,)
        result = self.db.fetch_data(exists_query, exists_params)

        entry_id = str(uuid.uuid4())
        if result[0]['count'] > 0:
            update_query = """
                UPDATE kpis
                SET volDaily = %s, volGeneral = %s, pontDaily = %s, pontGeneral = %s
                WHERE userId = %s
            """
            update_params = (volDaily, volGeneral, pontDaily, pontGeneral, userId)
            self.db.execute_query(update_query, update_params)
        else:
            insert_query = """
                INSERT INTO kpis (id, userId, volDaily, volGeneral, pontDaily, pontGeneral)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            insert_params = (entry_id, userId, volDaily, volGeneral, pontDaily, pontGeneral)
            self.db.execute_query(insert_query, insert_params)
