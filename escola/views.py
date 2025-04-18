from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2
from escola.models import Estudante, Curso, Matricula
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.throttling import AnonRateThrottle



#Aqui estamos criando as classes de viewsets para as models Estudante, Curso e Matricula.
#Viewsets são classes que fornecem uma interface entre as views e os dados da aplicação.
# As viewset Estudante, Curso e Matricua são classes que herdam de viewsets.ModelViewSet, que é uma classe que já implementa todos os métodos CRUD, ou seja, não precisamos implementar os métodos como list, create, update, destroy, etc.
# A única coisa que precisamos fazer é definir a queryset e o serializer_class.
class EstudanteViewSet(viewsets.ModelViewSet):
    """"
    Descrição da View:
    - Viewset para a CRUD de Estudante
    - Permite listar, criar, atualizar e excluir estudantes.
    - Permite filtrar estudantes por nome e cpf.
    Parâmetros:
    - nome (str): O nome do estudante. Deve ser uma string.
    - cpf (str): O CPF do estudante. Deve ser uma string.
    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.

    """
    
    
    queryset = Estudante.objects.all().order_by('id')
    
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
    filterset_fields = ['nome', 'cpf']
    #esta função é responsável por definir qual serializer será utilizado de acordo com a versão da API que está sendo utilizada.
    # A versão da API é definida na URL, por exemplo: /api/v1/estudantes/ ou /api/v2/estudantes/
    # A função get_serializer_class verifica a versão da API e retorna o serializer correspondente.
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer
    



class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    # ao definir a variável trottle_classes, estamos definindo que a view MatriculaViewSet vai usar as classes de limite de requisições AnonRateThrottle padrão de settings e a MatriculaAnonRateThrottle definida na classe que sobrescrevemos a padrão. 
    throttle_classes = [AnonRateThrottle, MatriculaAnonRateThrottle]

    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    # Aqui estamos definindo os métodos que a view MatriculaViewSet vai aceitar, ou seja, vamos permitir que o usuário faça requisições GET, POST.
    http_method_names = ['get', 'post']
    
#Esta classe de view é diferente das anteriores implementadas, pois nesta agora não vamos mais capturar todos os objetos da model, mas sim dados específicos, por isso vamos precisar usar recursos de filtro. Estamos usando generics ao invés de viewset pois estamos usando este recurso de ListViewAPI pois precisamos somente realizer GET para listar dados, não preciamos dos recursos de viewset para demais operações CRUD.
#Para as generiscs.ListAPIView precisamos implementar a função get_queryset para nossas views
class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk(int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class= ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class= ListaMatriculasCursoSerializer