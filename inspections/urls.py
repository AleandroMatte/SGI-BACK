from django.urls import path

from inspections import views

urlpatterns = [
    path("", views.InspectionListCreateView.as_view()),
    path("<pk>/", views.InspectionDetailView.as_view()),
    path("<uuid:inspection_id>/data/", views.InspectionDataListCreate.as_view()),
    path("asset/<uuid:assetId>/", views.InspectionByAssetView.as_view())
]
