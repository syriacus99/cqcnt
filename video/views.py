from django.shortcuts import render
from video.models import Video
import json
from django.http import HttpResponse
# Create your views here.
def get_url(request):
    id = request.GET.get("id")
    print(id)
    url_list =list()
    if (id =='all'):
        url_list_set = Video.objects.all().values("video_id","video_url","cover_url")
        for each_url in url_list_set:
            url_list.append({'video_id':each_url['video_id'],
                             'videoDownloadUrl':each_url['video_url'],
                             'coverImgUrl':each_url['cover_url']})
        return HttpResponse(json.dumps(url_list))
    else:
        url_response = Video.objects.filter(video_id=id).values("video_url","cover_url")
        print(url_response)
        return HttpResponse(json.dumps([{
            "coverImgUrl": url_response[0]['cover_url'],
            "videoDownloadUrl": url_response[0]['video_url']
        }]))