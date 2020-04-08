# -*- coding: utf-8 -*-
#可以在这里获取SCKEY: http://sc.ftqq.com/
#请将文件中所有{SCKEY}换成你自己的

import cv2
import requests
import os

path = ("confirm.png")//你的confiirm.png文件
payload = {'text':'今天份的自动打卡成功~'}
payload2 = {'text':'打 卡 失 败 请 检 查'}
img = cv2.imread(path)

if os.path.exists(path):
    print("BGR:",img[1153,168])
    if(img[1153,168][0] == 83):
        r = requests.get("https://sc.ftqq.com/{SCKEY}.send",params=payload)
    else:
        r = requests.get("https://sc.ftqq.com/{SCKEY}.send",params=payload2)
    os.remove("C:\\Code\\ncov_hitcarder\\confirm.png")
else:
     r = requests.get("https://sc.ftqq.com/{SCKEY}.send",params=payload2)
