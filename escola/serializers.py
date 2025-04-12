from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import celular_invalido, cpf_invalido, nome_invalido
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estudante
        fields= ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
    
    # O método validate é um método padrão do Django Rest Framework que permite validar os dados de entrada antes de serem salvos no banco de dados.
    # Ao tentar serializar os campos , o método validate  é chamado automaticamente para validar os campos. 
    # ele retorna a variável de dados sejam válidos, ou lança uma exceção de validação caso um dos dados não seja válido. Se for lançar uma exceção, vai buscar o dicionário usando como chave o nome do campo e lança a mensagem correspondente. 
    def validate(self, dados):    
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF digitado não é válido'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve conter 13 dígitos. Use o padrão XX XXXXX-XXXX'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras'})   
        
        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Matricula
        fields = '__all__'

# Serializer que lista as matriculas realizadas por um estudante, 
# Para este serializador usamos dois tipos de serializadores: 
# O SerializerMethodField para obter o display/descrição do campo período, visto que período é gravado apenas a primeira letra como código para cada período a ser cadastrado, que é obtido através de um método dentro da própria classe que é implementado para este fim 
# O ReadOnlyField para obter o campo curso, que precimos buscar sua descrição, então para este serializer buscamos informando como parâmetro o source='curso.descricao'para trazer a descrição para a variável curso 
# 
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta: 
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
# Este serializer traz a lista de Matriculas por curso, sendo que vamos listar somente os nomes dos alunos matriculados. 
# 
# #
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula    
        fields = ['estudante_nome']

# Serializer para versão 2. Esse novo endpoint deverá conter apenas os campos de ‘id',  ‘nome’, ‘email’ e ‘celular’ dos Estudantes
class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email', 'celular']