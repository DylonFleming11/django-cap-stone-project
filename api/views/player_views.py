from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.player import Player
from ..serializers import PlayerSerializer


class Players(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PlayerSerializer
    def get(self, request):
        """Index request"""
        player = Player.objects.filter(owner=request.user.id)
        data = PlayerSerializer(player, many=True).data
        return Response({ 'player': data })

    def post(self, request):
        """Create request"""
        request.data['player']['owner'] = request.user.id
        player = PlayerSerializer(data=request.data['player'])
        if player.is_valid():
            player.save()
            return Response({ 'player': player.data }, status=status.HTTP_201_CREATED)
        return Response(player.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        player = get_object_or_404(Player, pk=pk)
        if not request.user.id == player.owner.id:
            raise PermissionDenied('Unauthorized, you did not make this player')

        data = PlayerSerializer(player).data
        return Response({ 'player': data })

    def delete(self, request, pk):
        """Delete request"""
        player = get_object_or_404(Player, pk=pk)
        if not request.user.id == player.owner.id:
            raise PermissionDenied('Unauthorized, you did not make this player')
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        player = get_object_or_404(Player, pk=pk)
        if not request.user.id == player.owner.id:
            raise PermissionDenied('Unauthorized, you did not make this player')
        request.data['player']['owner'] = request.user.id
        data = PlayerSerializer(player, data=request.data['player'], partial=True)
        if data.id_valid():
            data.save()
            return Response()
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
