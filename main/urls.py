from django.conf.urls import url, include
from .views import (Index,
                    Login,
                    Signup,
                    logmeout,
                    Profile,
                    email,
                    activate
                    )

app_name = "main"

urlpatterns = [

    url(r'^$', Index.as_view(), name="index"),
    url(r'^profile$', Profile.as_view(), name='profile'),
    url(r'^login$', Login.as_view(), name="login"),
    url(r'^email$', email, name='email'),
    url(r'^signup$', Signup.as_view(), name="signup"),
    url(r'^activate/(?P<id>[0-9]+)$', activate, name='activate'),
    url(r'^logout$', logmeout, name="logout")
]
