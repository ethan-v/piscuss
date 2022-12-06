from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    template = loader.get_template('index.html')
    context = {
        'app_name': 'Piscuss | Opensource Discussion App',
    }
    return HttpResponse(template.render(context, request))