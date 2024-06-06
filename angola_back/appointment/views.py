from rest_framework import viewsets, permissions
from .models import AppReq
from .serializers import AppReqSerializer

class AppReqViewSet(viewsets.ModelViewSet):
    serializer_class = AppReqSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AppReq.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
