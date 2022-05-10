#-- coding:utf-8 --
import time
import requests
import pandas as pd
import os
import re
import webbrowser
import random
import urllib.request
import urllib.parse
import urllib.request
import urllib.parse
import ssl
import ast
import urllib.request
import urllib.parse
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# urllib3.contrib.pyopenssl.inject_into_urllib3()
import gzip
import numpy as np
import hashlib
"""a = data.loc['B','网址']
#所有关键词获取:
allword = data2.loc[:,'关键词']
print(allword)
print(data2.index[0])#获取索引为0的值
pat = str(data2.index)
print(pat)
rst = re.compile("stop=(\d)").findall(pat)
print(rst[0])"""
sbtime = 0
print("-" * 50 )
print("     _       ___   _____   _   _   __    __")
print("    | |     /   | /  ___| | | / /  \ \  / /")
print("    | |    / /| | | |     | |/ /    \ \/ /")
print("_   | |   / /_| | | |     | |\ \     \  /")
print("| |_| |  / /  | | | |___  | | \ \    / /")
print("\_____/ /_/   |_| \_____| |_|  \_\  /_/     ")
print("-" * 50 )
print("AI Miyu 1.6 版本")
print("Miyu:你好，我是Miyu你的私人助理")
while (True):
    data = pd.read_excel("ddd.xlsx")  # 索引为用关键词
    data2 = pd.read_excel("ddd.xlsx")  # 索引为用数字
    aaa = data.set_index('关键词', inplace=True)
    speak = input("Miyu:你想做什么呢?或者使用命令/help获取帮助")
    if(speak == ""):
        sbtime = sbtime+1
        if (sbtime > 30):
            print("您是有什么大病吗?")
    elif("找一些" in speak and "图片" in speak):
        if("图片p" in speak or "图片P" in speak):
            pic =re.findall("找一些(.*)的图片",speak)
            page = int(input("要第几页?"))
            savepath = input("保存路径? (一定要写对,最后别加/，注意她不能创建文件夹，请指定一个已经存在的文件夹)或默认D:/graph")
            if(savepath == ""):
                savepath = "D:\graph"
            pic = pic[0]
            print(pic)
            pic = urllib.parse.quote(pic)
            cookie = str(data.loc["pic_cookie", '网址'])
            url = "https://www.pixiv.net/ajax/search/artworks/" + pic + "?word=" + pic + "&order=date_d&mode=all&p=" + str(page) + "&s_mode=s_tag&type=all&lang=zh"
            headers = {
                'Referer': url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'cookie': cookie,
                'x-user-id': '62895271'}
            req = urllib.request.Request(url=url, headers=headers)
            response1 = urllib.request.urlopen(req, timeout=15)
            response = response1.read().decode("utf-8")
            uid = re.compile('id":"(\d{8})').findall(str(response))
            num = 0
            print("将保存到" + savepath)
            for id in uid:
                print("第",str(num+1),"张, id为 : ",uid[num])
                p_uid = uid[num]
                url = "http://embed.pixiv.net/decorate.php?illust_id=" + p_uid + "&mode=sns-automator"
                headers = {
                    'authority': 'www.pixiv.net',
                    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'x-requested-with': 'XMLHttpRequest',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'cookie': cookie
                }
                urllib.request.urlretrieve(url, savepath + "\\" + p_uid + ".jpg")
                time.sleep(random.randint(3.0, 9.0))
                num = num + 1
            response1.close()
        if ("图片D" in speak or "图片d" in speak):
            pic = re.findall("找一些(.*)的图片", speak)
            # page = int(input("要第几页?"))
            savepath = input("保存路径? (一定要写对,最后别加/，注意她不能创建文件夹，请指定一个已经存在的文件夹)或默认D:/graph")
            if (savepath == ""):
                savepath = "D:\graph"
            pic = pic[0]
            print(pic)
            pic = urllib.parse.quote(pic)
            url = "https://www.duitang.com/search/?kw=" + pic + "&type=feed"
            headers = {
                'Referer': url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                # 'cookie': cookie,
                }
            req = urllib.request.Request(url=url, headers=headers)
            response1 = urllib.request.urlopen(req, timeout=15)
            response = response1.read().decode("utf-8")
            pat = 'src="(.*?)" height='
            data_durl = re.compile(pat).findall(response)
            aisdd = 0
            if (len(data_durl) == 0):
                print("没找到相关图片哦 >-<")
            else:
                print("解析完成,大约" + str(len(data_durl)) + "张图")
                for picd_len in data_durl:
                    picd_len = picd_len.replace('.thumb.400_0','')
                    urllib.request.urlretrieve(picd_len, savepath + "/" + str(aisdd + 1) + ".jpg")
                    print("完成" + str(aisdd + 1))
                    aisdd += 1
                    time.sleep(random.randint(1, 7))
        if ("图片h" in speak or "图片H" in speak):
            pic = re.findall("找一些(.*)的图片", speak)
            page = int(input("要几页(一定要为偶数)?,且会有少许误差"))
            savepath = input("保存路径? (一定要写对,最后别加/，注意她不能创建文件夹，请指定一个已经存在的文件夹)或默认D:/graph")
            if (savepath == ""):
                savepath = "D:\graph"
            pic = pic[0]
            print(pic)
            pic = urllib.parse.quote(pic)
            url = "https://api.huaban.com/search?q=" + pic + "&sort=all&per_page=" + str(page/2) + "&page=1&hide_other_count=1"
            headers = {
                'Referer': url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                # 'cookie': cookie,
            }
            req = urllib.request.Request(url=url, headers=headers)
            response1 = urllib.request.urlopen(req, timeout=15)
            response = response1.read().decode("utf-8")
            pat = '"key":"(.*?)","type"'
            data_durl = re.compile(pat).findall(response)
            aisdd = 0
            if (len(data_durl) == 0):
                print("没找到相关图片哦 >-<")
            else:
                print("解析完成,大约" + str(len(data_durl)) + "张图")
                for picd_len in data_durl:
                    picd_len = "https://hbimg.huaban.com/" + picd_len + "_fw658/format/webp"
                    urllib.request.urlretrieve(picd_len, savepath + "/" + str(aisdd+1) + "and" + str(random.randint(0,1000)) + ".jpg")
                    print("完成" + str(aisdd + 1))
                    aisdd += 1
                    time.sleep(random.randint(1, 7))
        else:
            print("正在使用百度图片搜索,因技术原因只能搜出前30张")
            savepath2 = input("保存路径? (一定要写对,最后别加/，注意她不能创建文件夹，请指定一个已经存在的文件夹)或默认D:/graph")
            if (savepath2 == ""):
                savepath2 = "D:\graph"
            pic_bai = input("要找什么图片呢")
            pic_bai = urllib.parse.quote(pic_bai)
            cookie = str(data.loc["baidupic_cookie", '网址'])
            url = "https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=" + pic_bai
            headers = {
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'referer': url,
                'Host': 'image.baidu.com',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': cookie
            }
            req = urllib.request.Request(url=url, headers=headers)
            data_bai = urllib.request.urlopen(req, timeout=5)
            data_bai = data_bai.read().decode('utf-8')
            data_bai = re.findall('"objURL":"(.*?)",', data_bai, re.S)
            # data_bai = re.compile(pat2).findall(data_bai)
            aisd = 0
            if(len(data_bai) == 0):
                print("没找到相关图片哦 >-<")
            else:
                print("解析完成,大约" + str(len(data_bai)) + "张图")
                for picb_len in data_bai:
                    urllib.request.urlretrieve(picb_len, savepath2 + "/" + str(aisd + 1) + ".jpg")
                    print("完成" + str(aisd + 1))
                    aisd += 1
                    time.sleep(random.randint(1, 7))
    elif("杨子琪" in speak or "yzq" in speak or "ymq" in speak or "杨某琪" in speak or "某琪" in speak or "某肥" in speak):
        print("别提那个傻子")
        print("想到它我就来气")
    elif ("杨某" in speak):
        print("你想说杨某肥还是杨某琪?")
        print("反正都是傻瓜一个")
    elif (("音乐" in speak and "放" in speak) or ("歌" in speak and "放" in speak) or  ("歌" in speak and "点" in speak) or  ("音乐" in speak and "点" in speak) or ("音乐" in speak and "来" in speak) or ("歌" in speak and "来" in speak)):
        print("好的,音乐文件夹默认为D:/music,关键词为music_open。若需要更改请在开始页面输入/add进行更改")
        webdata = str(data.loc["music_open", '网址'])
        print("正在随机播放一首歌")
        dic_list = os.listdir(webdata)
        file_open = random.choice(dic_list)
        file_open = webdata + "/" + file_open
        webbrowser.open(file_open, new=0, autoraise=True)
        """basedir = webdata
        file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
        print("Playing file {}...".format(file))
        webbrowser.open(os.path.join(basedir, file))"""#另外一种达到随机播放音乐的目的
    elif("你好" in  speak):
        print("你好呀")
        print("有什么能帮助到你的吗")
    elif ("放" in speak and "首" in speak and "歌" not in speak):
        song = re.compile("首(.*)").findall(speak)
        song = str(song[0])
        webdata = str(data.loc["music_open", '网址'])
        dic_list = os.listdir(webdata)
        for sd in dic_list:
            if(song in sd):
                song = sd
                print(song)
                file_open = webdata + "/" + song
                webbrowser.open(file_open, new=0, autoraise=True)
                break
            else:
                if(sd == dic_list[len(dic_list)-1]):
                    print("查无此歌")
    elif ("来" in speak and "首" in speak and "歌" not in speak):
        song = re.compile("首(.*)").findall(speak)
        song = str(song[0])
        webdata = str(data.loc["music_open", '网址'])
        dic_list = os.listdir(webdata)
        for sd in dic_list:
            if(song in sd):
                song = sd
                file_open = webdata + "/" + song
                webbrowser.open(file_open, new=0, autoraise=True)
                break
            else:
                if(sd == dic_list[len(dic_list)-1]):
                    print("查无此歌")
    elif("你"in speak and "谁" in speak):
        print("我是AI助手,我叫Miyu")
        print("如果你不知道怎么使用我的话可以输入/help指令获取帮助哦")
    elif(speak == '/add'):
        word = input("输入您的词")
        if(word == ""):
            print("您未输入任何话")
            continue
        elif(word == "music_open"):
            print("您正在修改默认音乐播放文件夹哦此文件夹不支持使用//进行分割，否则可能会产生意外后果")
        pat = str(data2.index)
        print(pat)
        rst = re.compile("stop=(\d*),").findall(pat)
        print(rst)
        suoyin_num = rst[0]
        for i in range(0,int(suoyin_num)):
            i_1 = i + 1
            suo = str(data.index[i])
            """print(i)
            print(int(suoyin_num))"""
            if(suo == word):
                print("关键词有重复")
                print("对应着:\n",data.loc[word,'网址'])
                asd = input("是否更改?   Y/N")
                if(asd == "Y" or asd =="y"):
                    answer = input("要修改成的网址或文件地址,若填错了请写：啊写错了或不写。若需要打开多个请用//来隔开每个地址")
                    """data2.loc[str(int(suoyin_num)), '关键词'] = word
                    data2.loc[str(int(suoyin_num)), '网址'] = answer"""
                    if(answer == "啊写错了" or answer == ""):
                        print("好的，已退出")
                        continue
                    data2.loc[i, ['网址']] = [answer]
                    data2.to_excel('ddd.xlsx', sheet_name='Sheet1', index=False, header=True)
                    break
                else:
                    break
            else:
                if(i_1 == int(suoyin_num) and suo != word):
                    print("无重复")
                    print(word)
                    print(suo)
                    answer = input("要修改成的网址或文件地址,若填错了请写：啊写错了或不写。若需要打开多个请用//来隔开每个地址")
                    if (answer == "啊写错了" or answer == ""):
                        print("好的，已退出")
                        continue
                    dataframe = pd.DataFrame([[word, answer]], columns=["关键词", "网址"])
                    df_new = data2.append(dataframe, ignore_index=True)
                    df_new.to_excel(r"ddd.xlsx", sheet_name="Sheet1", index=False, engine="openpyxl")
                    break
    elif ("打开" in speak):
        speak = re.compile("打开(\w*)").findall(speak)
        speak = speak[0]#这行和上行是在对你说的话进行初步处理
        pat = str(data2.index)
        rst = re.compile("stop=(\d*),").findall(pat)
        suoyin_num = rst[0]
        for i in range(0, int(suoyin_num)):
            suo = str(data.index[i])
            if (suo == speak):
                webdata = str(data.loc[speak, '网址'])
                webdata = webdata.split("//")
                for num_w in range(0, len(webdata)):
                    print("正在打开:\n", webdata[num_w])
                    webbrowser.open(webdata[num_w], new=0, autoraise=True)
            else:
                if (i == suoyin_num):
                    print("未查询到此关键词")
    elif("open" in speak):
        speak = re.compile("open(\w*)").findall(speak)
        speak = speak[0]#这行和上行是在对你说的话进行初步处理
        pat = str(data2.index)
        rst = re.compile("stop=(\d*),").findall(pat)
        suoyin_num = rst[0]
        for i in range(0, int(suoyin_num)):
            i_1 = i + 1
            suo = str(data.index[i])
            if (suo == speak):
                webdata = str(data.loc[speak, '网址'])
                webdata = webdata.split("//")
                for num_w in range(0, len(webdata)):
                    print("正在打开:\n", webdata[num_w])
                    webbrowser.open(webdata[num_w], new=0, autoraise=True)
            else:
                if (i_1 == suoyin_num):
                    print("未查询到此关键词")
    elif(speak == "/help"):
        print("1:/add:\n添加关键词")
        print("2:打开+要打开的关键词:\n")
        print("例子:openB:会打开B站/打开B:会打开B站(注意打开(open)与B无空格)")
        print("3:试着对我说:来点歌吧会随机播放曲库中的一首歌哦.曲库文件夹默认为D:/music,关键词为music_open。若需要更改请在开始页面输入/add进行更改")
        print("4:和我说:找一些图片，我就会在百度给你找一些图片哦。比如：找一些图片，之后再输入要找的图片名字")
        print("4.1:和我说:找一些__的图片p，我就会在p站给你找一些图片。比如：给我找一些原神的图片p")
        print("4.2:和我说:找一些__的图片d，我就会在堆糖给你找一些图片。比如：给我找一些原神的图片d")
        print("4.2:和我说:找一些__的图片h，我就会在花瓣给你找一些图片。比如：给我找一些原神的图片h")
        print("5:和我说：今天有什么新闻？或今日热搜有啥，我会告诉你今日微博热搜词条")
        print("6:和我说：帮我翻译个东西，我会帮你翻译一段文本")
        print("7:和我说：今天天气怎么样，我会告诉你今明两天的天气")
    elif("新闻" in speak or "热搜" in speak or "news" in speak or "xinwen" in speak or "resou" in speak):
        news_num = input("查前几条?(最多50条，最低1条，默认20条)")
        if(news_num == "" or int(news_num) > 50 or int(news_num) < 1):
            news_num = 20
        print("正在查找今日热搜")
        cookie = str(data.loc["news_cookie", '网址'])
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',"cookie" : cookie}
        url = "https://s.weibo.com/top/summary"
        req = urllib.request.Request(url=url, headers=headers)
        news = urllib.request.urlopen(req, timeout=10)
        news = news.read().decode("utf-8","ignore")
        pat_news = 'target="_blank">(.*)</a>'
        pat_news2 = '<a href="(.*?)" target='
        data_news = re.compile(pat_news).findall(news)
        data_newsurl = re.compile(pat_news2).findall(news)
        len_news = 0
        for a in range(0,int(news_num)+1):
            print(str(a+1) + " : " + data_news[a])
            print("链接为 : " + "https://s.weibo.com/" + data_newsurl[a])
        print("一般第一条是上升速度快热度高的词条")
    elif('天气' in speak):
        wea = input('你想要哪里的天气?')
        if(wea == ""):
            print("没写默认南昌")
            wea = "南昌"
        with open("citycode.txt",'r',encoding='utf-8') as citycode:
            citycode = citycode.read()
            try:
                if (wea in citycode):
                    pat = wea + '"=>"(.*?)",'
                    wea_code = re.compile(pat).findall(citycode)
                    wea_code = wea_code[0]
                    url = 'http://t.weather.itboy.net/api/weather/city/' + wea_code
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        # 'cookie': cookie,
                    }
                    req = urllib.request.Request(url=url, headers=headers)
                    wea_data = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
                    pat_weatime = '"updateTime":"(.*)"},"data":{"'
                    updatetime = re.compile(pat_weatime).findall(wea_data)
                    updatetime = updatetime[0]
                    pat_tem = '","wendu":"(.*?)","ganmao":"'
                    tem = re.compile(pat_tem).findall(wea_data)
                    tem = tem[0]
                    # pat_wea = '","type":"(.*?)","notice'
                    # wea_type = re.compile(pat_wea).findall(wea_data)
                    # wea_type = wea_type[0]
                    pat_tolowtem = '"low":"低温 (.*?)","ymd":"'
                    tem_tolow = re.compile(pat_tolowtem).findall(wea_data)
                    tem_tolow = tem_tolow[0]
                    pat_tohigtem = '"high":"高温 (.*?)","low":"'
                    tem_tohig = re.compile(pat_tohigtem).findall(wea_data)[0]
                    pat_qua = '"quality":"(.*?)","wendu"'
                    qua_today = re.compile(pat_qua).findall(wea_data)[0]
                    pat_dir = 'fx":"(.*?)","fl"'
                    wea_dir = re.compile(pat_dir).findall(wea_data)
                    wea_dir = wea_dir[0]
                    pat_towea = '","type":"(.*?)","notice'
                    wea_totype = re.compile(pat_towea).findall(wea_data)
                    wea_totype = wea_totype[0]
                    pat_todir = '"fl":"(.*?)","type"'
                    wea_todir = re.compile(pat_todir).findall(wea_data)
                    wea_todir = wea_todir[1]
                    pat_lowtem = '"low":"低温 (.*?)","ymd":"'
                    tem_low = re.compile(pat_lowtem).findall(wea_data)
                    tem_low = tem_low[1]
                    pat_higtem = '"high":"高温 (.*?)","low":"'
                    tem_hig = re.compile(pat_higtem).findall(wea_data)[1]
                    notice_wea = re.compile('"notice":"(.*?)"},{"date"').findall(wea_data)[0]
                    print('天气数据来源于https://www.sojson.com/blog/305.html提供的api')
                    print(
                        "现在" + wea + "温度为：" + tem + "℃" + " , 最高" + tem_tohig + " , 最低" + tem_tolow + ", 风力大小为" + wea_dir + " , 空气质量为" + qua_today + " , 更新时间为" + updatetime)
                    print(
                        "明天" + wea + "温度为：最低:" + tem_low + " , 今日最高为" + tem_hig + " 天气为 : " + wea_totype + " , 风力大小为 " + wea_todir)
                    print("明天" + notice_wea)
                else:
                    print("没找到你说的城市哦，是不是写错了呢")
            except Exception as error:
                print(error)
    elif("杨启超" in speak or "yqc" in speak or "Jacky" in speak or "jacky" in speak):
        print("Miyu:嘻嘻 我的主人就是Jacky杨启超哦")
        #嘿嘿
    elif('翻译' in speak):
        q = input("原文为?(将自动检测语言)")
        orlg = "auto"
        tolg = input("转成什么语言?默认转为中文"+'''自动检测	auto	中文	zh	英语	en
粤语	yue	文言文	wyw	日语	jp
韩语	kor	法语	fra	西班牙语	spa
泰语	th	阿拉伯语	ara	俄语	ru
葡萄牙语	pt	德语	de	意大利语	it
希腊语	el	荷兰语	nl	波兰语	pl
保加利亚语	bul	爱沙尼亚语	est	丹麦语	dan
芬兰语	fin	捷克语	cs	罗马尼亚语	rom
斯洛文尼亚语	slo	瑞典语	swe	匈牙利语	hu
繁体中文	cht	越南语	vie''')
        if (tolg == ""):
            tolg = "zh"
        appid = str(data.loc["baidu_appid", '网址'])
        salt = str(random.randint(0000000000,9999999999))
        key = str(data.loc["baidu_key", '网址'])
        str1 = appid+q+salt+key
        str_md5 = hashlib.md5(str1.encode(encoding='UTF-8')).hexdigest()
        str2 = 'q='+q+'&from='+orlg+'&to='+tolg+'&appid='+appid+'&salt='+salt+'&sign='+str_md5
        url = 'https://fanyi-api.baidu.com/api/trans/vip/translate?' + str2
        data_trans = urllib.request.urlopen(url)
        data_trans = data_trans.read().decode('utf-8')
        pat_trans = '"dst":"(.*?)"}]'
        trans_fi = re.compile(pat_trans).findall(data_trans)[0]
        trans_fi = str(trans_fi.encode('utf-8').decode("unicode_escape"))
        print('翻译为' + trans_fi)
    else:
        print("你就不能加个打开在前面吗?")
        pat = str(data2.index)
        rst = re.compile("stop=(\d*),").findall(pat)
        suoyin_num = rst[0]
        for i in range(0, int(suoyin_num)):
            suo = str(data.index[i])
            if (suo == speak):
                webdata = str(data.loc[speak, '网址'])
                webdata = webdata.split("//")
                for num_w in range(0, len(webdata)):
                    print("正在打开:\n", webdata[num_w])
                    webbrowser.open(webdata[num_w], new=0, autoraise=True)
                print("算了,帮你开了")
            else:
                if (i == suoyin_num):
                    print("未查询到此关键词")








