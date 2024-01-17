class SistemaEntregaComida:
    id_pedido = 0
    registro_pedidos = {}

    def __init__(self):
        self.cardapio = {
            "Hambúrguer": 35,
            "Pizza": 70,
            "Macarrão": 55,
            "Salada": 20,
            "Bebidas": 20,
            "Macarrão Instantâneo": 5,
            "Sushi": 270,
            "Padaria": 50
            # Adicione mais itens ao cardápio
        }
        self.valor_pedido = 0

    def exibir_cardapio(self):
        """
        Retorna o cardápio como um dicionário.
        """
        return self.cardapio

    def fazer_pedido(self, nome_cliente, itens_pedido):
        """
        Retorna o registro de pedidos após o pedido feito por um cliente com status "Realizado", caso contrário, retorna "falha no pedido".
        Formato:
        registro_pedidos = {id_pedido: {"nome_cliente": ABC, "itens_pedido":{"item1":"Quantidade"}, status = "Realizado"}}
        """
        self.id_pedido += 1
        detalhes_pedido = {"nome_cliente": nome_cliente, "itens_pedido": itens_pedido, "status": "Realizado"}
        self.registro_pedidos[self.id_pedido] = detalhes_pedido
        return self.registro_pedidos

    def retirar_pedido(self, id_pedido):
        """
        Altera o status do pedido para "Retirado" se estiver "Realizado".
        Retorna o status.
        """
        if id_pedido in self.registro_pedidos and self.registro_pedidos[id_pedido]["status"] == "Realizado":
            self.registro_pedidos[id_pedido]["status"] = "Retirado"
            return "Retirado"
        else:
            return "Falha na retirada do pedido. Pedido não existe ou já foi retirado ou não foi realizado."

    def entregar_pedido(self, id_pedido):
        """
        Altera o status do pedido para "Entregue" se estiver "Retirado".
        Retorna o status.
        """
        if id_pedido in self.registro_pedidos and self.registro_pedidos[id_pedido]["status"] == "Retirado":
            self.registro_pedidos[id_pedido]["status"] = "Entregue"
            return "Entregue"
        else:
            return "Falha na entrega do pedido. O pedido ainda não foi retirado."

    def modificar_pedido(self, id_pedido, novos_itens):
        """
        Retorna o pedido modificado com itens disponíveis no cardápio apenas se o pedido não foi retirado:
        {id_pedido: {"nome_cliente": ABC, "itens_pedido":{"item1":"Quantidade", novos_itens}, status = "Realizado"}}
        """
        if id_pedido in self.registro_pedidos and self.registro_pedidos[id_pedido]["status"] != "Retirado":
            self.registro_pedidos[id_pedido]["itens_pedido"].update(novos_itens)
            return self.registro_pedidos[id_pedido]
        else:
            return "Falha na modificação do pedido. Pedido não existe ou já foi retirado."

    def gerar_conta(self, id_pedido):
        """
        Se a soma de todos os itens > 1000
        Valor = Soma de todos os itens do pedido + 10% do valor total
        Se a soma de todos os itens < 1000
        Valor = Soma de todos os itens do pedido + 5% do valor total
        Retorna o valor total da conta.
        """
        if id_pedido in self.registro_pedidos:
            soma_total = sum(self.cardapio[item] * quantidade for item, quantidade in self.registro_pedidos[id_pedido]["itens_pedido"].items())
            if soma_total > 1000:
                self.valor_pedido = soma_total + 0.10 * soma_total
            else:
                self.valor_pedido = soma_total + 0.05 * soma_total
            return self.valor_pedido
        else:
            return "Pedido não encontrado."

    def cancelar_pedido(self, id_pedido):
        """
        Cancela os itens do pedido para o cliente se o pedido não foi retirado e remove os detalhes do pedido do registro_pedidos.
        Retorna o registro de pedidos. Por exemplo, se houver 3 pedidos, mas o terceiro pedido for cancelado, você precisa removê-lo do registro_pedidos e apenas retornar os dois primeiros pedidos:
        {1: {"nome_cliente":"clienteA", "itens_pedido":{"Hambúrguer":1,"Macarrão":2},"status":"Entregue"}, 2: {"nome_cliente":"clienteB", "itens_pedido":{"Salada":2,"Sushi":4, "Bebidas":6, "Padaria":2},"status":"Realizado"}}
        """
        if id_pedido in self.registro_pedidos and self.registro_pedidos[id_pedido]["status"] != "Retirado":
            del self.registro_pedidos[id_pedido]
            return self.registro_pedidos
        else:
            return "Falha no cancelamento do pedido. Pedido não existe ou já foi retirado."