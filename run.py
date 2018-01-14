import argparse
from yamori.getpage import GetPage
from yamori.findimg import FindImg
from yamori.saveimg import SaveImg

# 获取命令行内的必须执行参数
parser = argparse.ArgumentParser()

parser.add_argument('url', help='需指定网页地址')
args = parser.parse_args()

url = args.url

base_url = "https://huaban.com"


page = GetPage(url)
imgpage = FindImg(page.getpage())