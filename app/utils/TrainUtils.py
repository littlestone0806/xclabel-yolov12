import psutil
import shutil
import os
from datetime import datetime

class TrainUtils:
    def __init__(self,logger):
        self.logger = logger

    def getProcessInfoByName(self,processName):

        info = {
            "process_name": processName,  # 中文名
            "status": None,
            "pid": None,
            "create_date": None,
            "create_date_str": "00:00:00",
            "state": 0
        }

        for pid in psutil.pids():
            process = psutil.Process(pid)
            p_name_lower = process.name().lower()  # 进程实际名称，包含后缀
            if p_name_lower.endswith(".exe"):
                p_name_lower = p_name_lower[0:-4]

            if p_name_lower == processName:
                create_date = datetime.fromtimestamp(process.create_time())
                now_date = datetime.now()

                spend_seconds = (now_date - create_date).seconds # 检测到该进程时，该进程已经存货的时长（单位秒）
                if 0 <= spend_seconds <= 20:

                    info["status"] = process.status()
                    info["pid"] = pid
                    info["create_date"] = create_date
                    info["create_date_str"] = create_date.strftime("%Y-%m-%d %H:%M:%S")
                    # timeArray = time.localtime(int(process.create_time()))
                    # dateStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    # info["started"] = dateStr

                    info["state"] = 1


        return info
    def checkProcessByPid(self,pid):
        try:
            process = psutil.Process(pid)
            if process.status():
                return True
            else:
                return False
        except Exception as e:
            self.logger.error("checkProcessByPid %s: %s" % (str(e), str(e)))
            return False

    def stopProcessByPid(self,pid):
        try:
            process = psutil.Process(pid)
            if process.status():
                process.kill()
        except Exception as e:
            self.logger.error("stopProcessByPid %s: %s" % (str(e), str(e)))

    @staticmethod
    def detect2detect(src_detect_dir, dst_detect_dir, freq=5):
        src_detect_images_dir = os.path.join(src_detect_dir, "images")
        src_detect_labels_dir = os.path.join(src_detect_dir, "labels")

        dst_detect_images_dir = os.path.join(dst_detect_dir, "images")
        dst_detect_labels_dir = os.path.join(dst_detect_dir, "labels")

        if not os.path.exists(dst_detect_images_dir):
            os.makedirs(dst_detect_images_dir)
        if not os.path.exists(dst_detect_labels_dir):
            os.makedirs(dst_detect_labels_dir)

        train_count = 0
        valid_count = 0
        i = 0
        filenames = os.listdir(src_detect_images_dir)
        for filename in filenames:
            if i % freq == 0:
                if filename.endswith(".jpg"):
                    name = filename[0:-4]
                    src_image_path = os.path.join(src_detect_images_dir, name + ".jpg")
                    src_label_path = os.path.join(src_detect_labels_dir, name + ".txt")

                    dst_image_path = os.path.join(dst_detect_images_dir, name + ".jpg")
                    dst_label_path = os.path.join(dst_detect_labels_dir, name + ".txt")

                    try:
                        shutil.copyfile(src_image_path, dst_image_path)
                        shutil.copyfile(src_label_path, dst_label_path)

                        os.remove(src_image_path)
                        os.remove(src_label_path)
                        valid_count += 1
                    except Exception as e:
                        try:
                            os.remove(src_image_path)
                        except:
                            pass
                        try:
                            os.remove(src_label_path)
                        except:
                            pass
                        try:
                            os.remove(dst_image_path)
                        except:
                            pass
                        try:
                            os.remove(dst_label_path)
                        except:
                            pass
                else:
                    train_count += 1
            else:
                train_count += 1
            i += 1
        return train_count, valid_count