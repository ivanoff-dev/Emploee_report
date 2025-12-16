import argparse
import csv
import os


class EmployeeArgsParser(argparse.ArgumentParser):
    """
    Класс для парсинга аргументов команды в CLI.
    """
    def __init__(self):
        super().__init__()
        self.add_argument(
            '--files',
            nargs='+',
            required=True
        )
        self.add_argument(
            '--report',
            required=True
        )

    def get_source_files_paths(self):
        """
        Метод возвращает список путей к файлам,
        полученный из аргументов в CLI.
        """
        args = self.parse_args()
        return args.files
    
    def get_report_name(self):
        """
        Метод возвраащет имя отчета,
        полученное из CLI.
        """
        args = self.parse_args()
        return args.report


class EmployeeParser():
    """
    Класс для парсинга файлов.
    """
    def get_file(self, path):
        """
        Метод позволяет получить файл по указанному пути.
        """
        if os.path.isfile(path):
            file = os.path.abspath(path)
            return file
        else:
            print(f'Неверно указан путь \'{path}\'')

    def get_data_from_file(self, filename):
        """
        Метод позволяет получить данные из файла.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data

    def get_average_performance(self, data):
        """
        Метод позволяет получить данные по средней производительности.
        """
        for employee in data:
            name = employee.get('name')
            performance = employee.get('performance')

    """
    Здесь вы можете написать дополнительные функции
    для обработки исходных данных.
    """
    # def get_employee_qty(self, data):
    #     """
    #     Метод позволяет получить количество сотрудников в разрезе
    #     технологий, которыми они владеют.
    #     """
    #     pass
