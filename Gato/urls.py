from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from Gato.views import GatoList, GatoCreate, GatoDetail, GatoUpdate, GatoAdopt





urlpatterns = [
    path('list/',GatoList.as_view(), name='gatolist'),
    path('create/', GatoCreate.as_view(), name='creategato'),
    path('<int:pk>/detail/',GatoDetail.as_view(), name='detailgato'),
    path('<int:pk>/update/', GatoUpdate.as_view(), name='updategato'),
    path('<int:pk>/adopt/', GatoAdopt.as_view(), name='adoptgato'),
    
]