class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def sacar(self, valor_retirado):
        self.valor_retirado = valor_retirado
        # se o saque for maior do que o saldo, raise error
        if valor_retirado > self.balance:
            raise "Value error"
        else:
            self.balance -= valor_retirado
        
        return f"{self.name} has {self.balance}"
    
    def add_dinheiro(self, valor_entrada):
        self.balance += valor_entrada
        return f"{self.name} has {self.balance}"
    
    def check(self, outro_usuario, pagamento):
        self.outro_usuario = outro_usuario
        self.pagamento = pagamento
        
        if pagamento > outro_usuario.balance:
            raise  "Impossivel concluir o pagamento"
        elif outro_usuario.checking_account == False:
            raise "Value error"
        else:
            self.balance += pagamento
            outro_usuario.balance -= pagamento
        
        return f"{self.name} has {self.balance} and {outro_usuario.name} has {outro_usuario.balance}"
            
            
            
hugo = User("Hugo", 100, True)
joao = User("Joao", 100, False)

print(hugo.sacar(10))
print(joao.check(hugo, 12))

joao.checking_account = True
print(hugo.check(joao, 80))

print(joao.add_dinheiro(200))