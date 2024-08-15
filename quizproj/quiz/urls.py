
from django.urls import path

from quiz import views


urlpatterns = [
    path('',views.index,name='home'),
    path('quiz/',views.quizPage,name='quizPage'),
    path('score/',views.quizScore,name='quizScore'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutPage,name='logoutPage'),
]
