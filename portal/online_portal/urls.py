from django.conf.urls import url
from online_portal.views import login_go,home_page,sign_up

urlpatterns=[
    url('^login/$',login_go,name='login_go'),
    url('^homepage/$',home_page,name='home_page'),
    url('^signup/$',sign_up,name='sign_up')

]