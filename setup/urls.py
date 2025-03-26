from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

#Criando o objeto de rotas e registrando as rotas.
router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas',MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #na rota abaixo estou indicando que será passada a primarykey do estudante(id) para listar as matrículas dele de acordo com a view do segundo paramentro que estamos determinando pelo método as_view() que é uma view. 
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()), 
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]
