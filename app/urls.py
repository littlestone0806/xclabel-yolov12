from django.urls import path
from .views import UserView
from .views import IndexView
from .views import TaskView
from .views import SampleView
from .views import TrainView
from .views import TrainTestView
from .views import StorageView

app_name = 'app'

urlpatterns = [
    # 主页功能
    path('', IndexView.index),
    # 登陆退出
    path('login', UserView.web_login),
    path('logout', UserView.web_logout),
    # 用户管理
    path('user/index', UserView.index),
    path('user/add', UserView.add),
    path('user/edit', UserView.edit),
    path('user/postDel', UserView.api_postDel),

    path('index/getIndex', IndexView.api_getIndex),

    # 任务管理
    path('task/index', TaskView.index),
    path('task/add', TaskView.add),
    path('task/edit', TaskView.edit),
    path('task/sync', TaskView.api_sync),
    path('task/postDel', TaskView.api_postDel),
    path('sample/index', SampleView.index),
    path('sample/getInfo', SampleView.api_getInfo),
    path('sample/postSaveAnnotation', SampleView.api_postSaveAnnotation),
    path('sample/postDelAnnotation', SampleView.api_postDelAnnotation),
    path('sample/getIndex', SampleView.api_getIndex),
    path('sample/postAdd', SampleView.api_postAdd),
    path('sample/postDel', SampleView.api_postDel),
    path('train/index', TrainView.index),
    path('train/add', TrainView.add),
    path('train/manage', TrainView.manage),
    path('train/postDel', TrainView.api_postDel),
    path('train/postTaskCreateDatasets', TrainView.api_postTaskCreateDatasets),
    path('train/postTaskStartTrain', TrainView.api_postTaskStartTrain),
    path('train/postTaskStopTrain', TrainView.api_postTaskStopTrain),
    path('train/getTrainLog', TrainView.api_getTrainLog),

    path('trainTest/postAdd', TrainTestView.api_postAdd),
    path('trainTest/postDel', TrainTestView.api_postDel),
    path('trainTest/getIndex', TrainTestView.api_getIndex),

    # 系统功能
    path('storage/download', StorageView.download),
    path('storage/access', StorageView.access),
]
