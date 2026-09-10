# 🐾 PawPulse

### Understand Your Dog's Every Pulse.

**PawPulse** is a Django-powered dog wellness and care platform designed to bring everyday pet tracking, behavioral observations, breed compatibility, and lost-dog discovery into one unified application.

🌐 **Live Application:** https://pawpulse-kfuu.onrender.com

📦 **Repository:** https://github.com/Sam-1014/PawPulse

---

## ✨ Why PawPulse?

Pet care information is often scattered across notebooks, reminders, apps, and social platforms.

PawPulse brings these experiences together into a single web application where users can:

* 🐕 Create and manage dog profiles
* ❤️ Track daily wellness and activity
* 🧠 Observe behavioral trends
* 🐾 Discover dog breeds compatible with their lifestyle
* 🔎 Report lost or found dogs
* 🤝 Automatically identify potential lost/found matches
* 📊 Generate Python-powered wellness scores and observations

The goal is simple:

> **Turn everyday pet-care data into meaningful, easy-to-understand insights.**

---

# 🚀 Core Modules

## ❤️ 1. Vitality — Daily Wellness Tracker

**Vitality** helps owners record their dog's everyday lifestyle and wellness information.

### Tracks

* 🍖 Meals
* 💧 Water intake
* 🚶 Walk duration
* 😴 Sleep
* ⚡ Energy level
* 🎾 Playtime
* 😊 Mood

### Wellness Score

PawPulse calculates a daily wellness score using a weighted scoring algorithm based on recorded activity.

Example:

```text
Energy       → 25%
Walking      → 20%
Sleep        → 20%
Playtime     → 15%
Meals        → 10%
Water        → 10%
```

The result is converted into an easy-to-understand wellness score.

Example:

```text
Bruno
❤️ Wellness Score: 92/100
```

---

# 🧠 2. PawMood — Behavior Journal

Dogs cannot tell us how they are feeling.

**PawMood** provides a structured way to record behavioral indicators over time.

### Records

* ⚡ Energy
* 🍖 Appetite
* 🎾 Playfulness
* 😴 Sleep
* 😊 Mood
* 📝 Daily notes

PawMood compares recent records with previous entries and generates simple observations.

Example:

```text
📉 Bruno's energy has decreased compared with the previous entry.

🎾 Bruno's playfulness has increased recently.

🍖 Bruno's appetite is stable.
```

These are **behavioral observations rather than medical diagnoses**.

---

# 🐕 3. PawMatch — Find the Right Dog

Choosing a dog breed should consider more than appearance.

**PawMatch** uses a Python-based compatibility scoring system to compare a user's lifestyle with different breed profiles.

### Questionnaire

Users provide:

* 🏠 Living situation
* 📏 Preferred dog size
* ⚡ Activity level
* 🚶 Available walking time
* 🐶 Whether they are a first-time owner

### Example Output

```text
🥇 Labrador Retriever     91%
🥈 Golden Retriever       87%
🥉 Beagle                 78%
```

The matching engine evaluates multiple lifestyle attributes and ranks the most compatible breeds.

### Matching factors

```text
Size              → 25 points
Activity Level    → 25 points
Living Situation  → 20 points
Walking Time      → 20 points
Owner Experience  → 10 points
```

---

# 🔎 4. PawFind — Lost Dog Finder

Losing a dog is stressful.

**PawFind** allows users to create:

* 🔴 Lost dog reports
* 🟢 Found dog reports

Each report can contain:

* Dog name
* Breed
* Color
* Size
* Location
* Date
* Description
* Photograph

PawFind then compares reports of opposite types and calculates a potential match score.

### Matching Algorithm

```text
Breed       → 30 points
Color       → 20 points
Size        → 15 points
Location    → 20 points
Date        → 15 points
```

Potential matches are ranked according to their calculated similarity.

Example:

```text
Potential Match
────────────────────────
Breed       ✓
Color       ✓
Size        ✓
Location    ✓
Date        ✓

Match Score: 100%
```

---

# 🏗️ System Architecture

```text
                        ┌─────────────────────┐
                        │      PawPulse       │
                        │    Django Web App    │
                        └──────────┬──────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
      │   Dog       │       │  Vitality   │       │  PawMood    │
      │  Profiles   │       │  Tracking   │       │  Behavior   │
      └─────────────┘       └─────────────┘       └─────────────┘
             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   │
             ┌─────────────────────┴─────────────────────┐
             │                                           │
             ▼                                           ▼
      ┌─────────────┐                            ┌─────────────┐
      │  PawMatch   │                            │   PawFind   │
      │ Compatibility│                            │ Lost/Found  │
      └─────────────┘                            └─────────────┘
             │                                           │
             └─────────────────────┬─────────────────────┘
                                   ▼
                         ┌──────────────────┐
                         │ Python Algorithms│
                         │ Scoring & Matching│
                         └────────┬─────────┘
                                  ▼
                         ┌──────────────────┐
                         │     Database     │
                         │ MySQL / Postgres │
                         └──────────────────┘
```

---

# 🛠️ Tech Stack

### Backend

* 🐍 Python
* Django
* Django ORM
* Gunicorn

### Database

* MySQL — local development
* PostgreSQL — production deployment

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Other Technologies

* Pillow — image uploads
* Git
* GitHub
* Render

---

# 📁 Project Structure

