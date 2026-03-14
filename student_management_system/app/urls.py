from django.urls import path
from . import views

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('export-students/', views.export_students, name='export_students'),

]