from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Challenge
from .serializers import ChallengeSerializer

@api_view(['GET'])
def get_challenges(request):
    challenges = Challenge.objects.all()
    serializer = ChallengeSerializer(challenges, many=True)
    return Response(serializer.data)

