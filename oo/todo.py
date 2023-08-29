class Categoria():
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
    
    def pendente(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
    
    def __str__(self):
        return f"{self.nome} ({len(self.pendente())}) tarefa(s) pendente(s)"

class Tarefa():
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
    
    def concluir(self):
        self.feito = True
    
    def __str__(self):
        return self.descricao + (" (Concluido)" if self.feito else "")

def main():
    
    casa = Categoria("Tarefas de casa")
    casa.add("Lavar roupa")
    casa.add("Tirar coco do cachorro")
    
    casa.procurar("Lavar roupa").concluir()
    print(casa)

    for tarefa_casa in casa.tarefas:
        print(f"- {tarefa_casa}")
        
if __name__ == "__main__":
    main() 