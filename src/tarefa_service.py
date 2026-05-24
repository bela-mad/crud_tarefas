class TarefaService:
    """
    Serviço responsável por gerenciar tarefas de estudo.

    Essa classe permite criar, listar, buscar, atualizar e remover tarefas,
    representando as operações básicas de um CRUD.
    """

    def __init__(self):
        """
        Inicializa a lista de tarefas e o controle de IDs.
        """
        self.tarefas = []
        self.proximo_id = 1

    def create(self, dados):
        """
        Create - Cria uma nova tarefa de estudo.
        """
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
        """
        Read - Busca todas as tarefas cadastradas.
        """
        return self.tarefas

    def get_by_id(self, tarefa_id):
        """
        Read - Busca uma tarefa pelo ID.
        """
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                return tarefa

        return None

    def update(self, tarefa_id, novos_dados):
        """
        Update - Atualiza os dados de uma tarefa existente.
        """
        tarefa = self.get_by_id(tarefa_id)

        if tarefa is None:
            return None

        tarefa["titulo"] = novos_dados["titulo"]
        tarefa["descricao"] = novos_dados["descricao"]
        tarefa["status"] = novos_dados["status"]

        return tarefa

    def delete(self, tarefa_id):
        """
        Delete - Remove uma tarefa pelo ID.
        """
        tarefa = self.get_by_id(tarefa_id)

        if tarefa is None:
            return False

        self.tarefas.remove(tarefa)
        return True