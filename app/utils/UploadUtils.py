import random
import time
from datetime import datetime
import os
import shutil
import cv2
import json

class UploadUtils():
    # 上传模型测试文件-图片
    def upload_model_test_image(self, test_save_dir, file):
        ret = False
        msg = "未知错误"
        info = {}

        try:
            file_name = file.name  # 上传文件的名称
            file_size = file.size  # 上传文件的字节大小 1M = 1024*1024, 100M = 100*1024*1024 = 104857600
            file_size_m = int(file_size / 1024 / 1024)
            file_content_type = file.content_type  # 上传文件的 content_type [wav->audio/wav , mp3->audio/mpeg]
            info = {
                "file_name": file_name,  # 上传文件的原始name
                "file_size": file_size,  # 上传文件的原始size
                "file_content_type": file_content_type
            }
            if file_size_m <= 10:
                if 'image/png' == file_content_type or 'image/jpeg' == file_content_type or 'image/jpg' == file_content_type:
                    test_filepath = os.path.join(test_save_dir, file_name)
                    # 图片写入本地start
                    f = open(test_filepath, 'wb')
                    f.write(file.read())
                    f.close()
                    # 图片写入本地end
                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "test_filepath": test_filepath
                    }
                    ret = True
                    msg = "success"
                else:
                    msg = "图片文件格式必须是png,jpg,jpeg"
            else:
                msg = "上传图片文件不能超过10M:" + str(file_size_m)
        except Exception as e:
            msg = str(e)
        return ret, msg, info
    # 上传模型测试文件-视频
    def upload_model_test_video(self, test_save_dir, file):
        ret = False
        msg = "未知错误"
        info = {}

        try:
            file_name = file.name  # 上传文件的名称
            file_size = file.size  # 上传文件的字节大小 1M = 1024*1024, 100M = 100*1024*1024 = 104857600
            file_size_m = int(file_size / 1024 / 1024)
            file_content_type = file.content_type  # 上传文件的 content_type [wav->audio/wav , mp3->audio/mpeg]
            info = {
                "file_name": file_name,  # 上传文件的原始name
                "file_size": file_size,  # 上传文件的原始size
                "file_content_type": file_content_type
            }
            if file_size_m <= 200:
                if file_name.endswith(".avi") or file_name.endswith(".flv") or file_name.endswith(".mp4"):

                    test_filepath = os.path.join(test_save_dir, file_name)
                    # 视频写入本地start
                    f = open(test_filepath, 'wb')
                    f.write(file.read())
                    f.close()
                    # 视频写入本地end
                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "test_filepath": test_filepath
                    }
                    ret = True
                    msg = "success"
                else:
                    msg = "视频文件格式必须是avi,flv,mp4"
            else:
                msg = "上传视频文件不能超过200M:" + str(file_size_m)
        except Exception as e:
            msg = str(e)
        return ret, msg, info
    # 上传样本文件-图片
    def upload_sample_image(self, storageDir, task_code, file):
        ret = False
        msg = "未知错误"
        info = {}

        try:
            file_name = file.name  # 上传文件的名称
            file_size = file.size  # 上传文件的字节大小 1M = 1024*1024, 100M = 100*1024*1024 = 104857600
            file_size_m = int(file_size / 1024 / 1024)
            file_content_type = file.content_type  # 上传文件的 content_type [wav->audio/wav , mp3->audio/mpeg]

            info = {
                "file_name": file_name,  # 上传文件的原始name
                "file_size": file_size,  # 上传文件的原始size
                "file_content_type": file_content_type
            }

            if file_size_m <= 20:
                if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):

                    sample_dir = "%s/task/%s/sample" % (storageDir, task_code)
                    if not os.path.exists(sample_dir):
                        os.makedirs(sample_dir)
                    __suffix = file_name.split(".")[-1]  # 上传原文件后缀 例如 .jpg,.png,.jpeg
                    if __suffix == "jpg":
                        __ymd_hms_str = datetime.now().strftime("%Y%m%d%H%M%S")
                        new_filename = "%s_%s" % (__ymd_hms_str, file_name)
                        new_filename_abs = os.path.join(sample_dir, new_filename)  # 存储上传文件的绝对路径

                        # 图片写入本地start
                        f = open(new_filename_abs, 'wb')
                        f.write(file.read())
                        f.close()
                        # 图片写入本地end
                    else:
                        __ymd_hms_str = datetime.now().strftime("%Y%m%d%H%M%S")
                        # image_name = "%s.%s" % (__ymd_hms_str, __suffix)
                        temp_new_filename = "%s_%s" % (__ymd_hms_str, file_name)
                        temp_new_filename_abs = os.path.join(sample_dir, temp_new_filename)  # 存储上传文件的绝对路径

                        # 图片写入本地start
                        f = open(temp_new_filename_abs, 'wb')
                        f.write(file.read())
                        f.close()
                        # 图片写入本地end

                        # 非jpg结尾的图片转换为jpg文件

                        __name = file_name[:-4]
                        new_filename = "%s_%s" % (__ymd_hms_str, "%s.jpg" % __name)
                        new_filename_abs = os.path.join(sample_dir, new_filename)  # 存储上传文件的绝对路径
                        temp_image = cv2.imread(temp_new_filename_abs)
                        cv2.imwrite(new_filename_abs, temp_image)
                        os.remove(temp_new_filename_abs)

                    ret = True
                    msg = "success"

                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "old_filename": file_name,
                        "new_filename": new_filename
                    }

                else:
                    msg = "图片文件格式必须是png,jpg,jpeg"
            else:
                msg = "上传图片文件不能超过20M:" + str(file_size_m)
        except Exception as e:
            msg = str(e)
        return ret, msg, info

    # 上传样本文件-视频
    def upload_sample_video(self, storageDir, task_code, file, saveInterval=0):
        ret = False
        msg = "未知错误"
        info = {}

        try:
            file_name = file.name  # 上传文件的名称
            file_size = file.size  # 上传文件的字节大小 1M = 1024*1024, 100M = 100*1024*1024 = 104857600
            file_size_m = int(file_size / 1024 / 1024)
            file_content_type = file.content_type  # 上传文件的 content_type [wav->audio/wav , mp3->audio/mpeg]
            info = {
                "file_name": file_name,  # 上传文件的原始name
                "file_size": file_size,  # 上传文件的原始size
                "file_content_type": file_content_type
            }
            if file_size_m <= 500:
                if file_name.endswith(".avi") or file_name.endswith(".flv") or file_name.endswith(".mp4"):

                    sample_dir = "%s/task/%s/sample" % (storageDir, task_code)
                    if not os.path.exists(sample_dir):
                        os.makedirs(sample_dir)
                    __ymd_hms_str = datetime.now().strftime("%Y%m%d%H%M%S")
                    video_filename = "%s_%s" % (__ymd_hms_str, file_name)
                    video_filename_abs = os.path.join(sample_dir, video_filename)  # 存储上传文件的绝对路径

                    # 视频写入本地start
                    f = open(video_filename_abs, 'wb')
                    f.write(file.read())
                    f.close()
                    # 视频写入本地end

                    # 分割视频为图片start
                    new_filenames = []
                    image_filename_prefix = "%s_%s" % (__ymd_hms_str, "frame")
                    cap = cv2.VideoCapture(video_filename_abs)
                    fps = cap.get(cv2.CAP_PROP_FPS)  # 视频FPS
                    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    if saveInterval == 0:
                        saveInterval = fps
                    frame_count = 0
                    while True:
                        read_video_ret, frame = cap.read()
                        if read_video_ret:
                            frame_count += 1
                            if frame_count % saveInterval == 0:
                                new_filename = image_filename_prefix + str(frame_count) + ".jpg"
                                image_filename_abs = os.path.join(sample_dir, new_filename)
                                cv2.imwrite(image_filename_abs, frame)
                                new_filenames.append(new_filename)
                        else:
                            break

                    cap.release()
                    # 分割视频为图片end


                    os.remove(video_filename_abs)

                    ret = True
                    msg = "success"

                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "old_filename": file_name,
                        "new_filenames": new_filenames
                    }

                else:
                    msg = "视频文件格式必须是avi,flv,mp4"
            else:
                msg = "上传视频文件不能超过500M:" + str(file_size_m)
        except Exception as e:
            msg = str(e)
        return ret, msg, info

    # 上传样本文件-labelme
    def upload_sample_labelme(self, storageDir, task_code, file):
        ret = False
        msg = "未知错误"
        info = {}

        try:
            file_name = file.name  # 上传文件的名称
            file_size = file.size  # 上传文件的字节大小 1M = 1024*1024, 100M = 100*1024*1024 = 104857600
            file_size_m = int(file_size / 1024 / 1024)
            file_content_type = file.content_type  # 上传文件的 content_type [wav->audio/wav , mp3->audio/mpeg]

            info = {
                "file_name": file_name,  # 上传文件的原始name
                "file_size": file_size,  # 上传文件的原始size
                "file_content_type": file_content_type
            }

            if file_size_m <= 20:
                sample_dir = "%s/task/%s/sample" % (storageDir, task_code)
                if not os.path.exists(sample_dir):
                    os.makedirs(sample_dir)

                file_name_suffix = file_name.split(".")[-1]  # 上传原文件后缀 例如 .jpg,.png,.jpeg
                if file_name_suffix == "jpg":
                    file_name_prefix = file_name[0:-4]

                    __ymd_hms_str = datetime.now().strftime("%Y%m%d%H%M%S")
                    new_filename = "%s_%s" % (__ymd_hms_str, file_name)
                    new_filename_abs = os.path.join(sample_dir, new_filename)  # 存储上传文件的绝对路径

                    # 图片写入本地start
                    f = open(new_filename_abs, 'wb')
                    f.write(file.read())
                    f.close()
                    # 图片写入本地end

                    ret = True
                    msg = "success"

                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "old_filename": file_name,
                        "old_filename_prefix": file_name_prefix,
                        "old_filename_suffix": file_name_suffix,
                        "new_filename": new_filename
                    }

                elif file_name_suffix == "json":
                    file_name_prefix = file_name[0:-5]
                    # 读取json内容start
                    json_content = file.read()
                    json_data = json.loads(json_content)
                    version = json_data.get("version")
                    shapes = json_data.get("shapes")
                    imagePath = json_data.get("imagePath")
                    imageWidth = json_data.get("imageWidth")
                    imageHeight = json_data.get("imageHeight")

                    annotation = {
                        "version": version,
                        "shapes": shapes,
                        "imagePath": imagePath,
                        "imageWidth": imageWidth,
                        "imageHeight": imageHeight
                    }
                    # 读取json内容end

                    ret = True
                    msg = "success"

                    info = {
                        "file_name": file_name,  # 上传文件的原始name
                        "file_size": file_size,  # 上传文件的原始size
                        "old_filename": file_name,
                        "old_filename_prefix": file_name_prefix,
                        "old_filename_suffix": file_name_suffix,
                        "annotation": annotation
                    }
                else:
                    msg = "文件格式必须是jpg,json"
            else:
                msg = "上传文件不能超过20M:" + str(file_size_m)
        except Exception as e:
            msg = str(e)
        return ret, msg, info
