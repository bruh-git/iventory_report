import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            return list(csv.DictReader(file))
