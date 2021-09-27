from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from escola import views as escola_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', escola_views.AlunosViewSet, basename='Alunos')
router.register('cursos', escola_views.CursosViewSet, basename='Cursos')
router.register('matriculas', escola_views.MatriculasViewSet, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', escola_views.ListaMatriculasAlunos.as_view()),
    path('cursos/<int:pk>/matriculas/', escola_views.ListaAlunosMatriculados.as_view()),
]
