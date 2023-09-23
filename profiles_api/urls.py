from django.urls import path,include

from rest_framework.routers import DefaultRouter

from profiles_api import views


# The Way you register the viewset with a URL is slighlty different from how you register the API View

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
    
]
