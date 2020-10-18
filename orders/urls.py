from django.urls import path

from .views import OrderListView, CurrencyRateListView

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),

]
