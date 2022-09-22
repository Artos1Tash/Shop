# Shop
Развертывание проекта

Развернуть локально 
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r req.txt
4. python manage.py makemigrations
5. python manage.py migrate

Развернуть через Docker
1. docker-compose up -d --build
2. docker-compose logs -f
