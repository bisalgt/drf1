from rest_framework.decorators import api_view
from rest_framework.response import Response







@api_view(['GET','POST'])
def home(request):
	print(dir(request))
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