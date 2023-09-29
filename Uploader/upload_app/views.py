from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_new = File.objects.create(
                file=request.data['file']
            )
            id_file = File.objects.latest('id').id
            process_file(id_file)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
