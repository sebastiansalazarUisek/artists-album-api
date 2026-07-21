from rest_framework import viewsets
from .models import Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        artist = self.request.query_params.get("artist")

        if artist:
            queryset = queryset.filter(artist=artist)

        return queryset