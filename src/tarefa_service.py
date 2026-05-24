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

    def update(self, tarefa_id, novos_dados):
        tarefa = self.get_by_id(tarefa_id)

        if tarefa is None:
            return None

        tarefa["titulo"] = novos_dados["titulo"]
        tarefa["descricao"] = novos_dados["descricao"]
        tarefa["status"] = novos_dados["status"]

        return tarefa

    def delete(self, tarefa_id):
        tarefa = self.get_by_id(tarefa_id)

        if tarefa is None:
            return False

        self.tarefas.remove(tarefa)
        return True