from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Arroz",
        "Arroz do Vale",
        "2020-01-01",
        "2020-12-31",
        "123456789",
        "em local seco",
    )
    assert (
        product.__repr__()
        == "O produto Arroz"
        " fabricado em 2020-01-01"
        " por Arroz do Vale com validade"
        " até 2020-12-31"
        " precisa ser armazenado em local seco."
    )
