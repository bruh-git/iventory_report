import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        report = []

        if (path.endswith(".csv")):
            report = cls.read_csv(path)
        elif (path.endswith(".json")):
            report = cls.read_json(path)
        elif (path.endswith(".xml")):
            report = cls.read_xml(path)

        if (type == 'simples'):
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)

    @classmethod
    def read_csv(cls, path):
        with open(path) as csv_file:
            return list(csv.DictReader(csv_file))

    @classmethod
    def read_json(cls, path):
        with open(path) as json_file:
            return json.loads(json_file.read())

    @classmethod
    def read_xml(cls, path):
        with open(path) as xml_file:
            return xmltodict.parse(xml_file.read())["dataset"]["record"]
