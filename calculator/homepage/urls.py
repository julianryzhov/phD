from django.urls import path

from . import views

urlpatterns = [
    # Если вызван URL без относительного адреса (шаблон — пустые кавычки),
    # то вызывается view-функция index() из файла views.py
    path('', views.index, name='home'),
    path('process_data_ET/', views.process_data_ET, name='process_data_ET'),
    path('ET/', views.ET, name='ET'),
    path('OPU_plasma/', views.OPU_plasma, name='OPU_plasma'),
    path('process_data_OPU_plasma/', views.process_data_OPU_plasma, name='process_data_OPU_plasma'),
    path('OPU_ff/', views.OPU_ff, name='OPU_ff'),
    path('process_data_OPU_ff/', views.process_data_OPU_ff, name='process_data_OPU_ff')
]
