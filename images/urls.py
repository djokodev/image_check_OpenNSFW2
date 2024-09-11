from django.urls import path
from images.views import home, upload_image

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_image, name='upload_image'),
]
