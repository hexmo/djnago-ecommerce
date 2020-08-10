from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('category/<str:category>', views.view_by_category, name='category'),
    path('view/<int:id>', views.view_product_details, name='view_product_details'),
]
