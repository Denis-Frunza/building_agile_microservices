FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_order_service

COPY shop_order_service/requirements.txt /shop_order_service/requirements.txt

RUN pip install -r requirements.txt

COPY . /shop_order_service

# Create and apply migrations during the Docker image build process
RUN python3 shop_order_service/manage.py migrate
RUN python3 shop_order_service/manage.py makemigrations order
RUN python3 shop_order_service/manage.py migrate order