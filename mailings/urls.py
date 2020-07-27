from django.urls import path
from mailings.views import *

urlpatterns = [
    path('add-to-common-list/', views.add_to_common_list_view),
]
