from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name = "register"),
    path("review", views.review, name = "review"),
    path("do", views.do, name='do'),
    path("dont", views.dont, name='dont'),
    path("comment", views.comment, name='comment'),
    path("reviewcard", views.reviewcard, name='reviewcard'),
    path("upvote", views.upvote, name="upvote"),
    path("downvote", views.downvote, name="downvote"),
    path("search", views.search, name="search"),
    path("searchuser", views.searchuser, name="searchuser"),
    path("user", views.user, name="user"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
