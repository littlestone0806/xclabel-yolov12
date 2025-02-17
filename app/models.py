from django.db import models
from django.utils import timezone

class Task(models.Model):
    user_id = models.IntegerField(verbose_name='用户')
    username = models.CharField(max_length=100, verbose_name='用户名')
    sort = models.IntegerField(verbose_name='排序')
    code = models.CharField(max_length=50, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='任务名称')
    task_type = models.IntegerField(verbose_name='任务类型') # 1:图片 2:视频 3:音频
    remark = models.TextField(verbose_name='扩展参数')

    sample_annotation_count = models.IntegerField(verbose_name='样本已标注数量')
    sample_count = models.IntegerField(verbose_name='样本总数量')

    labels = models.TextField(verbose_name='标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_timestamp = models.IntegerField(verbose_name='创建时间戳')
    last_update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    state = models.IntegerField(verbose_name='状态')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'xc_task'
        verbose_name = '任务'
        verbose_name_plural = '任务'

class TaskSample(models.Model):
    sort = models.IntegerField(verbose_name='排序')
    code = models.CharField(max_length=50, verbose_name='编号')
    user_id = models.IntegerField(verbose_name='用户')
    username = models.CharField(max_length=100, verbose_name='用户名')
    task_type = models.IntegerField(verbose_name='任务类型')
    task_code = models.CharField(max_length=50, verbose_name='任务编号')
    old_filename = models.CharField(max_length=200, verbose_name='原名称')
    new_filename = models.CharField(max_length=200, verbose_name='新名称')
    remark = models.CharField(max_length=100, verbose_name='备注')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    state = models.IntegerField(verbose_name='状态')  # 0:样本所属任务不存在 1:样本所属任务存在 默认0

    annotation_user_id = models.IntegerField(verbose_name='标注用户')
    annotation_username = models.CharField(max_length=100, verbose_name='标注用户名')
    annotation_time = models.DateTimeField(verbose_name='标注时间')
    annotation_content = models.TextField(verbose_name='标注内容')
    annotation_state = models.IntegerField(verbose_name='标注状态') # 0:未标注 1:已标注 默认0

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'xc_task_sample'
        verbose_name = '样本'
        verbose_name_plural = '样本'

class TaskTrain(models.Model):
    sort = models.IntegerField(verbose_name='排序')
    code = models.CharField(max_length=50, verbose_name='编号')
    user_id = models.IntegerField(verbose_name='用户')
    username = models.CharField(max_length=100, verbose_name='用户名')
    task_code = models.CharField(max_length=50, verbose_name='任务编号')
    algorithm_code = models.CharField(max_length=50, verbose_name='算法编号')
    device = models.CharField(max_length=50, verbose_name='设备')
    imgsz = models.IntegerField(verbose_name='输入尺寸')
    epochs = models.IntegerField(verbose_name='训练周期')
    batch = models.IntegerField(verbose_name='训练批次')
    save_period = models.IntegerField(verbose_name='保存周期')
    sample_ratio = models.IntegerField(verbose_name='训练验证比例')
    extra = models.TextField(verbose_name='其他参数')
    create_time = models.DateTimeField(verbose_name='create_time')
    train_datasets = models.CharField(max_length=200, verbose_name='train_datasets')
    train_datasets_remark = models.CharField(max_length=200, verbose_name='train_datasets_remark')
    train_datasets_time = models.DateTimeField(verbose_name='train_datasets_time')
    train_command = models.CharField(max_length=200, verbose_name='train_command')
    train_process_name = models.CharField(max_length=100, verbose_name='train_process_name')
    train_pid = models.IntegerField(verbose_name='train_pid')
    train_count = models.IntegerField(verbose_name='train_count')
    train_state = models.IntegerField(verbose_name='train_state')  # 0:未开启训练 1:训练中 2:已完成
    train_start_time = models.DateTimeField(verbose_name='train_start_time')
    train_stop_time = models.DateTimeField(verbose_name='train_stop_time')
    train_remark = models.CharField(max_length=200, verbose_name='train_remark')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'xc_task_train'
        verbose_name = '训练'
        verbose_name_plural = '训练'

class TaskTrainTest(models.Model):
    sort = models.IntegerField(verbose_name='排序')
    code = models.CharField(max_length=50, verbose_name='编号')
    user_id = models.IntegerField(verbose_name='用户')
    username = models.CharField(max_length=100, verbose_name='用户名')
    task_code = models.CharField(max_length=50, verbose_name='任务编号')
    train_code = models.CharField(max_length=50, verbose_name='训练编号')
    file_name = models.CharField(max_length=100, verbose_name='文件名称')
    file_size = models.IntegerField(verbose_name='文件大小')
    file_type = models.IntegerField(verbose_name='文件类型') # 0:未知 1:图片 2:视频
    calcu_seconds = models.FloatField(verbose_name='计算耗时') # 计算耗时
    create_time = models.DateTimeField(verbose_name='create_time')

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'xc_task_train_test'
        verbose_name = '测试记录'
        verbose_name_plural = '测试记录'
