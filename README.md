# buaa-ncov-hitcarder

BUAA肺炎状况自动打卡脚本

## 使用说明

*请确保你的Chrome版本号为79.x，否则需要更换chromedriver文件*
1. `pip install selenium`，并把 `chromedriver.exe` 所在位置添加进PATH。
2. 编辑 auto_hitcarder.py 文件，填入你的统一认证账号密码和所在地经纬度。所在地经纬度可以通过[这里](https://jingweidu.51240.com/)查询。
3. `python auto_hitcarder.py`即可。
4. 本地生成调试用的5个720P图像文件，可以查看提交状况（待优化）。

## 待优化内容

1. Geolocation是否正确
2. 是否正确登录
3. 是否正确提交
4. 自动按时执行√

## 已知Bug

1. 自动打卡完毕后不会刷新控制台信息，待修正。
