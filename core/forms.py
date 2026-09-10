from django import forms

from .models import (
    Dog,
    Vitality,
    PawMood,
    PawMatch,
    PawFind
)


# ============================================================
# DOG PROFILE FORM
# ============================================================

class DogForm(forms.ModelForm):

    class Meta:

        model = Dog

        fields = [
            'name',
            'breed',
            'age',
            'gender',
            'color',
            'weight',
            'photo',
            'adoption_date',
        ]


# ============================================================
# VITALITY FORM
# ============================================================

class VitalityForm(forms.ModelForm):

    class Meta:

        model = Vitality

        fields = [
            'dog',
            'date',
            'meals',
            'water',
            'walk_minutes',
            'sleep_hours',
            'energy',
            'play_minutes',
            'mood',
        ]

        widgets = {

            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'mood': forms.TextInput(
                attrs={
                    'placeholder':
                    'Happy, Calm, Playful...'
                }
            ),

        }


# ============================================================
# PAWMOOD FORM
# ============================================================

class PawMoodForm(forms.ModelForm):

    class Meta:

        model = PawMood

        fields = [
            'dog',
            'date',
            'energy',
            'appetite',
            'playfulness',
            'sleep_hours',
            'mood',
            'notes',
        ]

        widgets = {

            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'mood': forms.TextInput(
                attrs={
                    'placeholder':
                    'Happy, Calm, Excited, Quiet...'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'placeholder':
                    'Write about your dog’s behaviour today...',
                    'rows': 4
                }
            ),

        }


# ============================================================
# PAWMATCH FORM
# ============================================================

class PawMatchForm(forms.ModelForm):

    class Meta:

        model = PawMatch

        fields = [
            'preferred_size',
            'activity_level',
            'living_situation',
            'walking_time',
            'first_time_owner',
        ]

        widgets = {

            'preferred_size': forms.Select(
                choices=[
                    ('small', 'Small'),
                    ('medium', 'Medium'),
                    ('large', 'Large'),
                ]
            ),

            'activity_level': forms.Select(
                choices=[
                    ('low', 'Low'),
                    ('medium', 'Medium'),
                    ('high', 'High'),
                ]
            ),

            'living_situation': forms.Select(
                choices=[
                    ('apartment', 'Apartment'),
                    ('house', 'House'),
                ]
            ),

            'walking_time': forms.NumberInput(
                attrs={
                    'placeholder':
                    'Minutes per day',
                    'min': 0
                }
            ),

        }


# ============================================================
# PAWFIND FORM
# ============================================================

class PawFindForm(forms.ModelForm):

    class Meta:

        model = PawFind

        fields = [
            'report_type',
            'dog_name',
            'breed',
            'color',
            'size',
            'location',
            'date',
            'description',
            'photo',
        ]

        widgets = {

            'report_type': forms.Select(
                choices=[
                    ('lost', 'I Lost a Dog'),
                    ('found', 'I Found a Dog'),
                ]
            ),

            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'dog_name': forms.TextInput(
                attrs={
                    'placeholder':
                    'Dog name (optional)'
                }
            ),

            'breed': forms.TextInput(
                attrs={
                    'placeholder':
                    'e.g. Labrador Retriever'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'placeholder':
                    'e.g. Golden, Black, White'
                }
            ),

            'size': forms.Select(
                choices=[
                    ('small', 'Small'),
                    ('medium', 'Medium'),
                    ('large', 'Large'),
                ]
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder':
                    'Where was the dog lost/found?'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder':
                    'Describe the dog and any identifying features...',
                    'rows': 4
                }
            ),

        }