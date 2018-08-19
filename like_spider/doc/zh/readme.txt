like spider框架使用说明文档

###############################################################################################
1.配置文件说明
config.py: 此文件为框架执行时获取当前项目配置的文件, 无需了解和改动
config_example.py: 此文件为你的当前项目配置文件, 你需要复制此文件到你的开发目录, 并修改成当前项目需要的配置, 文件名称最好用config_加上项目名称, 例如: config_spider1.py

mysql数据库配置
DB_HOST: 数据库主机名
DB_USER: 数据库帐号
DB_PASSWORD: 数据库密码
DB_PORT: 数据库端口
DB_NAME: 数据库名称
DB_CHARSET: 数据库字符集

TIME_OUT: 请求过期时间, 单位: 秒

代理设置
HEADERS: 代理User-Agent, 此参数为列表类型, 可以配置多个, 访问时会随机抽取一个
PROXIES: 代理ip, 此参数为列表类型, 可以配置多个, 访问时会随机抽取一个

PHANTOMJS: phantomjs的绝对路径, 如果你不需要获取js运行后网页内容, 可以忽略此项

WAIT_TIME: webdriver等待页面加载完成的时间, 单位: 秒

LOG_DIR: 程序执行日志, 如果开启, 要保证此目录有写入权限

EXCEL_DIR: excel文件存储目录, 如果开启, 要保证此目录有写入权限

注意: 在实际开发过程中, 在需要import like_spider的时候, 需要先import config_spider1, 此处的名称就是你复制修改后的配置文件名称, 导入时注意你的目录层级


###############################################################################################
2.http请求说明
request.py

首先, 实例化Request对象
from like_spider import Request
req = Request()

(1).get函数: get请求

参数:
url: 访问url, 字符串类型, 此参数必传
data: 传送的数据, 字典类型, 例如:{'test':'test'}, 无数据可不传此参数

返回: 得到到页面内容, 访问失败会返回空字符串

res = req.get('http://xxx.xxx.xxx')

(2).post函数: post请求

参数和返回内容同get函数

res = req.post('http://xxx.xxx.xxx', data = {'test':'test'})

(3).final函数: webdriver加载并且运行网页内javascript后返回最终网页内容

参数只有url, 同上

res = req.final('http://xxx.xxx.xxx')

###############################################################################################
3.html提取说明
html.py

实例化Html对象
from like_spider import Html
html = Html()

(1).setHtml函数: 设置当前要处理的html字符串

参数:
html: 当前要处理的html字符串, 字符串类型, 此参数必传

(2).setTag函数: 设置你要提取的html标签内容, 调用此函数前必须调用setHtml设置html, 此函数可根据标签的子级关系连续调用, 最终会提取最后一次设置的标签内容, 最后必须调用getData函数才可得到结果

参数:
tagName: 标签名称, 字符串类型, 例如: div, span..., 此参数必传
setAttr: 要设置的标签属性, 字典类型, 例如: {'id':'i1', 'class':'c1'}, 无需指定属性可不传此参数
getAttr: 要提取的标签属性, 列表类型, 例如: ['href', 'value'], 无需获取属性可不传此参数
haveFoot: 是否带有结束标签, 默认为True, 如要提取img, input这种无尾部的标签, 此参数需要设置成False

(3).getData函数: 获取提取到的html标签内容和需要得到的标签属性

返回: 标签内容和需要得到的标签属性, 列表类型, 例如: [{'attr':{'a1':'v1', 'a2':'v2'}, 'content':'t1'}], 列表中每个元素都是一个字典, 字典中attr元素对应你要获取的标签属性, content元素对应标签内容

示例:
content = '''
<div class = "c1">
	<img src = "test">
	<p class = "p1">
		<img src = 'imgsrc1'>
		<a href = "href1">text1</a>
	</p>
	<a href = "test1">test1</a>
	<p class = "p1">
		<img src = 'imgsrc2'>
		<a href = "href2">text2</a>
	</p>
	<a href = "test2">test2</a>
	<p class = "p2">
		<img src = 'imgsrc3'>
		<a href = "href3">text3</a>
	</p>
</div>'''
我要得到每个class="p1"的p标签里面img标签的src属性, 代码如下:
imgMatch = html\
	.setHtml(content)\
	.setTag('p', setAttr = {'class':'p1'})\
	.setTag('img', getAttr = ['src'], haveFoot = False)\
	.getData()
print(imgMatch)
输出结果:
[
	{'attr': {'src': 'imgsrc1'}, 'content': "<img src = 'imgsrc1'>"}, 
	{'attr': {'src': 'imgsrc2'}, 'content': "<img src = 'imgsrc2'>"}
]
如果想要得到上述标签的同时, 还要得到每个class="p1"的p标签里面a标签的href属性和文本内容, 代码如下:
pMatch = html\
	.setHtml(content)\
	.setTag('p', setAttr = {'class':'p1'})\
	.getData()
for p in pMatch:
	imgMatch = html\
		.setHtml(p['content'])\
		.setTag('img', getAttr = ['src'], haveFoot = False)\
		.getData()
	aMatch = html\
		.setHtml(p['content'])\
		.setTag('a', getAttr = ['href'])\
		.getData()
	print(imgMatch[0]['attr']['src'], aMatch[0]['attr']['href'], aMatch[0]['content'])
输出结果:
imgsrc1 href1 text1
imgsrc2 href2 text2


###############################################################################################
4.mysql操作说明
mysql.py

实例化Mysql对象
from like_spider import Mysql
mysql = Mysql()

(1).insert函数: 插入数据

参数:
sql: sql语句, 字符串类型
data: sql语句中需替换的参数, 元组类型

返回: mysql插入后产生的新增主键id值

sql = "INSERT INTO test (f1, f2) VALUES (%s, %s)"
newId = mysql.insert(sql, (1, 2))

(2).update函数: 更新数据

参数同上

sql = "UPDATE test set f2 = %s WHERE f1 = %s"
mysql.update(sql, (1, 2))

(3).delete函数: 删除数据
参数以及调用方法同上

(4).getRow函数: 获取一行数据
参数以及调用方法同上

(4).getCol函数: 获取一列数据
参数以及调用方法同上

(4).getOne函数: 获取一行数据中的某一个字段值
参数以及调用方法同上

(4).getAll函数: 获取多行数据
参数以及调用方法同上


###############################################################################################
5.excel文件存储说明
excel.py

实例化Excel对象
from like_spider import Excel
excel = Excel()

(1).saveFile函数: 将数据存储到excel文件中, 并且会自动生成月份以及日期目录, 方便管理

参数:
data: 要保存的数据, 列表类型
fileName: excel文件名称

data = [[1,2,3],[4,5,6]]
excel.saveFile(data, 'test.xlsx')


注意: 在实际开发中, 实例化各个对象的时候, 可以
from like_spider import *
然后根据需要实例化对象


###############################################################################################
6.通用函数说明

(1).filterTag函数: 把字符串中的某个html标签全部清除
参数:
tagName: 标签名称
sourceStr: 来源字符串

(2).filterBlankChar函数: 把字符串中的空白字符全部清除
参数:
sourceStr: 来源字符串

(3).escapeString函数: 把字符串中的特殊字符全部转义
参数:
sourceStr: 来源字符串

(4).executeLog函数: 生成程序执行日志, 自动创建月份目录, 日志文件按日期命名
参数:
content: 要记录到日志文件的信息
