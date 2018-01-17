import requests


class GetPage:
    '''
    获取抓取页面
    '''

    def __init__(self, urlpath):
        '''
        指定抓取页面地址，参数：urlpath
        '''
        self.urlpath = urlpath

    def page_text(self):
        '''
        返回基础页面信息
        '''

        print("<- 抓取网页源码...... ->")
        html_page = requests.get(self.urlpath)

        return html_page.text
