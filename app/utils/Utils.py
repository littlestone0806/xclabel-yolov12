import uuid
import random
import datetime, time
import os
import re
import platform
import math
import base64
import random

def xc_gen_random_code(prefix="rand"):
    """
    产生永远不重复的random_code
    :param prefix: 编码前缀
    :return:
    """
    d= time.strftime("%Y%m%d%H%M%S")
    # d = time.strftime("%Y%m%d")
    val = str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1())))
    a = val.split("-")[0]
    random_code = "%s%s%s%d" % (prefix, d, a, random.randint(100000, 999999))
    return random_code


"""
将total_count相对均匀的分配在num个数值中，要求尽可能均匀分配
"""
def even_distribution(total_count,num):
    __vals = []
    __val = round(total_count / num) # 四舍五入
    for i in range(num-1):
        __vals.append(__val)
    __last_val = total_count - sum(__vals)
    if __last_val > 0:
        __vals.append(__last_val)
    else:
        # 四舍五入时，最后一个值小于等于0，则使用全舍法
        __vals = []
        __val = math.floor(total_count / num) # 全舍法
        for i in range(num - 1):
            __vals.append(__val)
        __last_val = total_count - sum(__vals)
        __vals.append(__last_val)
    return __vals


def classify_data(data, pid, level=0):
    result = []

    for v in data:
        if v["pid"] == pid:
            v["level"] = level

            if "childs" not in v.keys():
                v["childs"] = []

            inner_result = classify_data(data, v["id"], level + 1)

            if inner_result:
                for inner_v in inner_result:
                    v["childs"].append(inner_v)

            result.append(v)

    return result


def buildPageLabels(page, page_num):
    """
    :param page: 当前页面
    :param page_num: 总页数
    :return:
    返回式例：
        [{'page': 1, 'name': 1, 'cur': True}, {'page': 2, 'name': 2, 'cur': False}, {'page': 2, 'name': '下一页'}]

    """

    pageLabels = []
    if page > 1:
        pageLabels.append({
            "page": 1,
            "name": "首页"
        })
        pageLabels.append({
            "page": page - 1,  # 当前页点击时候触发的页数
            "name": "上一页"
        })
    if page == 1:
        pageArray = [1, 2, 3, 4]
    else:
        pageArray = list(range(page - 1, page + 3))  # page-1,page,page+1,page+2

    for p in pageArray:
        if p <= page_num:
            if page == p:
                cur = 1
            else:
                cur = 0
            pageLabels.append({
                "page": p,
                "name": p,
                "cur": cur
            })

    if page + 1 <= page_num:
        pageLabels.append({
            "page": page + 1,
            "name": "下一页"
        })
    if page_num > 0:
        pageLabels.append({
            "page": page_num,
            "name": "尾页"
        })
    return pageLabels



def gen_random_code_s(prefix,version=None):
    if version == 1:
        code = "%s%s%d" % (prefix, datetime.datetime.now().strftime('%Y%m%d%H%M%S'), random.randint(100, 999))
    else:
        val = str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1())))
        a = val.split("-")[0]
        a = str(a)[0:6]
        code = "%s%d%s" % (prefix, random.randint(1000, 9999), a)
    return code

def gen_random_code(prefix):
    """
    产生永远不重复的随机数
    :param prefix: 编码前缀
    :return:
    """
    # d= self.get_datetime_format("%Y%m%d%H%M%S")
    d = time.strftime("%Y%m%d")

    val = str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1())))
    a = val.split("-")[0]
    code = "%s_%s_%s%d" % (prefix, d, a, random.randint(100, 999))

    return code


def gen_dateList_startAndEnd(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []

    curr_date = start_date
    while curr_date != end_date:
        # t="%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day)

        result.append({
            "ym": "%04d-%02d" % (curr_date.year, curr_date.month),
            "ymd": curr_date
        })

        curr_date += datetime.timedelta(1)
    # result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))

    return result

def validate_chinese(s):
    for char in s:
        if '\u4e00' <= char <= '\u9fa5':
            return True
    return False

def validate_email(s):
    ex_email = re.compile(r'(^[\w][a-zA-Z0-9.]{4,19})@[a-zA-Z0-9]{2,10}.com')
    r = ex_email.match(s)

    if r:
        return True
    else:
        return False

def validate_tel(s):
    ex_tel = re.compile(r'(^[0-9\-]{11,15})')
    r = ex_tel.match(s)

    if r:
        return True
    else:
        return False
