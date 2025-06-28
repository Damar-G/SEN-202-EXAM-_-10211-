from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouters
from employees.views import ManagerViewSet, InternViewSet

router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r 'interns', InternViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apl/', include(router.urls))
    path('api-auth/', include('rest_framework.urls'))
]

