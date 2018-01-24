#!/usr/bin/python3
#coding:utf-8 

from aip import AipSpeech
from pydub import AudioSegment

def voice2word(filePath2mp3):
    print("transform start")
    # MP3 to WAV
    sound = AudioSegment.from_mp3(filePath2mp3)
        #转换后至temp.wav
    sound.export('temp.wav', format="wav")
    print("transform completed")
    # WAV to Word（下面3行的内容要从百度语音api官网获得）
    APP_ID = 'xxxxx'
    API_KEY = 'xxxxx'
    SECRET_KEY = 'xxxxx'
    print("connect to Baidu-API")
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    '''
    额外的设置，默认不设
    #建立连接的超时时间（单位：毫秒)
    client.setConnectionTimeoutInMillis = 1000
    #通过打开的连接传输数据的超时时间（单位：毫秒）
    client.setConnectionTimeoutInMillis = 1000
    '''
    # 读取文件
    def get_file_content(filePath):
        """以二进制的形式读取文件"""
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    result = client.asr(get_file_content('temp.wav'), 'wav', 8000, {
        'lan': 'zh',
    })

    return result

'''
会返回一个unicode格式编码的dict
{
u'err_no': 0, 
u'corpus_no': u'6514497432590049843', 
u'err_msg': u'success.', 
u'result': [u'\blahblahblah'], 
u'sn': u'378173005151516774630'
}
只提取文字部分就访问 result['result'][0]
'''
