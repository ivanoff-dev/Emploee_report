import csv

from employee_lib.parsers import (
    EmployeeArgsParser,
    EmployeeParser
)


parser = EmployeeArgsParser()
paths = parser.get_source_files_paths()
report = parser.get_report_name()
print(paths)
print(report)

file_parser = EmployeeParser()
for path in paths:
    file = file_parser.get_file(path)
    if file:
        file_parser.get_data_from_file(file)

# with open('./source/employees2.csv', 'r', encoding='utf-8') as file:
#     source_file = csv.reader(file)
#     for row in source_file:
#         print(row)
