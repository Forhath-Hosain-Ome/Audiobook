from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def public_view(request):
    return Response({'message': 'This is a public endpoint - no authentication required'})
