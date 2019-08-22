class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

class Medico(Pessoa):
    def __init__(self, nome, idade, telefone, crm):
        super().__init__(nome, idade, telefone, crm)
        self.crm = crm

class Paciente(Pessoa):
    def __init__(self, nome, idade, telefone, enfermidade):
        super().__init__(nome, idade, telefone, enfermidade)
        self.enfermidade = enfermidade

pessoa = Paciente('Naty', '16', '99999999', 'Gripe')
medico = Medico('Karen', '23', '943925792', '1979985')

print(Medico.crm)
print(Paciente.enfermidade)




