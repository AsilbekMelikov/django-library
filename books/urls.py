from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookDetailApiView, BookUpdateApiView, BookDeleteApiView, \
    BookCreateApiView, BookUpdateDeleteView, BookViewSet

router = SimpleRouter()
router.register("", BookViewSet, basename="books")

urlpatterns = [
    path("", BookListApiView.as_view()),
    path("<int:pk>", BookUpdateDeleteView.as_view()),
    path("create", BookCreateApiView.as_view()),
    # path("<int:pk>/", BookDetailApiView.as_view()),
    path("<int:pk>/update/", BookUpdateApiView.as_view()),
    path("<int:pk>/delete/", BookDeleteApiView.as_view())
]

# urlpatterns = urlpatterns + router.urls
