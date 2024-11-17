from django.urls import path

from students.views import IndexView, StudentDetailView, StudentsListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('students/', StudentsListView.as_view(), name="students"),
    path('students/<int:pk>/', StudentDetailView.as_view(), name="student_details"),
]
