from django.urls import path
from . import views



app_name = 'faculties'


urlpatterns = [
    path('create/new/faculty/', views.CreateFaculty, name='create_faculty'),

    path('CUS/<faculty_slug>/edit/', views.UpdateFaculty.as_view(), name='update_faculty'),

    path('CUS/all/', views.FacultyList.as_view(), name='faculty_list'),
    path('CUS/<faculty_slug>/departments/', views.FacultyDetail.as_view(), name='faculty_detail'),
    path('CUS/<faculty_slug>/delete', views.FacultyDelete.as_view(), name='delete_faculty'),

    path('CUS/form/upload/images', views.facutyimages, name='gallery_form'),
    path('CUS/gallery/', views.ImageList.as_view(), name='varsity_images'),

]