from django.urls import path
from conduit import views


urlpatterns=[
    path('',views.CreateArticle.as_view(),name='xyz'),
    path('<int:pk>/',views.CreateArticle.as_view(),name='xyz'),
    path('cbv/<int:pk>/',views.CreateArticleView.as_view()),
    path('cbv/crud/<int:pk>/',views.CrudView.as_view())

]