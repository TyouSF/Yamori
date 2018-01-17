import re


class FindImg:
    '''
    解析页面内容，并获取图片链接
    '''

    def __init__(self, pagetext):
        self.pagetext = pagetext

    def find_imginfos(self):
        '''
        提取所需要保存的图片的数据，数据整合为如下形式的一个列表：
        [
        {'id': 1281410004, 'url': 'http://img.hb.aicdn.com/128f1bf81808b8c6fadc1f442a0a9daa7f6d6bb21610f-3LFP5R'},
        {'id': 1281409968, 'url': 'http://img.hb.aicdn.com/112b6ea4df5be37ee118119e933236a49401778b22f64-T8UrUg'}
        ]
        '''

        # 正则
        pattern = re.compile(r'app\.page\["pins"\].*')

        print("<- 从网页源码提取图片数据...... ->")
        # 根据正则，从script中提取包含pins的内容
        pins_str = pattern.findall(self.pagetext)[0].replace('null', 'None').replace(
            'true', 'True')[19:-1]

        # 转换成python内置数据类型，方便操作
        pins_list = eval(pins_str)

        # 原图片地址链接
        # 结构示例：[]域名](http://img.hb.aicdn.com/)+[图片key](128f1bf81808b8c6fadc1f442a0a9daa7f6d6bb21610f-3LFP5R)
        img_base_url = 'http://img.hb.aicdn.com/'

        print("<- 组装图片链接地址...... ->")
        # 使用列表推导，快速取出图片链接信息
        imginfos = [{'id': i['pin_id'], 'url': img_base_url + i['file']['key']}
                    for i in pins_list]
        print("<- 组装完毕，等待创建存储路径...... ->")

        return imginfos
