from .views import ToDoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ToDoViewSet, basename='todos')
urlpatterns = router.urls
