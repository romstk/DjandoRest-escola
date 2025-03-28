from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from escola.models import Estudante, Curso, Matricula
from rest_framework import viewsets, generics


#Aqui estamos criando as classes de viewsets para as models Estudante, Curso e Matricula.
#Viewsets são classes que fornecem uma interface entre as views e os dados da aplicação.
# As viewset Estudante, Curso e Matricua são classes que herdam de viewsets.ModelViewSet, que é uma classe que já implementa todos os métodos CRUD, ou seja, não precisamos implementar os métodos como list, create, update, destroy, etc.
# A única coisa que precisamos fazer é definir a queryset e o serializer_class.
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

#Esta classe de view é diferente das anteriores implementadas, pois nesta agora não vamos mais capturar todos os objetos da model, mas sim dados específicos, por isso vamos precisar usar recursos de filtro. Estamos usando generics ao invés de viewset pois estamos usando este recurso de ListViewAPI pois precisamos somente realizer GET para listar dados, não preciamos dos recursos de viewset para demais operações CRUD.
#Para as generiscs.ListAPIView precisamos implementar a função get_queryset para nossas views
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class= ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class= ListaMatriculasCursoSerializer