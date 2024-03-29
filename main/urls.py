from . import views
from django.urls import path , include

app_name ='main'

urlpatterns = [
    path('',views.index , name = 'index'),
    path('contact/',views.contact , name = 'contact'),
    path('about/',views.about , name = 'about'),
    path('quote/',views.quote , name = 'quote'),
    path('services/',views.services , name = 'services'),
    path('serviced/',views.serviced , name = 'serviced'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
