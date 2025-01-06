from django.contrib.auth import views as auth_views
from django.urls import path,include
# import captcha
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup-d/', views.signup, name='signup'),
    path('signup-p/', views.signup1, name='signup1'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs1/', views.create_blogs, name='blogs1'),
    path('signup/', views.choice, name='choice'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('user-logout/',views.user_logout,name="user-logout"),
    path('blogs2/delete/<str:Blog_name>',views.delete_blogs,name="delete_blogs"),
    path('blogs2/', views.your_blogs, name='blogs1'),
    path('displayblog/<str:Blog_name>', views.display_blog, name='display_blog'),
    path('selfassesment/', views.self_assesment, name='self_assesment'),
    path('adhd/', views.adhd, name='adhd'),
    path('ptsd/', views.ptsd, name='ptsd'),
    path('depression/', views.depression, name='depression'),
    path('anxiety/', views.anxiety, name='anxiety'),
    
   
]
