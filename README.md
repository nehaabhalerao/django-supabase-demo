# Demo Django Project (Inventory CRUD + External API + Visualization)

This repository is a minimal Django project demonstrating:
- CRUD REST APIs for an `Item` model (Create, Read, Update, Delete) using Django REST Framework.
- An example third-party API integration endpoint (`/api/items/fetch-external/`) that pulls data from JSONPlaceholder.
- A simple dashboard (`/`) that visualizes summary statistics using Chart.js fetched from `/api/items/stats/`.

## Quick setup (local, SQLite)
1. Clone the repository and `cd` into it.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open `http://127.0.0.1:8000/` for the dashboard, `http://127.0.0.1:8000/admin/` for admin, and `http://127.0.0.1:8000/api/items/` for the API.

## Switching to PostgreSQL / Supabase
Update `demo/settings.py` DATABASES section, for example:
```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'your_db_name',
    'USER': 'your_db_user',
    'PASSWORD': 'your_password',
    'HOST': 'db.host',
    'PORT': 5432,
  }
}
```
You can use Supabase credentials in the same way.

## API Endpoints (examples)
- `GET /api/items/` — list items
- `POST /api/items/` — create item
- `GET /api/items/{id}/` — retrieve item
- `PUT /api/items/{id}/` — update item
- `DELETE /api/items/{id}/` — delete item
- `GET /api/items/fetch-external/` — example external API call (JSONPlaceholder)
- `GET /api/items/stats/` — aggregated totals for visualization

## Notes
- This is a scaffold meant to be deployed or extended. It uses SQLite by default for quick local testing.
- The project includes `requirements.txt` for easy setup.
