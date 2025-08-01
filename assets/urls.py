from django.urls import path

from assets.views import AssetTypeView, AssetView, AssetTypeDetailsView, AssetDetailsView

urlpatterns = [
    path('', AssetView.as_view()),
    path('<pk>', AssetDetailsView.as_view()),
    path('types/', AssetTypeView.as_view()),
    path('types/<pk>', AssetTypeDetailsView.as_view()),
]