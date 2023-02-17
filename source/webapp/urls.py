from django.urls import path

from webapp.views.tasks import add_view, detail_view, TaskDeleteView, TaskUpdateView
from webapp.views.base import index_view

urlpatterns =[
    path("", index_view, name='index'),
    path('task/add', add_view, name='add_task'),
    path('task/<int:pk>', detail_view, name='detail_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update')
]
