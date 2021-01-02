import requests
import base64
import json
import sys
import os
import hashlib
from Crypto.Cipher import AES
import logging
import coloredlogs


class AutoLogin:
    """
    网易云自动签到
    """
    def __init__(self, username="", password="", SCK=""):
        self.logger = logging.getLogger(__name__)
        coloredlogs.install(loggger=self.logger, level="INFO")
        self.username = username
        self.password = password
        self.SCK = SCK
        self.LOG_INFO = ""

    # NOTE 输出调试信息
    def log(self, content, status_code=3):
        if status_code == 1:
            self.logger.warning(str(content))
        elif status_code == 2:
            self.logger.error(str(content))
        else:
            self.logger.info(str(content))
        self.LOG_INFO = self.LOG_INFO + str(content) + '\n\n'

    # NOTE 加密
    def encrypt(self, key, text):
        cryptor = AES.new(key.encode('utf8'), AES.MODE_CBC,
                          b'0102030405060708')
        length = 16
        count = len(text.encode('utf-8'))
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 16
        pad = chr(add)
        text1 = text + (pad * add)
        ciphertext = cryptor.encrypt(text1.encode('utf8'))
        cryptedStr = str(base64.b64encode(ciphertext), encoding='utf-8')
        return cryptedStr

    # NOTE MD5
    def md5(self, str):
        hl = hashlib.md5()
        hl.update(str.encode(encoding='utf-8'))
        return hl.hexdigest()

    # NOTE 保存密文
    def protect(self, text):
        return {
            "params":
            self.encrypt('TA3YiYCfY2dDJQgg',
                         self.encrypt('0CoJUm6Qyw8W8jud', text)),
            "encSecKey":
            "84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210"
        }

    # NOTE 发送提示信息
    def send_msg(self, title="网易云音乐签到信息", msg="", SCK=""):
        if SCK == "":
            pass
        else:
            data = {"text": title, "desp": msg}
            res = requests.post(url='https://sc.ftqq.com/' + SCK + ".send",
                                data=data)
            if res.status_code == 200:
                self.log('> 发送通知成功')
            else:
                self.log('> 发送通知失败', status_code=2)

    # NOTE 处理帐号密码
    def deal_username_password(self):
        """
        处理输入数据
        """
        username_list = self.username.split("#")
        password_list = self.password.split("#")
        # OUTPUT 调试使用
        # self.log(username_list)
        # self.log(password_list)
        if (len(username_list) != len(password_list)):
            self.log("> 帐号密码数量不匹配，密码中包含间隔符#,如果密码中包含#请更改密码，或者手动修改脚本",
                     status_code=2)

        for username, password in zip(username_list, password_list):
            self.log("> 帐号 {} 开始执行".format(username))
            try:
                self.start(username=username, password=password)
                self.log("> 帐号 {} 执行完毕".format(username))
            except AttributeError:
                self.log("> 帐号 {} 执行出现问题".format(username))
                pass
            self.log("==")
        self.send_msg(msg=self.LOG_INFO, SCK=self.SCK)

    # NOTE 主函数
    # INFO server_SCK 为server酱的KEY
    def start(self, username="", password=""):
        s = requests.Session()
        header = {}
        url = "https://music.163.com/weapi/login/cellphone"
        url2 = "https://music.163.com/weapi/point/dailyTask"
        url3 = "https://music.163.com/weapi/v1/discovery/recommend/resource"
        logindata = {
            "phone": username,
            "countrycode": "86",
            "password": self.md5(password),
            "rememberLogin": "true",
        }
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            "Referer": "http://music.163.com/",
            "Accept-Encoding": "gzip, deflate",
        }
        headers2 = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            "Referer":
            "http://music.163.com/",
            "Accept-Encoding":
            "gzip, deflate",
            "Cookie":
            "os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; channel=netease; __remember_me=true;"
        }

        res = s.post(url=url,
                     data=self.protect(json.dumps(logindata)),
                     headers=headers2)
        tempcookie = res.cookies
        ans = json.loads(res.text)
        if ans['code'] == 200:
            self.log("> 登录成功！")
        else:
            self.log("> 登录失败！请检查密码是否正确！" + str(ans['code']), status_code=2)
            self.self.send_msg(msg=self.LOG_INFO, SCK=self.SCK)
            # exit(ans['code'])

        res = s.post(url=url2,
                     data=self.protect('{"type":0}'),
                     headers=headers)
        ans = json.loads(res.text)
        if ans['code'] != 200 and ans['code'] != -2:
            self.log("> 签到时发生错误：" + ans['msg'], status_code=2)
        else:
            if ans['code'] == 200:
                self.log("> 签到成功，经验+" + str(ans['point']))
            else:
                self.log("> 重复签到", status_code=1)

        res = s.post(
            url=url3,
            data=self.protect(
                '{"csrf_token":"' +
                requests.utils.dict_from_cookiejar(tempcookie)['__csrf'] +
                '"}'),
            headers=headers)
        ans = json.loads(res.text, strict=False)
        for x in ans['recommend']:
            url = 'https://music.163.com/weapi/v3/playlist/detail?csrf_token=' + requests.utils.dict_from_cookiejar(
                tempcookie)['__csrf']
            data = {
                'id':
                x['id'],
                'n':
                1000,
                'csrf_token':
                requests.utils.dict_from_cookiejar(tempcookie)['__csrf'],
            }
            res = s.post(url, self.protect(json.dumps(data)), headers=headers)
            ans = json.loads(res.text, strict=False)
            buffer = []
            count = 0
            for j in ans['playlist']['trackIds']:
                data2 = {}
                data2["action"] = "play"
                data2["json"] = {}
                data2["json"]["download"] = 0
                data2["json"]["end"] = "playend"
                data2["json"]["id"] = j["id"]
                data2["json"]["sourceId"] = ""
                data2["json"]["time"] = "240"
                data2["json"]["type"] = "song"
                data2["json"]["wifi"] = 0
                buffer.append(data2)
                count += 1
                if count >= 310:
                    break
            if count >= 310:
                break
        url = "http://music.163.com/weapi/feedback/weblog"
        postdata = {"logs": json.dumps(buffer)}
        res = s.post(url, self.protect(json.dumps(postdata)))
        ans = json.loads(res.text, strict=False)
        if ans['code'] == 200:
            log_info = "> 刷单成功！共" + str(count) + "首"
            self.log(log_info)
            # self.send_msg(msg=self.LOG_INFO, SCK=self.SCK)
            # exit()
        else:
            log_info = "> 发生错误：" + str(ans['code']) + ans['message']
            self.log(log_info, status_code=2)
            # self.send_msg(msg=self.LOG_INFO, SCK=self.SCK)
            exit(ans['code'])

    def index(self):
        """
        程序入口
        """
        self.log("==")
        self.log("##### 程序开始执行")
        self.log("==")
        self.deal_username_password()


if __name__ == "__main__":
    USER = os.environ.get("WYY_USER")
    PWD = os.environ.get("WYY_PWD")
    SCK = os.environ.get("SERVER_SCK")

    AL = AutoLogin(USER, PWD, SCK)
    AL.index()
