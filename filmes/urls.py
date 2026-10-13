from rest_framework.routers import DefaultRouter
from .views import GeneroViewSet, FilmeViewSet

router = DefaultRouter()

router.register('generos', GeneroViewSet, basename='genero')
router.register('filmes', FilmeViewSet, basename='filme')

urlpatterns = router.urls