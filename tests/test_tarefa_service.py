import unittest
from src.tarefa_service import TarefaService


class TestTarefaService(unittest.TestCase):
    def setUp(self):
        self.service = TarefaService()


if __name__ == "__main__":
    unittest.main()