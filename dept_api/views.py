from django.shortcuts import render
#from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

# Create your views here.
class Live_view(APIView):
	def get(self, request, *args, **kwargs):
		qs = Post.objects.all()
		serializer = PostSerializer(qs, many = True)
		return Response(serializer.data)
		# data = {
		# 	"fname": "Kevin",
		# 	"description": "python django course"
		# 	# "lname": "Maina",
		# 	# "age" : 30
		# }
		# return Response(data)

	def post (self, request, *args, **kwargs):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

# def App_view(request):
# 	data = {
# 		"fname": "Kevin",
# 		"lname": "Maina",
# 		"age" : 30
# 	}
# 	return  JsonResponse(data)
















