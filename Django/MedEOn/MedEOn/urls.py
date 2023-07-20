from django.contrib import admin
from django.urls import path
from Hospital import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('patient/', views.patient_view,name='patient'),
    path('', views.home,name='home'),
    path('opd', views.opd,name='opd'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('login', views.login_view,name='login'),
    path('logout', views.Logout,name='logout'),
    path('dashboard', views.patient_list,name='dashboard'),
    path('search',views.search, name='search'),
    path('appointment',views.appoint, name='appoint'),
    path('chuck_norris_joke',views.chuck_norris_joke, name='chuck'),
    # path('chuck-norris-joke/', views.chuck_norris_joke, name='chuck'),





    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
