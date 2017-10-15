from django.conf.urls import url
from . import views
app_name = 'Devs'
urlpatterns =[
url(r'^$',views.index,name='index'),
url(r'^trustsview/$',views.Indexview.as_view(),name='trusts'),
url(r'^trustsadd/$',views.trustscreate.as_view(),name='trustsadd')

]
