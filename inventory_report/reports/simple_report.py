class SimpleReport:
    @classmethod
    def generate(cls, list):
        return (
            f"Data de fabricação mais antiga: "
            f"{cls.get_min_fabrication(list)}\n"
            f"Data de validade mais próxima: "
            f"{cls.get_min_expired(list)}\n"
            f"Empresa com mais produtos: "
            f"{cls.get_max_company(list)}"
        )

    @classmethod
    def get_min_fabrication(cls, list):
        return min([item["data_de_fabricacao"] for item in list])

    @classmethod
    def get_min_expired(cls, list):
        return min([item["data_de_validade"] for item in list])

    @classmethod
    def get_max_company(cls, list):
        return max(
            [item["nome_da_empresa"] for item in list],
            key=[item["nome_da_empresa"] for item in list].count,
        )
