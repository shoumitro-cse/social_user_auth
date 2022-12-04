from django.urls import path
from accounts import views


urlpatterns = [
    path('user/is-authenticated/', views.IsAuthenticatedView.as_view(), name='is_authenticated_user'),
    path('user/is-authenticated-or-readonly/', views.IsAuthenticatedOrReadOnlyView.as_view(),
         name='is_authenticated_or_readonly_user'),
    path('user/is-admin-user/', views.IsAdminUserView.as_view(), name='is_admin_user'),
]
