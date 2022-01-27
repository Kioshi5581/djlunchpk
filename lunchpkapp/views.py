from django.contrib.auth.forms import UserCreationForm
from rest_framework.generics import CreateAPIView
from django import forms
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .paginations import perpage_pagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from .serializers import *
from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
import random
from django.contrib.auth import get_user_model



# Create your views here.

# class SignupView(generics.GenericAPIView):
#     serializer_class = RegistrationSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })

# class SignupView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     search_fields = '__all__'
#     filterset_fields = '__all__'
#     paginnation_class = perpage_pagination
#     authentication_class = (TokenAuthentication,)


class SignupView(CreateAPIView):
    
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SignupSerializer




class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'
    paginnation_class = perpage_pagination
    authentication_class = (TokenAuthentication,)

def index(request):
    return render(request, 'index.html')


def deals(request):
    my_deals = Deals.objects.all()
    context = {
        "Deals": my_deals,
    }
    return render(request, 'deals.html', context)


    

def deals_detail(request, pk):
    deal = Deals.objects.get(id=pk)
    my_deals = Deals.objects.all()
    context = {
        "Deals": deal,
        "myDeals": my_deals,
    }
    return render(request, "deal_detail.html", context)




def frozens(request):
    my_frzn = Frozen.objects.all()
    context = {
        "Frozen": my_frzn,
    }
    return render(request, 'frozen.html', context)


def frozens_detail(request, pk):
    frozen = Frozen.objects.get(id=pk)
    context = {
        "Frozen": frozen,
    }
    return render(request, "frz_detail.html", context)


def bcme_foodlancer(request):
    return render(request, 'foodlancer.html')


def apply_foodlancer(request):
  if request.method == 'POST':
    form = FoodlancerRegistration(data=request.POST)
    if form.is_valid():
       form.save()
       return HttpResponse("<h1>Success!</h1>")
  else:
    form = FoodlancerRegistration()
  return render(request, 'appy_foodlancer.html', {"form": form})



def order_now(request):
    if request.method == 'POST':
        form = Order_Now(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank-you/")
    else:
        form = Order_Now()

    return render(request, 'order.html', {"form": form})


def order_success(request):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

    password_len = 8

    password_count = 1

    for x in range(0, password_count):

        password = ""

        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char

    context = {
        "code": password
    }

    return render(request, 'order_secret.html', context)



def monthly_menu(request, pk):
    monthlypackage = MonthlyPackage.objects.get(id=pk)
    context = {
        "Package": monthlypackage
    }
    return render(request, 'monthly_menu.html', context)



def contact_us(request):
    if request.method == 'POST':
        form = Contact_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Contact_form()


    return render(request, 'contact.html', {"form": form})

# Deals Api



class DealViewSet(viewsets.ModelViewSet):
    queryset = Deals.objects.all()

    serializer_class = DealsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['^name', '=id', '^details', '^price']
    filterset_fields = ['name', 'id', 'persons', 'details', 'price', 'price3']
    paginnation_class = perpage_pagination
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class FrozenViewSet(viewsets.ModelViewSet):
    queryset = Frozen.objects.all()
    serializer_class = frozenSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'id', 'persons', 'pieces', 'pieces', 'price']
    filterset_fields = ['name', 'id', 'persons', 'pieces', 'pieces', 'price']
    paginnation_class = perpage_pagination
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MonthlyViewSet(viewsets.ModelViewSet):
    queryset = MonthlyPackage.objects.all()
    serializer_class = MonthlySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'
    paginnation_class = perpage_pagination
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

# class DealViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         deal = Deals.objects.all()
#         serializer = DealsSerializer(deal, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             deal = Deals.objects.get(id=id)
#             serializer = DealsSerializer(deal)
#             return Response(serializer.data)

#     def create(self, request):
#         serializer = DealsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk):
#         id = pk 
#         deal = Deals.objects.get(id=id)
#         serializer = DealsSerializer(deal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk):
#         id = pk 
#         deal = Deals.objects.get(id=id)
#         serializer = DealsSerializer(deal, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         id = pk 
#         deal = Deals.objects.get(id=id)
#         deal.delete()
#         return Response({'msg':'Data Deleted'})
