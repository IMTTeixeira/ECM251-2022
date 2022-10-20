from src.models.pedido import Pedido
from src.dao.pedido_dao import PedidoDao
class PedidoController:
    def __init__(self) -> None:
        pass

    def pegar_todos_pedidos(self) -> list[Pedido]:
        pedidos = PedidoDao.get_instance().listar_pedidos()
        return pedidos
