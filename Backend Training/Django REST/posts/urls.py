from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    post_lists,
    post_detail,
    PostListCreateView,
    POSTRetrieveUpdateDelete,
    PostListCreateGenericView,
    PostRetrieveUpdateDeleteGenericView,
    PostViewSet,
    PostModelViewSet,
)

router = DefaultRouter()
router.register("", PostModelViewSet, basename="posts")
# router.register("", PostViewSet, basename="posts")

urlpatterns = [
    # ViewSets
    path("", include(router.urls)),
    # Generic Class Base View
    # path("", PostListCreateGenericView.as_view(), name="post_lists"),
    # path(
    #     "<int:pk>/", PostRetrieveUpdateDeleteGenericView.as_view(), name="post_detail"
    # ),
    # Class Base View
    # path("", PostListCreateView.as_view(), name="post_lists"),
    # path("<int:pk>", POSTRetrieveUpdateDelete.as_view(), name="post_detail"),
    # Function Base View
    # path("", post_lists, name="post_lists"),
    # path("<int:pk>/", post_detail, name="post_detail"),
]
