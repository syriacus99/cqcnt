from django.shortcuts import render
import os
from pathlib import Path
from django.http import HttpResponse,Http404,StreamingHttpResponse
from django.http import FileResponse
BASE_DIR = Path(__file__).resolve().parent.parent

def stream_download(request):
    file_name = request.GET.get("file_name")
    try:
        response = StreamingHttpResponse(open(os.path.join(BASE_DIR,"static",file_name),'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
    except Exception:
        raise Http404