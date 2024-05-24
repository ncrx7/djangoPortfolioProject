# Base image olarak Python 3.12 kullan
FROM python:3.12

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Ortam değişkenlerini ayarla (opsiyonel, gerekliyse)
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Django ile statik dosyaları toplama komutunu çalıştır
RUN python manage.py collectstatic --noinput --settings=djangoPortfolioProject.settings

# Uygulamayı başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=djangoPortfolioProject.settings"]