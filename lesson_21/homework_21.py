import logging
from datetime import datetime

logging.basicConfig(filename='hb_test.log', level=logging.WARNING, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger("log_event")


def requirements_checker(file_name='hblog.txt'):
    main_log = []
    filtered_log = []
    with open(file_name, 'r') as f:
        main_log.extend(f.readlines())

    for line in main_log:
        if 'Key TSTFEED0300|7E3E|0400' in line:
            filtered_log.append(line)
    i = 0
    f = 1
    while f < len(filtered_log):
        current_line = filtered_log[i]
        next_line = filtered_log[f]
        current_timestamp = datetime.strptime((current_line[current_line.find('Timestamp ') + 10:current_line.find('Timestamp ') + 18]), '%H:%M:%S')
        next_timestamp = datetime.strptime((next_line[next_line.find('Timestamp ') + 10:next_line.find('Timestamp ') + 18]), '%H:%M:%S')
        if 31 < (current_timestamp - next_timestamp).seconds < 33:
            logger.warning(f'Time start-end: {current_timestamp.strftime('%H:%M:%S')} - {next_timestamp.strftime('%H:%M:%S')}')
        if (current_timestamp - next_timestamp).seconds >= 33:
            logger.error(f'Time start-end: {current_timestamp.strftime('%H:%M:%S')} - {next_timestamp.strftime('%H:%M:%S')}')
        i += 1
        f += 1


requirements_checker()
