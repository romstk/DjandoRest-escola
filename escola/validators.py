import re
from validate_docbr import CPF
# O validate_docbr é uma biblioteca que valida documentos brasileiros, como CPF, CNPJ, RG, etc.
def cpf_invalido(numero_cpf):
    cpf = CPF()
    # O CPF é um objeto da classe CPF, que possui o método validate que valida o CPF.

    return not cpf.validate(numero_cpf) # O método validate do cpf retorna True se o CPF for válido e False se não for. Então, se o CPF for inválido, o retorno será True. Assim podemos usar esta função para validar o CPF no método validate do serializer.

def celular_invalido(celular):
     #padrão de telefone (XX)XXXXX-XXXX
     #vamos usar regex para implementar a validação
     modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
     resposta = re.findall(modelo, celular)
     # Se a resposta for vazia, significa que não encontrou o padrão, então o celular é inválido. Vazio é igual a False, então podemos usar o not para inverter o resultado, ou seja se não encontrou resposta sendo false o meu return vai ser = not false = true - True = celular invalido.
     return not resposta
            
def nome_invalido(nome):            
    return not (nome).isalpha() # Verifica se o nome contém apenas letras e se não tiver apenas letras retornará True. Assim podemos usar esta função para validar o nome no método validate do serializer.
