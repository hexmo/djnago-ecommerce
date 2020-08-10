from django.urls import path

from . import views

urlpatterns = [
    path('addproduct/', views.add_product, name='add_product'),
    path('manageproduct/', views.manage_product, name='manage_product'),
    path('edit/<int:id>', views.edit_product, name='edit_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
]
