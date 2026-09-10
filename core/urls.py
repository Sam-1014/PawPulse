from django.urls import path

from . import views


urlpatterns = [

    # ========================================================
    # PAWPULSE HOME
    # ========================================================

    path(
        '',
        views.home,
        name='home'
    ),


    # ========================================================
    # MY DOGS
    # ========================================================

    path(
        'add-dog/',
        views.add_dog,
        name='add_dog'
    ),

    path(
        'dogs/',
        views.dog_list,
        name='dog_list'
    ),


    # ========================================================
    # VITALITY
    # ========================================================

    path(
        'vitality/',
        views.vitality,
        name='vitality'
    ),

    path(
        'vitality-dashboard/',
        views.vitality_dashboard,
        name='vitality_dashboard'
    ),


    # ========================================================
    # PAWMOOD
    # ========================================================

    path(
        'pawmood/',
        views.pawmood,
        name='pawmood'
    ),

    path(
        'pawmood-dashboard/',
        views.pawmood_dashboard,
        name='pawmood_dashboard'
    ),


    # ========================================================
    # PAWMATCH
    # ========================================================

    path(
        'pawmatch/',
        views.pawmatch,
        name='pawmatch'
    ),


    # ========================================================
    # PAWFIND
    # ========================================================

    path(
        'pawfind/',
        views.pawfind,
        name='pawfind'
    ),

]