```text
PawPulse/
│
├── PawPulse/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── migrations/
│   │
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       │
│   │       ├── dogs/
│   │       │   ├── dog_form.html
│   │       │   └── dog_list.html
│   │       │
│   │       ├── vitality/
│   │       │   ├── vitality_form.html
│   │       │   └── vitality_dashboard.html
│   │       │
│   │       ├── pawmood/
│   │       │   ├── pawmood_form.html
│   │       │   └── pawmood_dashboard.html
│   │       │
│   │       ├── pawmatch/
│   │       │   └── pawmatch.html
│   │       │
│   │       └── pawfind/
│   │           └── pawfind.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── staticfiles/
│
├── build.sh
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🗄️ Database Models

PawPulse currently uses five primary Django models.

| Model      | Purpose                              |
| ---------- | ------------------------------------ |
| `Dog`      | Dog profile and personal information |
| `Vitality` | Daily wellness and activity records  |
| `PawMood`  | Behavioral journal entries           |
| `PawMatch` | Lifestyle compatibility calculations |
| `PawFind`  | Lost/found dog reports and matching  |

### Relationships

```text
Dog
 │
 ├── Vitality
 │
 └── PawMood

PawMatch
 └── Lifestyle → Breed Compatibility

PawFind
 ├── Lost Reports
 └── Found Reports
       ↓
   Match Scoring
```

---

# ⚙️ Intelligent Features

PawPulse currently uses **Python-powered rule-based algorithms** rather than claiming machine learning where it isn't actually being used.

### Wellness Scoring

Converts multiple daily activity indicators into a normalized wellness score.

### Breed Compatibility

Matches lifestyle preferences against predefined breed profiles.

### Lost/Found Matching

Compares report attributes and calculates a similarity score.

### Behavioral Observation

Compares recent and previous PawMood records to identify changes in tracked indicators.

---

# 💻 Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/Sam-1014/PawPulse.git
```

```bash
cd PawPulse
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the database

For local development, configure MySQL in:

```text
PawPulse/settings.py
```

Create the database:

```sql
CREATE DATABASE pawpulse;
```

Then configure your local MySQL credentials.

For production, PawPulse uses PostgreSQL through the `DATABASE_URL` environment variable.

---

## 5. Run migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6. Create an admin account

```bash
python manage.py createsuperuser
```

---

## 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Environment Configuration

Production secrets should not be committed to GitHub.

Example environment variables:

```text
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-postgresql-database-url
```

Local credentials should remain outside source control.

The project `.gitignore` excludes sensitive files such as:

```text
.env
db.sqlite3
media/
venv/
__pycache__/
.idea/
.vscode/
```

---

# ☁️ Deployment

PawPulse is deployed as a Django web application on **Render**.

### Production Architecture

```text
              Internet
                  │
                  ▼
        ┌──────────────────┐
        │      Render      │
        │   Web Service    │
        └────────┬─────────┘
                 │
                 │ Django
                 ▼
        ┌──────────────────┐
        │    PawPulse      │
        │     Backend      │
        └────────┬─────────┘
                 │
          DATABASE_URL
                 │
                 ▼
        ┌──────────────────┐
        │ Render PostgreSQL│
        └──────────────────┘
```

### Production server

```bash
gunicorn PawPulse.wsgi:application
```

### Static collection

```bash
python manage.py collectstatic --no-input
```

### Database migration

```bash
python manage.py migrate
```

---

# 📊 Example User Flow

```text
                    START
                      │
                      ▼
              Create Dog Profile
                      │
                      ▼
             Record Daily Vitality
                      │
                      ▼
              View Wellness Score
                      │
                      ▼
               Record PawMood
                      │
                      ▼
            Observe Behavior Trends
                      │
             ┌────────┴────────┐
             ▼                 ▼
         PawMatch           PawFind
             │                 │
             ▼                 ▼
      Breed Compatibility   Lost/Found
                              Matching
```

---

# 🎯 Design Philosophy

PawPulse follows a simple principle:

> **Pet technology should feel useful, understandable, and human.**

Instead of overwhelming users with raw data, the application converts everyday records into:

* Scores
* Comparisons
* Rankings
* Observations
* Potential matches

This makes the information easier to understand for everyday dog owners.

---

# 🔮 Future Improvements

PawPulse is designed to evolve beyond its current rule-based system.

### Planned Features

* 🤖 ML-based breed compatibility
* 📈 Advanced wellness trend prediction
* 🧠 ML-powered behavior anomaly detection
* 🩺 Veterinary reminder system
* 💊 Medication tracking
* 💉 Vaccination management
* 📊 Interactive analytics dashboard
* 📱 Progressive Web App support
* 🔔 Notifications and reminders
* 🗺️ Map-based lost-dog discovery
* 📍 Location-aware PawFind matching
* ☁️ Cloud image storage
* 🔐 User authentication and personalized dashboards
* 🐕 Expanded breed knowledge base
* 📷 Computer vision for dog identification
* 🧬 Personalized wellness recommendations

---

# 🧪 Project Status

```text
Version: 1.0
Status: Active Development
Deployment: Live
Backend: Django
Database: PostgreSQL (Production)
```

The current version focuses on demonstrating the core platform architecture and intelligent rule-based functionality.

---

# 👩‍💻 Developer

### Sasmita Karthikeyan

**Data Science Undergraduate | SRM Institute of Science and Technology**

Interested in:

* Machine Learning
* Data Science
* Full-Stack Development
* Embedded Systems
* Intelligent Applications
* Research & Engineering

### Profiles

* 💻 GitHub: [Sam-1014](https://github.com/Sam-1014)
* 🚀 Project: [PawPulse](https://github.com/Sam-1014/PawPulse)

---

# 📜 License

This project is currently intended as an academic and portfolio project.

© 2026 Sasmita Karthikeyan. All rights reserved.

---

# 🐾 Final Note

PawPulse started as a simple idea:

> **What if we could understand our dogs a little better through the data we already observe every day?**

From daily walks and meals to behavior changes and lost-dog discovery, PawPulse brings those pieces together into one platform.

**One dog. One pulse. One smarter way to care. 🐾**
