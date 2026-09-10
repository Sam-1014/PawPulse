from django.shortcuts import render, redirect

from .forms import (
    DogForm,
    VitalityForm,
    PawMoodForm,
    PawMatchForm,
    PawFindForm
)

from .models import (
    Dog,
    Vitality,
    PawMood
)


# ============================================================
# PAWPULSE HOME
# ============================================================

def home(request):

    return render(
        request,
        'core/home.html'
    )


# ============================================================
# ADD DOG
# ============================================================

def add_dog(request):

    if request.method == 'POST':

        form = DogForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('dog_list')

    else:

        form = DogForm()

    return render(
        request,
        'core/dogs/dog_form.html',
        {
            'form': form
        }
    )


# ============================================================
# MY DOGS
# ============================================================

def dog_list(request):

    dogs = Dog.objects.all()

    return render(
        request,
        'core/dogs/dog_list.html',
        {
            'dogs': dogs
        }
    )


# ============================================================
# VITALITY — ADD DAILY RECORD
# ============================================================

def vitality(request):

    if request.method == 'POST':

        form = VitalityForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'vitality_dashboard'
            )

    else:

        form = VitalityForm()

    return render(
        request,
        'core/vitality/vitality_form.html',
        {
            'form': form
        }
    )


# ============================================================
# VITALITY DASHBOARD
# ============================================================

def vitality_dashboard(request):

    records = Vitality.objects.select_related(
        'dog'
    ).order_by('-date')

    return render(
        request,
        'core/vitality/vitality_dashboard.html',
        {
            'records': records
        }
    )


# ============================================================
# PAWMOOD — ADD ENTRY
# ============================================================

def pawmood(request):

    if request.method == 'POST':

        form = PawMoodForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'pawmood_dashboard'
            )

    else:

        form = PawMoodForm()

    return render(
        request,
        'core/pawmood/pawmood_form.html',
        {
            'form': form
        }
    )


# ============================================================
# PAWMOOD — INTELLIGENT DASHBOARD
# ============================================================

def pawmood_dashboard(request):

    records = PawMood.objects.select_related(
        'dog'
    ).order_by('-date')

    observations = []

    dogs = Dog.objects.all()

    for dog in dogs:

        dog_records = list(
            PawMood.objects.filter(
                dog=dog
            ).order_by('-date')
        )

        if len(dog_records) >= 2:

            recent = dog_records[0]

            previous = dog_records[1]

            energy_change = (
                recent.energy -
                previous.energy
            )

            play_change = (
                recent.playfulness -
                previous.playfulness
            )

            appetite_change = (
                recent.appetite -
                previous.appetite
            )

            # =================================================
            # ENERGY
            # =================================================

            if energy_change <= -2:

                observations.append(
                    f"📉 {dog.name}'s energy has decreased "
                    f"compared with the previous entry."
                )

            elif energy_change >= 2:

                observations.append(
                    f"⚡ {dog.name}'s energy has increased "
                    f"compared with the previous entry."
                )

            # =================================================
            # PLAYFULNESS
            # =================================================

            if play_change <= -2:

                observations.append(
                    f"🎾 {dog.name}'s playfulness has "
                    f"decreased recently."
                )

            elif play_change >= 2:

                observations.append(
                    f"🎾 {dog.name}'s playfulness has "
                    f"increased recently."
                )

            # =================================================
            # APPETITE
            # =================================================

            if appetite_change <= -2:

                observations.append(
                    f"🍖 {dog.name}'s appetite is lower "
                    f"than the previous entry."
                )

            elif appetite_change >= 2:

                observations.append(
                    f"🍖 {dog.name}'s appetite is higher "
                    f"than the previous entry."
                )

            # =================================================
            # STABILITY
            # =================================================

            if (
                energy_change == 0
                and
                play_change == 0
                and
                appetite_change == 0
            ):

                observations.append(
                    f"💚 {dog.name}'s recent behaviour "
                    f"indicators are relatively stable."
                )

    return render(
        request,
        'core/pawmood/pawmood_dashboard.html',
        {
            'records': records,
            'observations': observations,
        }
    )


# ============================================================
# PAWMATCH
# ============================================================

def pawmatch(request):

    results = None

    if request.method == 'POST':

        form = PawMatchForm(request.POST)

        if form.is_valid():

            match = form.save()

            results = match.calculate_matches()

    else:

        form = PawMatchForm()

    return render(
        request,
        'core/pawmatch/pawmatch.html',
        {
            'form': form,
            'results': results,
        }
    )


# ============================================================
# PAWFIND — REPORT + MATCH
# ============================================================

def pawfind(request):

    results = None

    if request.method == 'POST':

        form = PawFindForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            report = form.save()

            results = report.calculate_matches()

    else:

        form = PawFindForm()

    return render(
        request,
        'core/pawfind/pawfind.html',
        {
            'form': form,
            'results': results,
        }
    )