from django.conf.urls import url

from . import views
app_name = 'Devs'
urlpatterns =[
url(r'^$',views.home,name='home'),
url(r'^developers/$',views.index,name='developers'),
url(r'^trustsview/$',views.Indexview.as_view(),name='trusts'),
url(r'^trustsadd/$',views.trustscreate.as_view(),name='trustsadd'),
url(r'^register/$',views.register,name='register'),
url(r'^profile/$',views.profile,name='profile'),
url(r'^volunters/$',views.voluntersview.as_view(),name='volunters'),
url(r'^postcreate/$',views.postcreate.as_view(),name='postcreate'),
url(r'^posts/$',views.posts.as_view(),name='posts'),
url(r'^posts/(?P<post_id>[0-9]+)/$',views.postdetail,name='postdetail'),
url(r'^posts/(?P<post_id>[0-9]+)/comments/$',views.postdetail,name='comment'),
url(r'^posts/(?P<post_id>[0-9]+)/comments/createcomment$',views.createcomment,name='createcomment'),
]
