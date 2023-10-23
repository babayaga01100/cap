from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from server.models import SmartFarm
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken import views

class RegistrationSF(APIView):

    def post(self, request):
        # 토큰 검증
        token = request.data.get('token')
        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user  # 토큰에서 사용자 추출
        except Token.DoesNotExist:
            return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        # 토큰이 유효하고 사용자가 인증되면 나머지 작업 수행
        serializer = SFSerializer(data=request.data)
        print(serializer.data)
        if serializer.is_valid():
            # SmartFarm 모델의 user 필드에 사용자 연결
            serializer.validated_data['user'] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)