# FlowCheck

ip 命令截取

## 安装

```bash
  $ sudo pip install flowCheck --upgrade
```

## 调用

```bash
  $ flower
  $ flower -h 
  $ flower -l
  $ flower -a
  $ flower eth0

```
## 说明

+ 基于linux系统中的ip命令
+ ip 命令作用和ifconfig相似,然而并不需要管理员权限
+ mac 系统未进行测试
+ 终端调用接口 flower
+ 没有做到实时监控(实现机制都不一样吧)



## 历史版本

+ 0.1 英文输出, 未封装, 裸方法, linux中ubuntu, CentOs 可以使用ip命令
+ 0.4 添加说明说明文件