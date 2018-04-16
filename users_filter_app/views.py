from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.http import Http404,JsonResponse
import time
from .models import *
from django.contrib.auth.decorators import login_required


# https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html

from .filters import UserFilter

@login_required(login_url="/login/")
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'index.html', {'filter': user_filter})

