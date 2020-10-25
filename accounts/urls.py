from django.urls import path

from .views import \
    ListUsersView, \
    RetrieveOrUpdateUserView


urlpatterns = [
    path('', ListUsersView.as_view()),
    path('<int:pk>/', RetrieveOrUpdateUserView.as_view()),
]
