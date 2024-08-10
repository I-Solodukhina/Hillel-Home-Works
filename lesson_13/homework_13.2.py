# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import json
import logging
import os

logging.basicConfig(filename='json_solodukhina.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s')

json_files_folder_path = 'work_with_json'


def to_validate_json_files(path):
    for file_name in os.listdir(path):
        if file_name.endswith('.json'):
            file_path = os.path.join(path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
            except json.JSONDecodeError as e:
                logging.error(f'Invalid JSON in file {file_path}: {e}')
                print(f'Invalid JSON in file {file_path}: {e}')


to_validate_json_files(json_files_folder_path)
