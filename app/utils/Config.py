import json
import os


class Config:
    def __init__(self, filepath):
        config_data = None
        for encoding in ["utf-8","gbk"]:
            try:
                f = open(filepath, 'r', encoding=encoding)
                content = f.read()
                config_data = json.loads(content)
                f.close()
                break
            except Exception as e:
                print("Config read %s error: encoding=%s,%s" % (str(filepath),encoding,str(e)))

        if config_data:
            self.__config_data_str = str(config_data)
            self.host = "http://" + config_data.get("host")
            self.port = int(config_data.get("port"))
            self.ffmpeg = config_data.get("ffmpeg")
            self.storageDir = config_data.get("storageDir")
            self.storageTempDir = os.path.join(self.storageDir,"temp")
            # 存储路径
            if not os.path.exists(self.storageTempDir):
                os.makedirs(self.storageTempDir)
            # self.storageDir_www = "http://%s:%d/storage/access?filename=" % (host, adminPort)
            self.storageDir_www = "/storage/access?filename="
            self.yolo12 = config_data.get("yolo12")

        else:
            msg = "Config read %s error" % str(filepath)
            raise Exception(msg)

    def __del__(self):
        pass

    def getConfigStr(self):
        return self.__config_data_str

    def show(self):
        pass
