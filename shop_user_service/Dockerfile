FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_user_service

COPY shop_user_service/requirements.txt /shop_user_service/requirements.txt

RUN pip install -r requirements.txt

COPY . /shop_user_service

# Create and apply migrations during the Docker image build process
# RUN python3 shop_user_service/manage.py migrate
# RUN python3 shop_user_service/manage.py makemigrations user_auth
# RUN python3 shop_user_service/manage.py migrate user_auth