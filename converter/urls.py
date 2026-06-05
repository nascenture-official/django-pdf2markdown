from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path('preview/<int:doc_id>/', views.preview_view, name='preview'),
    path('delete/<int:doc_id>/', views.delete_document_view, name='delete_document'),
    path('bulk_delete/', views.bulk_delete_documents_view, name='bulk_delete'),
]
