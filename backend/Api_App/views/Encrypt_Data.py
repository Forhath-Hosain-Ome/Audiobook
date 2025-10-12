from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework import status
from cryptography.fernet import Fernet
import base64

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def encrypt_data(request):
    data = request.data.get('data')
    if not data:
        return Response({'error': 'Data is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    encrypted_data = fernet.encrypt(data.encode())
    return Response({
        'encrypted_data': base64.urlsafe_b64encode(encrypted_data).decode(),
        'message': 'Data encrypted successfully'
    })