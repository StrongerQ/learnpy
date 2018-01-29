#email: strongeren@163.com
#_autor: smallqiang

import configparser

config = configparser.ConfigParser()  #生成一个文件对象

# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('', 'w') as configfile:
#     config.write(configfile)

config.read('example.ini')  #关联配置文件
# print(config.sections()) #获取一般配置文件内容(除了默认)
# print(config.defaults()) #获取默认配置内容
# print(config['bitbucket.org']['User']) #获取指定值
# for key in config['bitbucket.org']: #循环会把default的值也去到
#     print(key)

config.remove_section('topsecret.server.com')
config.write(open('new_config.ini','w'))
