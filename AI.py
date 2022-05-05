import pandas as pd
import os
import re
import webbrowser
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
print("-" * 200 )
print("AI 1.0 版本")
while (True):
    data = pd.read_excel("ddd.xlsx")  # 索引为用关键词
    data2 = pd.read_excel("ddd.xlsx")  # 索引为用数字
    aaa = data.set_index('关键词', inplace=True)
    speak = input("Siri:您要做什么?或者使用命令/help获取帮助")
    if(speak == ""):
        sbtime = sbtime+1
        if (sbtime > 30):
            print("您是有什么大病吗?")
    elif(speak == '/add'):
        word = input("输入您的词")
        if(word == ""):
            print("您未输入任何话")
            continue
        pat = str(data2.index)
        print(pat)
        rst = re.compile("stop=(\d*),").findall(pat)
        print(rst)
        suoyin_num = rst[0]
        print(suoyin_num)
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
            print(int(suoyin_num))
            print(i)
            print(suo)
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








