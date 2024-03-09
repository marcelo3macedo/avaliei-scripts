import os
from dao.avaliations import AvaliationsDAO
from dao.reports import ReportsDAO
from helpers.dates import get_first_and_last_day_of_month
from modules.csvGenerator import CsvGenerator

def generate_reports(message):
    print(message)

    reports_dao = ReportsDAO()
    results = reports_dao.fetch_pending_reports()

    for r in results:
        url = create_report(r)
        reports_dao.update_report_status_and_url(r['id'], url)

def create_report(query):
    reports_path = os.getenv('REPORTS_PATH', 'default_folder_path')
    first_day, last_day = get_first_and_last_day_of_month(query['period'])
    avaliations_dao = AvaliationsDAO()
    csv_generator = CsvGenerator()

    results = avaliations_dao.fetch_avaliations(
        query['userId'],
        first_day,
        last_day
    )

    report_id = reports_path + '/' + query['userId'] + "_" + query['period'].replace("/", "_")
    csv_generator.generate(report_id, results)

    return f"{report_id}.csv"
