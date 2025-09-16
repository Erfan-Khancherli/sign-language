# Sign Language Backend

This project is a **backend application** designed to help deaf people learn **sign language**. It provides APIs for managing users, words, packages, and favorite items. This repository focuses only on the backend side.

## Features

- User registration and authentication
- CRUD operations for words and packages
- Favorite words management
- Supports multiple packages for learning
- Built with **Python** and **Django**

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default, can be changed)
- **API:** Django REST Framework

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Erfan-Khancherli/sign-language.git
   cd sign-language
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate
5. Run the development server:
   ```bash
   python manage.py runserver
