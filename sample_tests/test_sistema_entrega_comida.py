import unittest

from src.sistema_entrega_comida import SistemaEntregaComida

class Test(unittest.TestCase):
    def test_validacao(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.exibir_cardapio(), {
            "Hambúrguer": 35,
            "Pizza": 70,
            "Macarrão": 55,
            "Salada": 20,
            "Bebidas": 20,
            "Macarrão Instantâneo": 5,
            "Sushi": 270,
            "Padaria": 50
        })

    def test_validacao1(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.fazer_pedido("Maria Silva", {"Hambúrguer": 1, "Macarrão": 2}), {1: {"nome_cliente": "Maria Silva", "itens_pedido": {"Hambúrguer": 1, "Macarrão": 2}, "status": "Realizado"}})

    def test_validacao2(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.gerar_conta(1), 577.5)

    def test_validacao3(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.retirar_pedido(1), "Retirado")

    def test_validacao4(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.entregar_pedido(1), "Entregue")

    def test_validacao5(self):
        sistema_entrega = SistemaEntregaComida()
        self.assertEqual(sistema_entrega.cancelar_pedido(1), {})