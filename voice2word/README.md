# Voice2word
顾名思义，这就是一个把声音转换成文字的脚本
## 输入要求
+ 格式：MP3
+ 采样率：8000Hz 
+ 位率：16kb/s

PS：其实就是微信网页版上语音对话的格式，可用chrome+F12 Application-->Frames-->Media Copy link address 下载
## 语言
Python
+ 测试环境Python2.7/3.5
+ 推荐Python3+


## 调用示例

```
~$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from voice2word import voice2word
>>> voice2word("voice.mp3")
transform start
transform completed
connect to Baidu-API
{'sn': '408148476441516784855', 'err_msg': 'success.', 'corpus_no': '6514541352940318111', 'result': ['华南理工大学五山华南理工，位于广东省广州市创建于1934年，是中华人民共和国教育部直属的全国重点大学，首批国家双一流211工程985工程重点建设院校之一，路线仙人计划111计划五月工程师教育培养计划，我说打字人才教育培养计划和国家双创示范基地，是建筑老八校都说大学联盟中的工科大学联盟，中欧工程教育平台从应大学工程教育与研究联盟的主要成员，'], 'err_no': 0}
>>> 
```


