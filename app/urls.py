from django.urls import path
from .views import UniversitetListView, MalumotListView

urlpatterns = [
    path('', UniversitetListView.as_view(), name='home'),  # Asosiy sahifa sifatida universitetlar ro'yxati
    path('posts/', UniversitetListView.as_view(), name='universitet_list'),
    path('malumot/', MalumotListView.as_view(), name='malumot_list'),
]

"""
python -m venv venv
venv/Scripts/activate
"""