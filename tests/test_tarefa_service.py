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

    def test_get_all_tarefas(self):
        self.service.create({
            "titulo": "Estudar Ciência de Dados",
            "descricao": "Aprender os conceitos de Machine Learning",
            "status": "concluída"
        })

        self.service.create({
            "titulo": "Fazer atividade de Engenharia de Software",
            "descricao": "Fazer relatório da atividade sobre TDD",
            "status": "pendente"
        })

        tarefas = self.service.get_all()

        self.assertEqual(len(tarefas), 2)

    def test_get_tarefa_by_id(self):
        tarefa_criada = self.service.create({
            "titulo": "Ler sobre Git",
            "descricao": "Revisar comandos básicos do Git",
            "status": "pendente"
        })

        tarefa_encontrada = self.service.get_by_id(tarefa_criada["id"])

        self.assertEqual(tarefa_encontrada["titulo"], "Ler sobre Git")


if __name__ == "__main__":
    unittest.main()