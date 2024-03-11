import os, logging
from dao.avaliations import AvaliationsDAO
from dao.reports import ReportsDAO
from helpers.dates import get_first_and_last_day_of_month
from modules.csvGenerator import CsvGenerator

def generate_reports(message):
    logging.info(f"generate_reports - {message}")

    reports_dao = ReportsDAO()
    results = reports_dao.fetch_pending_reports()

    if results is None:
        return

    for r in results:
        url = create_report(r)
        reports_dao.update_report_status_and_url(r['id'], url)

def create_report(query):
    logging.info(f"create_report - ${query['userId']}")
    reports_path = os.getenv('REPORTS_PATH', 'default_folder_path')
    first_day, last_day = get_first_and_last_day_of_month(query['period'])
    avaliations_dao = AvaliationsDAO()
    csv_generator = CsvGenerator()

    results = avaliations_dao.fetch_avaliations(
        query['userId'],
        first_day,
        last_day
    )

    report_id = query['userId'] + "_" + query['period'].replace("/", "_")
    csv_generator.generate(report_id, results)

    return f"{reports_path}/{report_id}.csv"
