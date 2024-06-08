from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from .repository import get_product, get_user_auth

import redis
import json
import hashlib

HOURS_24 = 86400

r = redis.Redis(host='redis', port=6379, db=0)

def generate_order_hash(order_data):
    """Генерирует хеш от содержимого заказа"""
    order_json = json.dumps(order_data, sort_keys=True)
    return hashlib.sha256(order_json.encode('utf-8')).hexdigest()


class OrderCreate(APIView):
    """ Create an order """
    name = 'order-create'

    def post(self, request, format=None):
        user = get_user_auth(token=request.data['token'])
        if user.status_code == 200:
            user_id = user.json()['pk']
            order_data = request.data['orderItems']

            order_hash = generate_order_hash(order_data)

            existing_order_id = r.get(order_hash)
            if existing_order_id:
                existing_order = Order.objects.get(pk=existing_order_id)
                serializer = OrderSerializer(existing_order)
                return Response(serializer.data, status=status.HTTP_200_OK)

            serializer = OrderItemSerializer(data=order_data, many=True)
            if serializer.is_valid():
                order = Order.objects.create(user=user_id)
                for item_data in serializer.validated_data:
                    product = get_product(item_data['product_id']).json()
                    OrderItem.objects.create(
                        product_id=product['pk'],
                        product_name=product['name'],
                        order=order,
                        qty=item_data['qty'],
                        price=product['price'],
                        image=product['image']
                    )

                r.set(order_hash, order.id, ex=HOURS_24)

                serializer = OrderSerializer(order)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class OrderDetail(APIView):
    """
    Retrieve, update or delete a  order.
    """
    name = 'order-detail'

    def get_object(self, pk, token):
        try:
            user = get_user_auth(token=token)
            if user.status_code == 200:
                print(f'User login 1 view: {user.json()}')
                order = Order.objects.get(pk=pk, user=user.json()['pk'])
                print(f'Order user: {order.user}')
                return order
            return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        print(f"Order {order}")

        if hasattr(order, 'user'):
            serializer = OrderSerializer(order)
            print(f'Order serialzer: {serializer.data}')
            return Response(serializer.data)
        return Response({'error': 'User information not found in the order object'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserOrders(APIView):
    name = 'user-orders'

    def get(self, request, token, format=None):
        try:
            user = get_user_auth(token=token)

            
            print(f'User in orders list: {user.json()} ')
        except:
            return Response({'detail': f'No connection with '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            if user.status_code == 200:
                order = Order.objects.filter(user=user.json()['pk'])
                serializer = OrderSerializer(order, many=True)
                return Response(serializer.data)
        return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-list'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'orders': reverse(OrderCreate.name, request=request),

            }
        )
