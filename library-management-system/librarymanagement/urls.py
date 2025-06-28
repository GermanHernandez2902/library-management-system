from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from library import views
from library.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Página principal
    path('', views.home_view, name='home'),

    # Login / Logout
    path('logout/', custom_logout, name='logout'),
    path('adminlogin/', LoginView.as_view(template_name='library/adminlogin.html'), name='adminlogin'),
    path('studentlogin/', LoginView.as_view(template_name='library/studentlogin.html'), name='studentlogin'),

    # Click routes
    path('adminclick/', views.adminclick_view, name='adminclick'),
    path('studentclick/', views.studentclick_view, name='studentclick'),

    # Registro
    path('adminsignup/', views.adminsignup_view, name='adminsignup'),
    path('studentsignup/', views.studentsignup_view, name='studentsignup'),

    # Redirección después del login
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),

    # Gestión de libros
    path('addbook/', views.addbook_view, name='addbook'),
    path('viewbook/', views.viewbook_view, name='viewbook'),
    path('issuebook/', views.issuebook_view, name='issuebook'),
    path('viewissuedbook/', views.viewissuedbook_view, name='viewissuedbook'),
    path('viewissuedbookbystudent/', views.viewissuedbookbystudent, name='viewissuedbookbystudent'),

    # Estudiantes
    path('viewstudent/', views.viewstudent_view, name='viewstudent'),

    # Páginas informativas
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('contactus/', views.contactus_view, name='contactus'),
]
