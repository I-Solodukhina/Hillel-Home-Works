# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
# timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger('').addHandler(console_handler)

# logging.info('Log info')

tree = ET.parse('xml_file/groups.xml')
root = tree.getroot()
xml_file_path = 'xml_file/groups.xml'


def to_find_timing_exbytes_incoming(xml_data, group_number):
    for group in root.findall('group'):
        number = group.find('number').text
        if number == str(group_number):
            incoming = group.find('timingExbytes/incoming').text
            return incoming
    return None


number_of_the_group = 2
logging.info(f"The incoming parameter for group number {number_of_the_group}: "
             f"{to_find_timing_exbytes_incoming(xml_file_path, number_of_the_group)}")

