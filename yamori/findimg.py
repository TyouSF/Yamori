import re


class FindImg:
    '''
    解析页面内容，并获取图片链接
    '''

    def __init__(self, pagetext):
        self.pagetext = pagetext

    def findimg_id(self):
        pattern = re.compile(r'app\.page\["pins"\].*')  # 正则
        pinsstr = pattern.findall(self.pagetext)[0].replace(
            'null', 'None').replace('true', 'True')  # 根据正则，从script中提取包含pins的内容
        pinslist = eval(pinsstr)  # 转换成python内置数据类型，方便操作
        pin_id_list = [i['pin_id'] for i in pinslist]

        return pin_id_list
