from modules.mySqlDB import MySQLDB

class ReportsDAO:
    def __init__(self):
        self.db = MySQLDB()

    def fetch_pending_reports(self):
        select_query = """
             SELECT id,
                    userId,
                    period
                FROM reports r 
                WHERE r.url  IS NULL
        """
        
        return self.db.fetch_data(select_query)

    def update_report_status_and_url(self, report_id, url):
        """
        Updates the status to 'processed' and sets the URL for a report identified by its ID.

        Parameters:
        - report_id: The ID of the report to be updated.
        - url: The new URL to be set for the report.
        """
        update_query = """
            UPDATE reports
               SET status = 'processed',
                   url = %s
             WHERE id = %s
        """
        self.db.execute_query(update_query, (url, report_id))