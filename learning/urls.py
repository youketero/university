from django.conf.urls import url

import learning
from learning import views

urlpatterns = [
    url(r'^edu_plan/$', learning.views.edu_plans, name="edu_plan"),
    url(r'^education/$', learning.views.education, name='education'),
    url(r'^science_learning/$', learning.views.science_learning, name="science_learning"),
    url(r'^phd_learning/$', learning.views.phd_learning, name="phd_learning"),
]