from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
#from django.conf.urls import url
app_name = "departments"


urlpatterns = [
    path('create/new/', views.CreateDepartment , name='create_department'),
    path('CUS/all/departments/', views.AllDepartments.as_view(), name='all_departments'),

    path('CUS/<faculty_slug>/edit/<department_slug>/', views.UpdateDepartment.as_view(), name='update_department'),
    path('CUS/<faculty_slug>/<department_slug>/', views.DepartmentDetail.as_view(), name='department_detail'),

    path('CUS/<faculty_slug>/department/<department_slug>/delete', views.DepartmentDelete.as_view(), name='delete_department'),

    path('<department_slug>/students/', views.DepartmentStudents.as_view(), name='department_students' ),
    path('<department_slug>/teachers/', views.DepartmentTeachers.as_view(), name='department_teachers' ),

]