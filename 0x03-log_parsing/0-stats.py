#!/usr/bin/python3

import sys

total_size = 0
status_codes = {'200': 0,
                '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0,
                '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        line = line.split()
        if len(line) == 9:
            total_size += int(line[-1])
            if line[-2] in status_codes.keys():
                status_codes[line[-2]] += 1
        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print('{}: {}'.format(code, status_codes[code]))
except KeyboardInterrupt:
    print('File size: {}'.format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print('{}: {}'.format(code, status_codes[code]))
