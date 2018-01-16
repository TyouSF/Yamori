import argparse
from yamori.getpage import GetPage
from yamori.findimg import FindImg
from yamori.saveimg import SaveImg

# 获取命令行内的必须执行参数
parser = argparse.ArgumentParser()

parser.add_argument('url', help='需指定网页地址')
args = parser.parse_args()

url = args.url

# 原图片地址链接
# 结构示例：[]域名](http://img.hb.aicdn.com/)+[图片key](128f1bf81808b8c6fadc1f442a0a9daa7f6d6bb21610f-3LFP5R)
img_base_url = "http://img.hb.aicdn.com/"


page = GetPage(url)
imgpage = FindImg(page.getpage())
