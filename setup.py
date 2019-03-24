import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'like_spider',
    version = '1.1.8',
    author = 'Yingjie Wu',
    author_email = 'wyjhaha@foxmail.com',
    description = 'a crawler framework that allows developers to easily extract web page information and quickly store data',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/wuyingjie1002/like_spider',
    packages = setuptools.find_packages(),
    classifiers = (),
    install_requires = [
        'requests',
        'pymysql',
        'openpyxl',
        'selenium'
    ]
)
