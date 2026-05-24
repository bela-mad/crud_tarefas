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

    def test_update_tarefa(self):
        tarefa = self.service.create({
            "titulo": "Estudar Python",
            "descricao": "Revisar conceitos básicos",
            "status": "pendente"
        })

        tarefa_atualizada = self.service.update(tarefa["id"], {
            "titulo": "Estudar Python e R",
            "descricao": "Revisar Python e R",
            "status": "em andamento"
        })

        self.assertEqual(tarefa_atualizada["titulo"], "Estudar Python e R")
        self.assertEqual(tarefa_atualizada["descricao"], "Revisar Python e R")
        self.assertEqual(tarefa_atualizada["status"], "em andamento")

    def test_delete_tarefa(self):
        tarefa = self.service.create({
            "titulo": "Fazer relatório",
            "descricao": "Escrever relatório da atividade de TDD",
            "status": "pendente"
        })

        resultado = self.service.delete(tarefa["id"])
        tarefas = self.service.get_all()

        self.assertTrue(resultado)
        self.assertEqual(len(tarefas), 0)

    def test_return_none_get_tarefa_inexistente(self):
        tarefa = self.service.get_by_id(999)

        self.assertIsNone(tarefa)

    def test_return_none_update_tarefa_inexistente(self):
        resultado = self.service.update(999, {
            "titulo": "Tarefa inexistente",
            "descricao": "Essa tarefa não existe",
            "status": "pendente"
        })

        self.assertIsNone(resultado)

    def test_return_false_delete_tarefa_inexistente(self):
        resultado = self.service.delete(999)

        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()