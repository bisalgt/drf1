from rest_framework.decorators import api_view, throttle_classes, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied



# to convert bytes of string to json we need to import io
import io

# to create token we need a particular user instance as token has OneToOneField.
from django.contrib.auth.models import User 



SAFE_METHODS = ['GET', 'OPTIONS', 'HEADERS']


# custom throttling
class CustomAnonymousRateThrottle(AnonRateThrottle):
	rate='3/day'

# custom Permissions
class CustomBasePermission(BasePermission):
	def has_permisssion(self, request, view):
		return True
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return False

def check_object_permissions(request, obj):
	if request.method in SAFE_METHODS:
		return True
	raise PermissionDenied


# using custom throttling, we need to use both the throttling classes available

# we can include or override our default authentication classes if specified as a decorator for function based views

# By default the permissions class is set to AllowAny

# We can customize the default behaviour by adding Default settings under rest_framework which is used globally by all views,
# or by importing them in views and using in required views


########## Token Authentication Part #################

# token is created for user and saved
# the genereted token is in the format Token: dlfjasofo23432klsdf3f3f323
# to send the bearer token from postman we need to change the keyword by inheriting the TokenAuthentication class and subclassing



# Token.objects.filter(user = User.objects.get(id=1)).delete()
# token = Token.objects.create(user=User.objects.get(id=1))
# print(token.key)
print(Token.objects.all())

# subclassing TokenAuthentication to change the default header keyword=Token to keyword=Bearer
class CustomKeywordForTokenAuthentication(TokenAuthentication):
	keyword = "Bearer"






@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@throttle_classes([CustomAnonymousRateThrottle,UserRateThrottle])
@permission_classes([CustomBasePermission,]) 
def home(request):
	print(dir(request))
	stream = io.BytesIO(request.body)
	print(str(stream), type(stream))
	data = JSONParser().parse(stream)
	print(data,type(data))
	# print(request.headers)
	check_object_permissions(request, request.user)
	print(request.user)
	print('------')
	print(request.auth)

	if request.method=='GET':
		content = {
			'name': 'Bishal Gautam',
			'age': 24,
			'salary': '$1M',
			'professional': 'Engineer'
		}
	elif (request.method=='POST'):	
		content = {
		'data': request.data
		}
	return Response(content)





class HomeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {
            'user': "bishal",  # `django.contrib.auth.User` instance.
            'auth': "Fully Authorized"  # None
        }
        return Response(content)



@api_view(['GET', 'POST'])
def about(request):
	content = {
	'name': 'Bishal',
	'position': 'MultiMillonaire'
	}
	return content