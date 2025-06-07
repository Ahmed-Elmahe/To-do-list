from django.urls import path
from .views import index, about, contact, signup, login_view, logout_view, create_task, update_task, delete_task, delete_completed_tasks


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('clear/', delete_completed_tasks, name='delete_completed_tasks'),
]

