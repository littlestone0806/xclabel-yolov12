from logging import fatal

import psutil
from datetime import datetime
import platform
import subprocess
import os

class OSSystem():
    def __init__(self):
        self.__system_name = platform.system() # 操作系统
        self.__machine_node = str(platform.node()) # 机器名称

    def __spendDateFormat(self,spend_date):# type <class 'datetime.timedelta'>
        spend_day = spend_date.days  # 已运行的天数 int
        spend_seconds = spend_date.seconds  # 已运行的秒数 int
        spend_hour = int(spend_seconds / 60 / 60)  # 已运行小时 int
        spend_seconds -= spend_hour * 60 * 60  # 已运行的秒数 int
        spend_minute = int(spend_seconds / 60)  # 已运行的分钟 int
        spend_seconds -= spend_minute * 60  # 已运行的秒数 int
        spend_date_str = "%d天%d小时%d分钟%d秒" % (spend_day, spend_hour, spend_minute, spend_seconds)

        return spend_date_str

    def __byteFormat(self,bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def getOSInfo(self):

        # 获取系统cpu比例 start
        os_cpu_used = psutil.cpu_percent()
        # os_cpu_physical_core = psutil.cpu_count(logical=False) # 物理核心数量
        os_cpu_total_core = psutil.cpu_count(logical=True) # 逻辑核心数量
        os_cpu_used_rate = round(os_cpu_used / 100, 3)  # <class 'float'> 0.125
        # 获取系统cpu比例 end

        # 获取系统内存比例 start
        os_virtual_mem = psutil.virtual_memory()
        os_virtual_mem_total = os_virtual_mem.total
        os_virtual_mem_used_rate = os_virtual_mem.used / os_virtual_mem.total
        os_virtual_mem_used_rate = round(os_virtual_mem_used_rate, 3)  # <class 'float'> 0.635
        # 获取系统内存比例 end

        # 获取系统磁盘比例 start
        os_disk_total = 0
        os_disk_used = 0
        os_disk_free = 0
        os_disk_partitions = psutil.disk_partitions()
        for partition in os_disk_partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                os_disk_total += partition_usage.total
                os_disk_free += partition_usage.free
                os_disk_used += partition_usage.used
            except PermissionError:
                continue
        os_disk_used_rate = os_disk_used / os_disk_total
        os_disk_used_rate = round(os_disk_used_rate, 3)  # 当前系统磁盘占用比例
        # 获取系统磁盘比例 end

        # 获取系统开机时间 start
        os_boot_time = psutil.boot_time()  # <class 'float'> 1651904713.9067075
        os_boot_date = datetime.fromtimestamp(os_boot_time)  # <class 'datetime.datetime'>
        os_run_date = datetime.now() - os_boot_date  # <class 'datetime.timedelta'>
        os_run_date_str = self.__spendDateFormat(os_run_date)
        # 获取系统开机时间 end


        os_info = {
            "machine_node": str(platform.node()),
            "system_name": self.getSystemName(),
            "os_cpu_used_rate": os_cpu_used_rate,
            "os_virtual_mem_used_rate": os_virtual_mem_used_rate,
            "os_disk_used_rate": os_disk_used_rate,

            "os_cpu_used_rate_str": str(round(os_cpu_used_rate*100,1))+"% / "+str(os_cpu_total_core),
            "os_virtual_mem_used_rate_str": str(round(os_virtual_mem_used_rate*100,1))+"% / "+str(self.__byteFormat(os_virtual_mem_total)),
            "os_disk_used_rate_str": str(round(os_disk_used_rate*100,1))+"% / "+str(self.__byteFormat(os_disk_total)),

            "os_run_date_str": os_run_date_str
        }

        return os_info

    def getSystemName(self):
        return self.__system_name
    def getMachineNode(self):
        return self.__machine_node

    def getMachineCpu(self):
        if self.getSystemName() == "Windows":
            # cpu_info值示例： 11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz
            try:
                machine_cpu = subprocess.check_output("wmic cpu get Name", shell=True)
                machine_cpu = machine_cpu.decode("utf-8")
                machine_cpu = str(machine_cpu)
                machine_cpu = machine_cpu.replace("\r", "").replace("\n", "")
                if machine_cpu.startswith("Name"):
                    ms = machine_cpu.split("Name")
                    if len(ms) == 2:
                        machine_cpu = str(ms[1].strip())

            except Exception as e:
                machine_cpu = "read error"
        else:
            try:
                result = os.popen('lscpu | grep "Model name"')
                machine_cpu = str(result.read())
                if machine_cpu.startswith("Model name"):
                    ms = machine_cpu.split(":")
                    if len(ms) == 2:
                        machine_cpu = str(ms[1].strip())
            except:
                machine_cpu = "read error"

        return machine_cpu
