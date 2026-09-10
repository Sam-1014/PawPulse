from django.db import models


# ============================================================
# PAWPULSE — DOG PROFILE
# ============================================================

class Dog(models.Model):

    name = models.CharField(
        max_length=100
    )

    breed = models.CharField(
        max_length=100
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=20,
        blank=True
    )

    color = models.CharField(
        max_length=50,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    photo = models.ImageField(
        upload_to='dogs/',
        blank=True,
        null=True
    )

    adoption_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# ============================================================
# VITALITY — DAILY DOG WELLNESS
# ============================================================

class Vitality(models.Model):

    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    meals = models.PositiveIntegerField(
        default=0
    )

    water = models.FloatField(
        default=0
    )

    walk_minutes = models.PositiveIntegerField(
        default=0
    )

    sleep_hours = models.FloatField(
        default=0
    )

    energy = models.PositiveIntegerField(
        default=5
    )

    play_minutes = models.PositiveIntegerField(
        default=0
    )

    mood = models.CharField(
        max_length=30,
        blank=True
    )

    def calculate_score(self):

        score = 0

        score += (self.energy / 10) * 25

        score += min(
            self.walk_minutes / 60,
            1
        ) * 20

        score += min(
            self.sleep_hours / 10,
            1
        ) * 20

        score += min(
            self.play_minutes / 60,
            1
        ) * 15

        score += min(
            self.meals / 3,
            1
        ) * 10

        score += min(
            self.water / 2.5,
            1
        ) * 10

        return round(score)

    def __str__(self):

        return f"{self.dog.name} - {self.date}"


# ============================================================
# PAWMOOD — BEHAVIOUR JOURNAL
# ============================================================

class PawMood(models.Model):

    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    energy = models.PositiveIntegerField(
        default=5
    )

    appetite = models.PositiveIntegerField(
        default=5
    )

    playfulness = models.PositiveIntegerField(
        default=5
    )

    sleep_hours = models.FloatField(
        default=0
    )

    mood = models.CharField(
        max_length=30
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):

        return f"{self.dog.name} - {self.date}"


# ============================================================
# PAWMATCH — DOG BREED COMPATIBILITY
# ============================================================

class PawMatch(models.Model):

    preferred_size = models.CharField(
        max_length=30
    )

    activity_level = models.CharField(
        max_length=30
    )

    living_situation = models.CharField(
        max_length=30
    )

    walking_time = models.PositiveIntegerField(
        default=0
    )

    first_time_owner = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def calculate_matches(self):

        breeds = {

            'Labrador Retriever': {
                'size': 'large',
                'activity': 'high',
                'living': 'house',
                'walking': 60,
                'beginner': True
            },

            'Golden Retriever': {
                'size': 'large',
                'activity': 'high',
                'living': 'house',
                'walking': 60,
                'beginner': True
            },

            'Beagle': {
                'size': 'medium',
                'activity': 'medium',
                'living': 'apartment',
                'walking': 45,
                'beginner': True
            },

            'Pug': {
                'size': 'small',
                'activity': 'low',
                'living': 'apartment',
                'walking': 30,
                'beginner': True
            },

            'Border Collie': {
                'size': 'medium',
                'activity': 'high',
                'living': 'house',
                'walking': 90,
                'beginner': False
            },

        }

        results = []

        for breed, profile in breeds.items():

            score = 0

            if self.preferred_size == profile['size']:
                score += 25

            if self.activity_level == profile['activity']:
                score += 25

            if self.living_situation == profile['living']:
                score += 20

            difference = abs(
                self.walking_time -
                profile['walking']
            )

            if difference <= 15:

                score += 20

            elif difference <= 30:

                score += 10

            if self.first_time_owner == profile['beginner']:

                score += 10

            results.append({
                'breed': breed,
                'score': score
            })

        results.sort(
            key=lambda x: x['score'],
            reverse=True
        )

        return results[:5]

    def __str__(self):

        return f"PawMatch #{self.id}"


# ============================================================
# PAWFIND — LOST / FOUND DOG REPORT
# ============================================================

class PawFind(models.Model):

    REPORT_TYPES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPES
    )

    dog_name = models.CharField(
        max_length=100,
        blank=True
    )

    breed = models.CharField(
        max_length=100,
        blank=True
    )

    color = models.CharField(
        max_length=50,
        blank=True
    )

    size = models.CharField(
        max_length=30,
        blank=True
    )

    location = models.CharField(
        max_length=200
    )

    date = models.DateField()

    description = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to='pawfind/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def calculate_matches(self):

        opposite_type = (
            'found'
            if self.report_type == 'lost'
            else 'lost'
        )

        other_reports = PawFind.objects.filter(
            report_type=opposite_type
        ).exclude(
            id=self.id
        )

        matches = []

        for report in other_reports:

            score = 0

            # =================================================
            # BREED MATCH — 30 POINTS
            # =================================================

            if (
                self.breed
                and report.breed
                and
                self.breed.lower().strip()
                ==
                report.breed.lower().strip()
            ):

                score += 30

            # =================================================
            # COLOR MATCH — 20 POINTS
            # =================================================

            if (
                self.color
                and report.color
                and
                self.color.lower().strip()
                ==
                report.color.lower().strip()
            ):

                score += 20

            # =================================================
            # SIZE MATCH — 15 POINTS
            # =================================================

            if (
                self.size
                and report.size
                and
                self.size.lower().strip()
                ==
                report.size.lower().strip()
            ):

                score += 15

            # =================================================
            # LOCATION MATCH — 20 POINTS
            # =================================================

            if (
                self.location
                and report.location
                and
                self.location.lower().strip()
                ==
                report.location.lower().strip()
            ):

                score += 20

            # =================================================
            # DATE PROXIMITY — 15 POINTS
            # =================================================

            date_difference = abs(
                (self.date - report.date).days
            )

            if date_difference == 0:

                score += 15

            elif date_difference <= 2:

                score += 10

            elif date_difference <= 7:

                score += 5

            # =================================================
            # STORE MATCH
            # =================================================

            if score > 0:

                matches.append({

                    'report': report,

                    'score': score,

                    'date_difference':
                        date_difference

                })

        # Highest compatibility first

        matches.sort(
            key=lambda x: x['score'],
            reverse=True
        )

        return matches[:10]

    def __str__(self):

        return (
            f"{self.report_type.title()} - "
            f"{self.breed or 'Dog'}"
        )