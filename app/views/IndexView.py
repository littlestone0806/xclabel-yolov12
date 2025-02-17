from app.views.ViewsBase import *
from app.models import *
from framework.settings import PROJECT_ADMIN_START_TIMESTAMP
from django.shortcuts import render
from app.utils.OSSystem import OSSystem


def index(request):
    context = {

    }
    return render(request, 'app/web_index.html', context)

def api_getIndex(request):
    ret = False
    msg = "未知错误"
    osInfo = {}
    appInfo = {
        "project_version": PROJECT_VERSION,
        "project_flag": PROJECT_FLAG,
        "start_timestamp": PROJECT_ADMIN_START_TIMESTAMP
    }
    try:
        osSystem = OSSystem()
        osInfo = osSystem.getOSInfo()

        ret = True
        msg = "success"
    except Exception as e:
        msg = str(e)

    res = {
        "code": 1000 if ret else 0,
        "msg": msg,
        "osInfo": osInfo,
        "appInfo": appInfo
    }
    return HttpResponseJson(res)