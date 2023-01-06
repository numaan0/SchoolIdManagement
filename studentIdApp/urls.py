from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('log_out/',views.log_out,name="log_out"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name='profile'),
    path('editprofile/<role>/<pk>/',views.editprofile,name="editprofile"),
    path('editteacher/<role>/<pk>/',views.editteacher,name="editteacher"),
    path('updateImage/<role>/<pk>/',views.updateImage,name="updateImage"),
]
