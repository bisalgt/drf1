from rest_framework.decorators import api_view, throttle_classes, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token


import io

# custom throttling
class CustomAnonymousRateThrottle(AnonRateThrottle):
	rate='3/day'


# using custom throttling, we need to use both the throttling classes available

# we can include or override our default authentication classes if specified as a decorator for function based views

# By default the permissions class is set to AllowAny

# We can customize the default behaviour by adding Default settings under rest_framework which is used globally by all views,
# or by importing them in views and using in required views
from django.contrib.auth.models import User

# Token.objects.filter(user = User.objects.get(id=1)).delete()
# token = Token.objects.create(user=User.objects.get(id=1))
# print(token.key)

print(Token.objects.all())

# subclassing TokenAuthentication to change the default header keyword=Token to keyword=Bearer
class CustomKeywordForTokenAuthentication(TokenAuthentication):
	keyword = "Bearer"

print(Token.objects.all())



@api_view(['GET','POST'])
@authentication_classes([CustomKeywordForTokenAuthentication,])
@throttle_classes([CustomAnonymousRateThrottle,UserRateThrottle])
@permission_classes([IsAuthenticated,]) 
def home(request):
	print(dir(request))
	stream = io.BytesIO(request.body)
	print(str(stream), type(stream))
	data = JSONParser().parse(stream)
	print(data,type(data))
	# print(request.headers)

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