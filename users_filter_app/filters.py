from django import forms
from django.contrib.auth.models import User, Group
import django_filters

class UserFilter(django_filters.FilterSet):
    skills = django_filters.CharFilter(name ='skills',lookup_expr='icontains')
    current_location = django_filters.CharFilter(name='current_location', lookup_expr='icontains')
    ctc = django_filters.CharFilter(name='ctc',lookup_expr='icontains')
    preferred_location = django_filters.CharFilter(name='preferred_location',lookup_expr='icontains')
    current_employer = django_filters.CharFilter(name='current_employer',lookup_expr='icontains')
    current_designation = django_filters.CharFilter(name='current_designation',lookup_expr='icontains')
    work_exp = django_filters.CharFilter(name='work_exp',lookup_expr='icontains')
    UG_Course = django_filters.CharFilter(name='UG_Course',lookup_expr='icontains')
    PG_Course = django_filters.CharFilter(name='PG_Course',lookup_expr='icontains')
    UG_Passing_Year = django_filters.CharFilter(name='UG_Passing_Year',lookup_expr='icontains')
    PG_Passing_Year = django_filters.CharFilter(name='PG_Passing_Year',lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['skills', 'current_location','ctc','preferred_location','current_employer','current_designation','work_exp','UG_Course','PG_Course','UG_Passing_Year','PG_Passing_Year']