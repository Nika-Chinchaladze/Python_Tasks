from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_month_list, name="index_page"),
    path("<int:month>", views.month_number_handler),
    path("<str:month>", views.month_handle, name="month_handle_page")
]
