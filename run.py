import os
import argparse
from yamori.getpage import GetPage
from yamori.findimg import FindImg
from yamori.saveimg import CreateDirectory, SaveImg

# 获取命令行内的必须执行参数
parser = argparse.ArgumentParser()

parser.add_argument('url', help='需指定网页地址')
args = parser.parse_args()


url = args.url  # 获取花瓣网页地址

root_path = os.path.split(os.path.abspath(__name__))[0]  # 获取项目的绝对路径
img_path = os.path.join(root_path, "huabanimgs")  # 指定图片保存的路径

page = GetPage(url)  # 获取基础花瓣网址页面源码
imginfos = FindImg(page.page_text()).find_imginfos()  # 获取所有需要保存的图片信息

createdir = CreateDirectory(img_path)
img_folder = createdir.create_folder()  # 创建图片保存的文件夹

saveimg = SaveImg(imginfos, img_folder)
saveimg.save_img()  # 执行图片的保存
