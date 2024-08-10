# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv


def to_read_the_csv_file(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        data = [row for row in reader]
    return data


first_csv_file = to_read_the_csv_file('csv_files/random.csv')
second_csv_file = to_read_the_csv_file('csv_files/random-michaels.csv')

combined_data_from_csv_files = first_csv_file + second_csv_file[1:]

seen_all_data = set()
unique_data_left = []

for row in combined_data_from_csv_files:
    row_tuple = tuple(row)
    if row_tuple not in seen_all_data:
        seen_all_data.add(row_tuple)
        unique_data_left.append(row)


def to_write_in_new_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


to_write_in_new_csv('result_solodukhina.csv', unique_data_left)
