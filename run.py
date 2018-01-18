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
page_num = 1  # 下拉加载新页面编号

root_path = os.path.split(os.path.abspath(__name__))[0]  # 获取项目的绝对路径
img_path = os.path.join(root_path, "huabanimgs")  # 指定图片保存的路径


def run(url, total_num=0):
    page = GetPage(url)  # 获取基础花瓣网址页面源码
    imginfos = FindImg(page.page_text()).find_imginfos()  # 获取所有需要保存的图片信息

    createdir = CreateDirectory(img_path)
    img_folder = createdir.create_folder()  # 创建图片保存的文件夹

    saveimg = SaveImg(imginfos, img_folder)
    total_num = saveimg.save_img(total_num=total_num)  # 执行图片的保存
    return total_num


if __name__ == '__main__':
    total_num = run(url, total_num=0)
    while True:
        print("""当前页图片已全部抓取，请确认是否包含您所需图片。
        如果包含，且不再抓取，请输入英文字母：n，结束程序;
        如果没有，且需再抓取，请输入英文字母：y，继续抓取。""")
        to_next = input("[y/n]：")
        if to_next == 'n':
            print("程序已终止")
            break
        else:
            page_num += 1
            next_url = url + "&page={}&per_page=20".format(page_num)
            total_num = run(next_url, total_num=total_num)
