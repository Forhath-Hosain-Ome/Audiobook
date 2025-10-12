from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        'message': f'Hello {request.user.username}! This is a protected view.',
        'user': request.user.username
    })