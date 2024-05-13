from django.urls import path
from .views import HomePageView, SingleProductView

app_name = 'store'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<int:pk>/', SingleProductView.as_view(), name='product'),
    path('product/<int:pk>/comment/', SingleProductView.as_view(), name='submit_comment'),  # URL для отправки комментариев
]

