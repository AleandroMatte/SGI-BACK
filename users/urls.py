from django.urls import include, path
from knox import views as knox_views
from users.views.group_views import GroupDetailsViews, GroupViews
from users.views.login_views import LoginView
from rest_framework import routers
from users.views.permission_views import PermissionListView
from users.views.user_views import UserViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path(r'groups/', GroupViews.as_view()),
    path(r'groups/<pk>', GroupDetailsViews.as_view()),
    path(r'permissions/', PermissionListView.as_view()),
    path('', include(router.urls))
]
