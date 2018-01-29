import logging

'''法一'''

# logging.basicConfig(                       #自定义日志
#                     level=logging.DEBUG,  #警报级别
#                     formater='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                         #日志格式,此处filename不同于下面filename,上面为执行模块  名字,下面为日志记录文件路径
#                     datefmt='%a,%d %b %Y %H:%M:%S', #上面的asctime格式化
#                     filename='test.log',#日志记录文件路径
#                     filemode='w' #文件打开方式,默认为a方式
#                     )
# logging.debug('111')
# logging.info('111')
# logging.warning('111')
# logging.error('111')
# logging.critical('111')

'''法二'''

# logger = logging.Logger("name",level=logging.INFO)#获取一个logger对象,并设置其名字与等级
logger = logging.getLogger()#获取一个logger对象
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()#创建一个Handler屏幕输出流对象
ch.setLevel(logging.INFO)#设置等级
fh = logging.FileHandler('test.log')#创建一个Handler文件输出流对象
fh.setLevel(logging.INFO) #设置等级
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")#输出格式 name是logger名字
ch.setFormatter(formater)#获取设置格式
fh.setFormatter(formater)#获取设置格式
logger.addHandler(ch) #logger获取屏幕输出对象
logger.addHandler(fh )#logger获取文件输出对象

logger.debug("sfsafas")
logger.info("sfsafas")
logger.warning("sfsafas")
logger.info("sfsafas")
logger.critical("sfsafas")