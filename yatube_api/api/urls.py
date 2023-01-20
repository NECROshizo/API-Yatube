from rest_framework import routers
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
    # "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDE1ODkzOCwianRpIjoiM2M4YzhiZTViNGY5NDU1YjkyYzEwNDYxOThiNmIxZmEiLCJ1c2VyX2lkIjozfQ.P3qsjiH01FRSN5l0A7Et8PKTC15VzVfkSKlMNXCeVjs",
    # "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MTU4OTM4LCJqdGkiOiJiOTRlN2UxNDFhZjg0YThmOWJlMjEyNWYyYmIxNjJhYiIsInVzZXJfaWQiOjN9.UbwKkfKkLR-DftZIiamWrbkl8495SJAJ_NpuWHM8o6Q"