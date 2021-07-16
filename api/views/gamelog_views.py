from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.gamelog import GameLog
from ..serializers import GameLogSerializer, GameLogPlusSerializer

class GameLogs(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        game = GameLog.objects.all()[:10]
        data = GameLogPlusSerializer(game, many=True).data
        return Response(data)

    serializer_class = GameLogSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        game = GameLogSerializer(data=request.data)
        if game.is_valid():
            game.save()
            return Response(game.data, status=status.HTTP_201_CREATED)
        else:
            return Response(game.errors, status=status.HTTP_400_BAD_REQUEST)

class GameLogDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        game = get_object_or_404(GameLog, pk=pk)
        data = GameLogPlusSerializer(game).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        game = get_object_or_404(GameLog, pk=pk)
        ms = GameLogSerializer(game, data=request.data['author'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        game = get_object_or_404(GameLog, pk=pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
