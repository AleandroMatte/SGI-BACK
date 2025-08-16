from django.urls import path

from inspections.views import InspectionByAssetView, InspectionDetailView, InspectionListCreateView

urlpatterns = [
    path("", InspectionListCreateView.as_view()),
    path("<pk>/", InspectionDetailView.as_view()),
    path("asset/<uuid:assetId>/", InspectionByAssetView.as_view())
]
