from django.urls import path
from .views import user_list, user_detail, csv_database_write

urlpatterns = [

    path('users/', user_list),
    path('user/<int:pk>', user_detail),
    path('export/csv-database-write/', csv_database_write, name='csv_database_write'),

]
