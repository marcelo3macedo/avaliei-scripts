from dotenv import load_dotenv
import os
import csv

load_dotenv()

reports_folder = os.getenv('REPORTS_FOLDER', 'default_folder_path')

class CsvGenerator:
    def generate(self, id, data, headers=None):
        """
        Generates a CSV file from the provided data.

        Parameters:
        - filename: The path to the output CSV file.
        - data: The data to be written to the CSV file. This can be a list of dictionaries or a list of tuples.
               If it's a list of tuples, the first tuple should contain the column headers.
        """
        os.makedirs(os.path.dirname(reports_folder), exist_ok=True)
        
        filename = os.path.join(reports_folder, f"{id}.csv")

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            if data:
                is_dict = isinstance(data[0], dict)
                if is_dict:
                    if headers is None:
                        headers = data[0].keys()
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    writer = csv.writer(file)
                    if headers is None:
                        headers = data[0]  # Assuming the first element are the headers
                        data = data[1:]  # Exclude the first row from data to be written next
                    else:
                        writer.writerow(headers)  # Write the headers explicitly if provided
                    writer.writerows(data)
            else:
                if headers is None:
                    print("No data and no headers provided. Creating an empty CSV file.")
                writer = csv.writer(file)
                if headers is not None:
                    writer.writerow(headers)