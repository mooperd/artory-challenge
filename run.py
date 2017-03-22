# Tested in Python 3.5.2 & Python 2.7.10
import csv
import re
from collections import Counter
from datetime import datetime


def read_file(file_path):
    data = []
    with open(file_path, 'rt' ) as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',' )
        for row in file_reader:
            # According to the docs the day and month should be zero padded but it seems to work ok.
            row[0] = datetime.strptime(row[0], '%d.%m.%Y %H:%M')
            # Convert outcome to true/fase. One less string which should improve performance when tallying.
            row[3] = bool(re.match('COMPLETED', row[3]))
            data.append(row)
    return data


def math(data):
    """ Perhaps it would be better to tally whilst reading in the file although perhaps we wont always be getting the
      data from a file. If the amount of input data gets huge then this will need rethinking.
    """
    tally = dict()
    # Iterate through the data
    for row in data:

        # If the key (phone #) does not exist then create it with a counter
        if not row[1] in tally.keys():
            tally[row[1]] = Counter()

        if not row[2] in tally.keys():
            tally[row[2]] = Counter()

        # Tally Failed calls here
        if not row[3]:
            tally[row[1]]['FAILED'] += 1
            tally[row[2]]['FAILED'] += 1

        # Tally Completed calls here
        if row[3]:
            tally[row[1]]['COMPLETED'] += 1
            tally[row[2]]['COMPLETED'] += 1

    # Iterate through the tally and calculate the percentage.
    for number, values in tally.items():
        try:
            percentage = round(float(values['COMPLETED'])
                                    / (float(values['FAILED'])
                                    + float(values['COMPLETED']))
                                    * 100, 2)
            # Print output. This could be made prettier but the instructions imply that we should only use the
            # standard library.
            print(number + " " + str(percentage) + "%")
        except ZeroDivisionError as msg:
            print(msg)

if __name__ == '__main__':
    math(read_file('data.csv'))
