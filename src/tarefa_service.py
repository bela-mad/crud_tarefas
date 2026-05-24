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

    def get_all(self):
        return self.tarefas

    def get_by_id(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                return tarefa

        return None