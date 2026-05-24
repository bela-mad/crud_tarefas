class TarefaService:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def create(self, dados):
        nova_tarefa = {
            "id": self.proximo_id,
            "titulo": dados["titulo"],
            "descricao": dados["descricao"],
            "status": dados["status"]
        }

        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1

        return nova_tarefa