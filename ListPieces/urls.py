from django.urls import re_path as url
from ListPieces import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    url(r'^List_OF_Pieces$',views.ListPiecesApi),
    url(r'^List_OF_Pieces/([0-9]+)$',views.ListPiecesApi),
    url(r'^Pieces/(?P<pk>[0-9]+)$', views.list_detail),
    url(r'^Piéce/SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
