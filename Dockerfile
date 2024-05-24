# Base image olarak Python 3.12 kullan
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --settings=djangoPortfolioProject.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=djangoPortfolioProject.settings"]