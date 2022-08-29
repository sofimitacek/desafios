from django.urls import path
from family.views import template_1


urlpatterns = [
    path('heroes', template_1),
]
