like spider framework instructions

###############################################################################################
1.Configuration file description
config.py: This file gets the file of the current project configuration when the framework is executed, no need to understand and change
config_example.py: This file is your current project configuration file. You need to copy this file to your development directory and change it to the configuration required by the current project. The file name is best to use config_ plus the project name, for example: config_spider1.py

Mysql database configuration
DB_HOST: database host name
DB_USER: database account
DB_PASSWORD: database password
DB_PORT: database port
DB_NAME: database name
DB_CHARSET: database character set

Proxy settings
HEADERS: Proxy User-Agent, this parameter is a list type, you can configure multiple, randomly select one when accessing
PROXIES: Proxy ip, this parameter is a list type, you can configure multiple, randomly select one when accessing

LOG_DIR: Program execution log, if enabled, to ensure write access to this directory

EXCEL_DIR: excel file storage directory, if enabled, to ensure that this directory has write permission

Note: In the actual development process, when you need to import like_spider, you need to import config_spider1 first, the name here is the name of the configuration file you copied and modified, pay attention to your directory hierarchy when importing.


###############################################################################################
2.Http request description
request.py

First, instantiate the Request object

from like_spider import Request
req = Request()

(1).get: get request

Parameter:
url: access url, string type, this parameter must pass
data: the data to be transferred, the dictionary type, for example: {'test': 'test'}, no data can not pass this parameter

returns: get the page content, access failure will return an empty string

res = req.get('http://xxx.xxx.xxx')

(2).post: post request

Parameters and return content are the same as the get function

res = req.post('http://xxx.xxx.xxx', data = {'test':'test'})


###############################################################################################
3.Html extraction instructions
html.py

Instantiate Html objects

from like_spider import Html
html = Html()

(1).setHtml: set the html string to be processed currently

Parameter:
html: the html string to be processed currently, the string type, this parameter must pass

(2).setTag: set the content of the html tag you want to extract. You must call setHtml to set html before calling this function. This function can be called continuously according to the child relationship of the tag, and finally the label content of the last setting will be extracted. Finally, it must be Call the getData function to get the result

Parameter:
tagName: tag name, string type, for example: div, span..., this parameter must pass
setAttr: the tag attribute to be set, the dictionary type, for example: {'id': 'i1', 'class': 'c1'}, no need to specify the attribute can not pass this parameter
getAttr: the tag attribute to be extracted, the list type, for example: ['href', 'value'], no need to get the attribute, you can not pass this parameter
haveFoot: whether there is an end tag, the default is True, if you want to extract img, input such a tailless tag, this parameter needs to be set to False

(3).getData: get the extracted html tag content and the required tag attributes

Returns: the tag content and the tag attributes that need to be obtained, the list type, for example: [{'attr':{'a1':'v1', 'a2':'v2'}, 'content':'t1'}], Each element in the list is a dictionary. The attr element in the dictionary corresponds to the tag attribute you want to get, and the content element corresponds to the tag content

Example:

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

I want to get the src attribute of the img tag in the p tag of each class="p1". The code is as follows:

imgMatch = html\
	.setHtml(content)\
	.setTag('p', setAttr = {'class':'p1'})\
	.setTag('img', getAttr = ['src'], haveFoot = False)\
	.getData()
print(imgMatch)

Output result:

[
	{'attr': {'src': 'imgsrc1'}, 'content': "<img src = 'imgsrc1'>"}, 
	{'attr': {'src': 'imgsrc2'}, 'content': "<img src = 'imgsrc2'>"}
]

If you want to get the above label, you also need to get the href attribute and text content of the a tag in the p tag of each class="p1". The code is as follows:

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

Output result:

imgsrc1 href1 text1
imgsrc2 href2 text2


###############################################################################################
4.Mysql operation instructions
mysql.py

Instantiate a Mysql object

from like_spider import Mysql
mysql = Mysql()

(1).insert: insert data

Parameter:
sql: sql statement, string type
data: parameters to be replaced in the sql statement, tuple type

Returns: the new primary key id value generated after mysql insert

sql = "INSERT INTO test (f1, f2) VALUES (%s, %s)"
newId = mysql.insert(sql, (1, 2))

(2).update: update data

Same as above

sql = "UPDATE test set f2 = %s WHERE f1 = %s"
mysql.update(sql, (1, 2))

(3).delete: delete data
Parameters and calling methods are the same as above

(4).getRow: get a row of data
Parameters and calling methods are the same as above

(4).getCol: get a column of data
Parameters and calling methods are the same as above

(4).getOne: get a field value in a row of data
Parameters and calling methods are the same as above

(4).getAll: get multiple rows of data
Parameters and calling methods are the same as above


###############################################################################################
5.Excel file storage instructions
excel.py

Instantiate an Excel object

from like_spider import Excel
excel = Excel()

(1).saveFile: store data in excel file, and automatically generate month and date directory for easy management

Parameter:
data: the data to be saved, the list type
fileName: excel file name

data = [[1,2,3],[4,5,6]]
excel.saveFile(data, 'test.xlsx')


Note: In actual development, when instantiating each object, you can

from like_spider import *

Then instantiate the object as needed


###############################################################################################
6.General function description

(1).filterTag: Clear all html tags in the string
Parameter:
tagName: tag name
sourceStr: source string

(2).filterBlankChar: Clear all whitespace characters in the string
Parameter:
sourceStr: source string

(3).escapeString: Escape all special characters in the string
Parameter:
sourceStr: source string

(4).executeLog: Generate program execution log, automatically create month directory, log file named by date
Parameter:
content: information to log to the log file