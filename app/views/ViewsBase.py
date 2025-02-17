import json
import os
import base64
from datetime import datetime, timedelta
from django.db import connection
from app.utils.Config import Config
from app.utils.Utils import buildPageLabels
from django.http import HttpResponse
from framework.settings import BASE_DIR, PROJECT_VERSION, PROJECT_FLAG
from app.utils.Logger import CreateLogger
from app.utils.OSSystem import OSSystem
__log_dir = os.path.join(BASE_DIR, "log")
if not os.path.exists(__log_dir):
    os.makedirs(__log_dir)

g_logger = CreateLogger(filepath=os.path.join(__log_dir, "xclabel%s.log" % (datetime.now().strftime("%Y%m%d-%H%M%S"))), is_show_console=True)
g_logger.info("xclabel %s,%s" % (PROJECT_VERSION, PROJECT_FLAG))
g_logger.info("BASE_DIR:%s" % BASE_DIR)
g_config = Config(filepath=os.path.join(BASE_DIR, "config.json"))
g_logger.info("config.json:%s" % g_config.getConfigStr())
g_osSystem = OSSystem()

g_session_key_user = "user"


class Database():

    def select(self, sql):

        cursor = connection.cursor()
        cursor.execute(sql)
        data = []
        try:
            rawData = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]

            for row in rawData:
                d = {}
                for index, value in enumerate(row):
                    d[col_names[index]] = value

                data.append(d)
        except Exception as e:
            g_logger.error("DjangoSql.select error: %s" % str(e))
            g_logger.error(sql)

        return data

    def select_ex(self, sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        data = []

        rawData = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

        for row in rawData:
            d = {}
            for index, value in enumerate(row):
                d[col_names[index]] = value

            data.append(d)

        return data

    def insert(self, tb_name, d):

        sql = "insert into %s(%s) values(%s)" % (
            tb_name, ",".join(d.keys()), ",".join(map(lambda x: "'" + str(x) + "'", d.values())))

        return self.execute(sql)

    def execute(self, sql):
        ret = False
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            ret = True
        except Exception as e:
            g_logger.error("DjangoSql.execute error: %s" % str(e))
            g_logger.error(sql)
        return ret

    def execute_ex(self, sql):
        cursor = connection.cursor()
        cursor.execute(sql)
g_database = Database()

def f_readSampleCountAndAnnotationCount(task_code):
    sample_count = g_database.select("select count(id) as count from xc_task_sample where task_code='%s'" % task_code)
    sample_count = int(sample_count[0]["count"])
    sample_annotation_count = g_database.select(
        "select count(id) as count from xc_task_sample where task_code='%s' and annotation_state=1" % task_code)
    sample_annotation_count = int(sample_annotation_count[0]["count"])

    return sample_count, sample_annotation_count

def readUser(request):
    user = request.session.get(g_session_key_user)
    return user


def parse_get_params(request):
    params = {}
    try:
        for k in request.GET:
            params.__setitem__(k, request.GET.get(k))
    except Exception as e:
        params = {}

    return params


def parse_post_params(request):
    params = {}
    for k in request.POST:
        params.__setitem__(k, request.POST.get(k))

    # 接收json方式上传的参数
    if not params:
        try:
            params = request.body.decode('utf-8')
            params = json.loads(params)
        except:
            params = {}

    return params


def HttpResponseJson(res):
    def json_dumps_default(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            raise TypeError

    return HttpResponse(json.dumps(res, default=json_dumps_default), content_type="application/json")

