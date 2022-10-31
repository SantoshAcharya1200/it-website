from django.urls import path

from . import views





urlpatterns = [



    path('', views.PostList.as_view(), name='home'),
    path("search/", views.SearchResultView.as_view(), name="search_results"),
    path('management', views.MgmtPostList.as_view(), name='management'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('management/<slug:slug>/', views.mgmt_post_detail, name='mgmt_post_detail'),





]