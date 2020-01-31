# buaa-ncov-hitcarder

BUAA肺炎状况自动打卡脚本

## 使用说明

1. `pip install selenium`

2. 编辑hitcard_general.py文件，填入你的统一认证账号密码和所在地经纬度。所在地经纬度可以通过[这里](https://jingweidu.51240.com/)查询。
3. `python hitcard_general.py`即可。
4. 本地生成调试用的图像文件，可以查看提交状况（待优化）。

## 待优化内容

1. Geolocation是否正确
2. 是否正确登录
3. 是否正确提交
