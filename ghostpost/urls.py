from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from ghostpost.views import index, author, add_boast, add_roast, add_author, boast, roast

from ghostpost.models import Author, Boast, Roast, User

admin.site.register(Author)
admin.site.register(Boast)
admin.site.register(Roast)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    # path('message/', message),
    # path('author/', views.author, name='author'),
    path('roast/', roast),
    path('boast/', boast),
    path('addauthor/', add_author),
    path('addboast/', add_boast, name='add_boast'),
    path('addroast/', add_roast, name='add_roast'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
