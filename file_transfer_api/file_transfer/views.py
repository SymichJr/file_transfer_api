from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class UploadFileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        data = request.data
        file_serializer = FileSerializer(data=data)
        if file_serializer.is_valid():
            file_serializer.save()
            process_file.delay(file_serializer.data["id"])
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):
    serializer_class = FileSerializer

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
