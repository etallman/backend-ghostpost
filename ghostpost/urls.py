from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

from ghostpost.views import index, BoastSingleView, RoastSingleView, BoastFormView, RoastFormView,add_upvote_boast, add_upvote_roast, add_downvote_boast, add_downvote_roast

from ghostpost.models import Boast, Roast, Vote

admin.site.register(Vote)
admin.site.register(Boast)
admin.site.register(Roast)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    # path('message/', message),
    path('addupvote/<int:boast_id>/', add_upvote_boast),
    path('addupvote/<int:roast_id>/', add_upvote_roast),
    path('adddownvote/<int:boast_id>/', add_downvote_boast),
    path('adddownvote/<int:roast_id>/', add_downvote_roast),
    path('<int:pk>/', RoastSingleView.as_view(), name="roast-detail"), #roast/1
    path('<int:pk>/', BoastSingleView.as_view(), name="boast-detail"), #boast/1    
    path('addboast/', BoastFormView.as_view(), name='add_boast'),
    path('addroast/', RoastFormView.as_view(), name='add_roast'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)