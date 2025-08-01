from django.urls import path, include

from discipline.views.DisciplineListView import DisciplinesView
from discipline.views.DisciplineDetailsView import DisciplineDetailsView

urlpatterns = [
    path("", DisciplinesView.as_view()),
    path("<uuid:pk>", DisciplineDetailsView.as_view())
]