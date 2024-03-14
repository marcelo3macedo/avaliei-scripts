import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('configs/credentials.json', scope)
client = gspread.authorize(creds)

class GoogleSheets:
    def update_sheet_with_dicts(self, spreadsheet_id, sheet_name, data_dicts):
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        headers = list(data_dicts[0].keys()) if data_dicts else []

        for index, data_dict in enumerate(data_dicts, start=1):
            headers = list(data_dict.keys())
            row_values = [data_dict.get(header, '') for header in headers]
            
            range_to_update = f"A{index+1}:{chr(64 + len(row_values))}{index+1}"
            try:
                sheet.update(range_to_update, [row_values])
            except Exception as e:
                print(f"Error updating row at index {index}: {e}")
