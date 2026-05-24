import unittest
from src.tarefa_service import TarefaService


class TestTarefaService(unittest.TestCase):
    def setUp(self):
        self.service = TarefaService()

    def test_create_tarefa_estudo(self):
        tarefa = self.service.create({
            "titulo": "Estudo de Sistemas Distribuídos",
            "descricao": "Revisar roteamento distribuído",
            "status": "pendente"
        })

        self.assertIn("id", tarefa)
        self.assertEqual(tarefa["titulo"], "Estudo de Sistemas Distribuídos")
        self.assertEqual(tarefa["descricao"], "Revisar roteamento distribuído")
        self.assertEqual(tarefa["status"], "pendente")


if __name__ == "__main__":
    unittest.main()