from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from Perro.views import PerroList, PerroCreate, PerroDetail, PerroUpdate, PerroAdopt





urlpatterns = [
    path('list/',PerroList.as_view(), name='perrolist'),
    path('create/', PerroCreate.as_view(), name='createperro'),
    path('<int:pk>/detail/',PerroDetail.as_view(), name='detailperro'),
    path('<int:pk>/update/', PerroUpdate.as_view(), name='updateperro'),
    path('<int:pk>/adopt/', PerroAdopt.as_view(), name='adoptperro'),
    
]