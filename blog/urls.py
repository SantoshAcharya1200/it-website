from django.urls import path

from . import views
from .apiviews import PostList,PostDetail






urlpatterns = [



    path('', views.PostList.as_view(), name='home'),
    path("post/", PostList.as_view(), name="post_list"),
    path("post/<int:pk>",PostDetail.as_view(),name="post_detail"),
    path("search/", views.SearchResultView.as_view(), name="search_results"),
    path('management', views.MgmtPostList.as_view(), name='management'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('management/<slug:slug>/', views.mgmt_post_detail, name='mgmt_post_detail'),





]