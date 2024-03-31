from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "tubuyakis"

urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.post, name='post'),
    path('view/', views.view, name='view'),
    path('view2/', views.view2, name='view2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)