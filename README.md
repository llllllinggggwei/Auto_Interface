# Auto_Interface
只需要修改testcase里的excel文件，再运行文件即可跑测试用例

关于接口的增删改查已有demo
删除接口有些会用不同的形式

例:

DELETE https://api data:id=xx

DELETE https://api?id=xx

(还是说因为我们公司不规范才会有两种形式)


后期想法：

1.增加多excel文件多sheet形式的testcase

2.上下游关联，比如新增的接口id关联给修改和删除的接口（需要开发配合返回）

3.增加数据库查询，根据自己的查询返回与接口返回比较（增加数据可靠性）

4.添加一个bat文件在windows双击执行脚本

5.添加数据基准，已上一次准确的测试结果与这次的测试结果匹配判断


