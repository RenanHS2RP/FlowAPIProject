from rest_framework import routers
from django.urls import path, include
from FlowAPIApp.views import FlowView

router = routers.DefaultRouter()
router.register(r'', FlowView)

urlpatterns = [
    path('', include(router.urls))
]
