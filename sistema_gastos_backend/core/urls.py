from rest_framework.routes import DefaulRouter
from .view import ProyectosViewSet, GastosViewSet

router = DefaulRouter()
roter.register(r'proyectos', ProyectosViewSet)
router.register(r'gastos', GastosViewSet)

urlpatterns = router.urls