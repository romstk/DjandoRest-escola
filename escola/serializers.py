from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estudante
        fields= ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

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
