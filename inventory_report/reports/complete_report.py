from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        return (
            f"{super().generate(list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.products_by_company(list)}"
        )

    @classmethod
    def products_by_company(cls, list):
        companies = dict()

        for item in list:
            companies[item["nome_da_empresa"]] = cls.quantity(
                item["nome_da_empresa"], list
            )

        list_quantity = ""

        for key, value in companies.items():
            list_quantity += f"- {key}: {value}\n"

        return list_quantity

    @classmethod
    def quantity(cls, company, list):
        return str([item["nome_da_empresa"] for item in list].count(company))
