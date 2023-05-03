import pandas
from django.forms import model_to_dict
from django.shortcuts import render, redirect


from .models import Unitsdb
from .forms import UnitsForm
import os
import environ
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .resources import UnitsResources
from .serializers import UnitSerializer, UserSerializer
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import views
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
# Create your views here.




# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# # reading .env file
# environ.Env.read_env()
#
# def environ(request):
#
#     variable_env = env('HELLO')
#     return render(
#         request,
#         'environ.html',
#         context={'variable': variable_env}
#     )

@cache_page(60*15)
def index(request):
    unitDBiter = Unitsdb.objects.all()
    for i in unitDBiter:
        i.imgIndex = str(i.img)[5:]
        i.imgBck = str(i.img_bck)[5:]
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()



    data = {
        'title': 'SC2 Units',
        'unitslist' : unitDBiter,
        'form': form,
    }
    template = 'index/main.html'
    return render(request, template, data)


class UnitDetailView(DetailView):
    error = ''

    model = Unitsdb
    template_name = 'index/detail_view.html'
    context_object_name = 'unit'


def create(request):
    error =''
    if request.method == "POST":
        form = UnitsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'invalid form'
    form = UnitsForm()
    data = {
        'title': 'Create unit',
        'form': form,
        'error': error,
    }
    return render(request, 'index/create.html', data)

class UnitUpdateView(UpdateView):
     model= Unitsdb
     template_name = 'index/create.html'
     #fields =['name', 'fr', 'type', 'short_des', 'des']
     form_class= UnitsForm


class UnitDelete(DeleteView):
    model = Unitsdb
    success_url = '/units/'
    template_name = 'index/unit_delete.html'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'index/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'index/register.html', {'form': form})

class UnitsAPIPagination(PageNumberPagination):
    page_size = 10,
    page_size_query_param = 'page_size'
    max_page_size = 10000
class UnitsAPIViewSet(mixins.CreateModelMixin, #viewsets.ModelViewSet <- все наследования как в модел вью сет
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Unitsdb.objects.all()
    serializer_class = UnitSerializer


    # permission_classes = (IsAdminOrReadOnly, )
    # pagination_class = UnitsAPIPagination
    #authentication_classes = (TokenAuthentication, )

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return Unitsdb.objects.all()[:3]
    #     return Unitsdb.objects.filter(pk=pk)

    # @action(methods=['get'], detail=False)
    # def unitsListDownload(self,request, pk=None):
    #     resources = UnitsResources()
    #     dataset = resources.export()
    #     response = HttpResponse(dataset.xls)
    #     response['Content-Disposition'] = 'attachment; filename="units.xls"'
    #     return response


class LoginView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
class RegisterView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtectedView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, authenticated user!'})

class AdminView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, admin user!'})

class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Successfully logged out.'})

class TokenRevokeView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message': 'Token revoked successfully.'})