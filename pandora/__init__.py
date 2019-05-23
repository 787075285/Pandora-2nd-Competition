from flask import Flask
from flask import render_template
import requests
from lxml import etree
import json
from flask import request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello, world!"

    # TODO: 捕获 404 错误，返回 404.html
    @app.errorhandler(404)
    def page_not_found(error):
        """
        以此项目中的404.html作为此Web Server工作时的404错误页
        """
        return render_template("404.html"),404
        

    # TODO: 完成接受 HTTP_URL 的 picture_reshape
    # TODO: 完成接受相对路径的 picture_reshape
    @app.route('/pic', methods=['GET'])
    def picture_reshape():
        if request.method == 'GET':
            show_the_login_form()
        """
        **请使用 PIL 进行本函数的编写**
        获取请求的 query_string 中携带的 b64_url 值
        从 b64_url 下载一张图片的 base64 编码，reshape 转为 100*100，并开启抗锯齿（ANTIALIAS）
        对 reshape 后的图片分别使用 base64 与 md5 进行编码，以 JSON 格式返回，参数与返回格式如下
        
        :param: b64_url: 
            本题的 b64_url 以 arguments 的形式给出，可能会出现两种输入
            1. 一个 HTTP URL，指向一张 PNG 图片的 base64 编码结果
            2. 一个 TXT 文本文件的文件名，该 TXT 文本文件包含一张 PNG 图片的 base64 编码结果
                此 TXT 需要通过 SSH 从服务器中获取，并下载到`pandora`文件夹下，具体请参考挑战说明
        
        :return: JSON
        {
            "md5": <图片reshape后的md5编码: str>,
            "base64_picture": <图片reshape后的base64编码: str>
        }
        """
        import PIL
        pass

    # TODO: 爬取 996.icu Repo，获取企业名单
    @app.route('/996')
    def company_996():
        """
        从 github.com/996icu/996.ICU 项目中获取所有的已确认是996的公司名单，并

        :return: 以 JSON List 的格式返回，格式如下
        [{
            "city": <city_name 城市名称>,
            "company": <company_name 公司名称>,
            "exposure_time": <exposure_time 曝光时间>,
            "description": <description 描述>
        }, ...]
        """
        html = requests.get("https://github.com/996icu/996.ICU/blob/master/blacklist/README.md")
        # print html.text
        etree_html = etree.HTML(html.text)
        content1 = etree_html.xpath('//*[@id="readme"]/article/table[2]/tbody/tr[*]/td[1]/text()')
        content2 = etree_html.xpath('//*[@id="readme"]/article/table[2]/tbody/tr[*]/td[2]/a/text()')
        content2a = etree_html.xpath('//*[@id="readme"]/article/table[2]/tbody/tr[*]/td[2]/text()')
        content2 +=content2a
        content3 = etree_html.xpath('//*[@id="readme"]/article/table[2]/tbody/tr[*]/td[3]/text()')
        content4 = etree_html.xpath('//*[@id="readme"]/article/table[2]/tbody/tr[*]/td[4]/text()')
        content4[102]+=content4[103]
        del content4[103]
        i = len(content1)
        j = 0
        list1=[]
        while i >j:
            data={}
            data["city"]=content1[j]
            data["company"]=content2[j]
            data["exposure_time"]=content3[j]
            data["description"]=content4[j]
            list1.append(data)
            j+=1
        return json.dumps(list1)

        

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
