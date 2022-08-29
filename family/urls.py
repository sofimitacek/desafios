from django.urls import path
from family.views import list_familia


urlpatterns = [
    path('family', list_familia),
]
