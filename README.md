## xxxx系统的接口自动化； 
语言：python 3.9.7  
工具：requests 2.25.1 
测试框架：pytest 6.2.5 
报告工具：Allure 

## 项目其他包、文件说明
### common

configHTTP.py 基于requests框架对常用的get、post进行二次封装。
getData.py 封装一些获取数据的方法，比如读取config.ini中url、username、token；读取json和yaml类型文件等等。
logger.py logging库的一些配置，指定保存日志的文件路径，日志级别，以及调用文件；将日志存入到指定的文件中。

Token.py 每次运行run_fuse_case.py,会执行该py文件set_config方法把需要token写入config.ini中。 本demo删了。

### logs 

脚本执行后产生的日志均存在该文件下

### model

封装各模块的接口。

### report

xml报告和html报告生成的文件夹。

### testcases

测试pages封装好的接口，所有文件以test_开头，里面的测试类也要以test开头或包含test（为了pytest框架能够识别） 所有的断言、参数化在这里实现。

### testfiles

- config_file下config.ini存放测试需要用到的url、username和token数据。
- json_data 各接口请求数据存放在此处，已.json类型文件存储，使用getData.py中的read_json_file()方法读取该文件。
- schema_file 存放.schema文件，做接口返回值类型验证。
- upload_file 接口包含上传文件的情况时，上传的文件存在方在此文件夹。

## 根目录下的文件

- conftest.py pytest独有的文件，如果有的接口和其他接口有依赖关系，可以把方法封装再此处；用fixture机制实现。
- msg_push.py 钉钉推送的文件