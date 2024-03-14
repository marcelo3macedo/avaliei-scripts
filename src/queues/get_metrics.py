import logging, os
from dao.users import UsersDAO
from modules.googleSheets import GoogleSheets

def get_metrics(message):
    logging.info(f"get_metrics - {message}")
    users_dao = UsersDAO()
    google_sheets = GoogleSheets()
    spreedsheet_id = os.getenv('SPREADSHEET_ID', '')

    data = users_dao.fetch_users()

    google_sheets.update_sheet_with_dicts(spreedsheet_id, "users", data)
