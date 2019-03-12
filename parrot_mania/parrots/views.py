from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from parrots.models import Parrot
from parrots.serializers import ParrotSerializer


class ParrotViewSet(viewsets.ModelViewSet):
    queryset = Parrot.objects.all()
    serializer_class = ParrotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        """Return the authenticated user's parrots."""
        return serializer.save(user=self.request.user)
