# Sistema de Entrega de Comida

Este é um sistema simples de entrega de comida desenvolvido em Python. Ele permite que os usuários façam pedidos, visualizem o cardápio, retirem e entreguem pedidos, gerem contas e cancelem pedidos.

## Funcionalidades

1. **Exibir Cardápio:**
   - Método: `exibir_cardapio()`
   - Descrição: Retorna o cardápio atualizado com os itens disponíveis e seus preços.

2. **Fazer Pedido:**
   - Método: `fazer_pedido(nome_cliente, itens_pedido)`
   - Descrição: Permite que um cliente faça um pedido fornecendo o nome do cliente e os itens desejados com as quantidades. O pedido é registrado no sistema.

3. **Retirar Pedido:**
   - Método: `retirar_pedido(id_pedido)`
   - Descrição: Altera o status de um pedido para "Retirado" se o pedido estiver "Realizado".

4. **Entregar Pedido:**
   - Método: `entregar_pedido(id_pedido)`
   - Descrição: Altera o status de um pedido para "Entregue" se o pedido estiver "Retirado".

5. **Modificar Pedido:**
   - Método: `modificar_pedido(id_pedido, novos_itens)`
   - Descrição: Permite a modificação de um pedido se o pedido ainda não foi retirado. Adiciona novos itens ao pedido.

6. **Gerar Conta:**
   - Método: `gerar_conta(id_pedido)`
   - Descrição: Gera o valor total da conta com base nos itens do pedido. Aplica desconto se o valor total for inferior a 1000.

## Testes Unitários

Os testes unitários estão localizados no diretório `sample_tests`. Eles cobrem várias funcionalidades do sistema e podem ser executados usando o seguinte comando:

```bash
python -m unittest sample_tests.test_sistema_entrega_comida