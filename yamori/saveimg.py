import os
from datetime import datetime
import requests


class CreateDirectory:
    '''
    图片保存目录类
    '''

    def __init__(self, img_path):
        self.img_path = img_path

    def create_folder(self):

        # 根据日期创建图片存储的文件夹
        print("<- 开始创建图片保存根目录 “huabanimgs”...... ->")
        if not os.path.exists(self.img_path):
            os.mkdir(self.img_path)  # 本项目根目录下，创建图片保存目录
        else:
            print("<- 图片保存根目录已存在，无需创建...... ->")

        folder_name = datetime.now().strftime('%Y%m%d')

        # 基于图片目录，创建保存图片的对应日期文件夹
        img_folder = os.path.join(self.img_path, folder_name)
        print("<- 开始创建本日图片文件夹...... ->")
        if not os.path.exists(img_folder):
            os.mkdir(img_folder)
        else:
            print("<- 本日已创建对应文件夹，无需创建...... ->")

        return img_folder


class SaveImg:
    '''
    图片命名以及保存类
    '''

    def __init__(self, imginfos, img_folder):
        self.imginfos = imginfos
        self.img_folder = img_folder

    def save_img(self):
        '''
        保存图片到对应的目录下
        '''
        n = 0
        for img in self.imginfos:
            img_name = os.path.join(
                self.img_folder, '{}.jpg'.format(img['id']))
            if not os.path.exists(img_name):
                n += 1
                print("<- 正在抓取第 {} 张图片...... ->".format(n))
                r = requests.get(img['url'])
                print("<- 开始保存图片...... ->")
                with open(img_name, 'wb') as f:
                    f.write(r.content)
                    print("<- 保存成功...... ->")
            else:
                print("<- 当天图片已存在，执行跳过...... ->")
        print("<- 执行完毕，成功保存 {} 张图片...... ->".format(n))

        return True
