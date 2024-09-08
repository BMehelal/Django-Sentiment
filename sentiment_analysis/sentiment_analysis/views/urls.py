from django.urls import path
from . import youtubeSentiment

urlpatterns = [
    path('youtubeSentiment/<str:video_id>/',
         youtubeSentiment.youtubeSentiment, name="youtube_sentiment")
]
