
from django.urls import path
from .views import (TagList,
                    FoodList,
                    GoodList,
                    NewsList,
                    AboutList,
                    AuthorList,
                    CommentList,
                    ServicesList,
                    LaveCommentList,
                    CategoryList,
                    OpenHoursList,
                    FoodDetail)

urlpatterns = [
    path('tags/', TagList.as_view(), name='tag'),
    path('foods/', FoodList.as_view(), name='food'),
    path('foods/<int:pk>/', FoodDetail.as_view(), name='detail'),
    path('goods/', GoodList.as_view(), name='good'),
    path('news/', NewsList.as_view(), name='news'),
    path('about/', AboutList.as_view(), name='about'),
    path('author/', AuthorList.as_view(), name='author'),
    path('comments/', CommentList.as_view(), name='comment'),
    path('services/', ServicesList.as_view(), name='services'),
    path('lavecomments/', LaveCommentList.as_view(), name='lavecomment'),
    path('category/', CategoryList.as_view(), name='category'),
    path('openhours/', OpenHoursList.as_view()),

]

