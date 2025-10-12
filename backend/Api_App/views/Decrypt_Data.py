from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from cryptography.fernet import Fernet
import base64

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decrypt_data(request):
    encrypted_data = request.data.get('encrypted_data')
    if not encrypted_data:
        return Response({'error': 'Encrypted data is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        decrypted_data = fernet.decrypt(base64.urlsafe_b64decode(encrypted_data))
        return Response({
            'decrypted_data': decrypted_data.decode(),
            'message': 'Data decrypted successfully'
        })
    except Exception as e:
        return Response({'error': 'Decryption failed'}, status=status.HTTP_400_BAD_REQUEST)
