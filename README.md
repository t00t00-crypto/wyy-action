# 网易云音乐自动签到 + 刷歌
> 网易云音乐自动登录签到 + 刷歌 310 首

## Github Actions 部署指南

### 一、Fork 此仓库
![image-20200727142541791](https://i.loli.net/2020/07/27/jK5H8FLvt7aBeYX.png)



### 二、设置账号密码
添加名为 **USER**、**PWD** 的变量，值分别为 **账号（仅支持手机号）**、**密码 **

> Settings-->Secrets-->New secret

支持多账号，账号之间与密码之间用 ***#*** 分隔，账号与密码的个数要对应

(可选)设置[Server酱](http://sc.ftqq.com/)推送密钥,添加到 **SCKEY** 的变量,可以将运行结果推送到微信上

示例：**USER:13800000000#13800000001**，**PWD:cxkjntm#jntmcxk**
![image-20200727142753175](https://i.loli.net/2020/07/27/xjri3p4qdchaf2G.png)

### 三、启用 Action
1. 点击 ***Actions***，再点击 **I understand my workflows, go ahead and enable them**

   ![](https://i.loli.net/2020/07/27/pyQmdMHrOIz4x2f.png)

2. 点击左侧的 ***Star***

   ![image-20200727142617807](https://i.loli.net/2020/07/27/3cXnHYIbOxfQDZh.png)

### 四、查看运行结果
> Actions --> 签到 --> build
>
> 能看到如下图所示，表示成功

![image-20200727143009081](https://i.loli.net/2020/07/27/kvV31BJKYDp9MRm.png)

## 注意事项

1. 每天运行两次，在上午 6 点和晚上 22 点。

2. 可以通过 ***Star*** 手动启动一次。

   ![image-20200727142617807](https://i.loli.net/2020/07/27/87oQeLJOlZvU3Ep.png)
