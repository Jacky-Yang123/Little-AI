import pandas as pd
import os
import re
import webbrowser
import random
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
print("AI Miyu 1.1 版本")
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
        song = re.compile("放首(.*)").findall(speak)
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
        song = re.compile("来首(.*)").findall(speak)
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
    elif("杨启超" in speak or "yqc" in speak or "Jacky" in speak or "jacky" in speak):
        print("Miyu:我的主人就是Jacky杨启超哦")
        #嘿嘿
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








