![](https://i0.hdslb.com/bfs/album/250f77dc6386e0cb9ffc93e9836f96c07c73e701.png)

# 网易云音乐自动签到 + 刷歌 310首

##  Github Actions 部署指南

- [网易云音乐自动签到 + 刷歌 310首](#网易云音乐自动签到--刷歌-310首)
  - [Github Actions 部署指南](#github-actions-部署指南)
  - [一、Fork 此仓库](#一fork-此仓库)
  - [二、设置账号、密码以及微信通知（可选）](#二设置账号密码以及微信通知可选)
    - [可选择设置Server酱通知](#可选择设置server酱通知)
  - [三、启用 Action](#三启用-action)
  - [四、查看运行结果](#四查看运行结果)
  - [注意事项](#注意事项)

## 一、Fork 此仓库

![image-20200727142541791](https://i.loli.net/2020/07/27/jK5H8FLvt7aBeYX.png)



## 二、设置账号、密码以及微信通知（可选）

![](https://i0.hdslb.com/bfs/album/eb3958ad1c3da6528091c63f602789cbe114b5dd.png)

添加以下变量

| 名称  |      | 值                                                                                                                         |
| ----- | ---- | -------------------------------------------------------------------------------------------------------------------------- |
| PHONE | 必填 | 用户名，多个用户名之间请用**#** 隔开，账号与密码的要对应 `示例`：**USER:13800000000#13800000001**                          |
| PWD   | 必填 | 密码，多个密码之间请用**#**隔开，账号与密码的要对应，密码中不能包含**#**，有的话请提前修改 `示例`：**PWD:cxkjntm#jntmcxk** |
| SCK   | 可选 | Server 酱的SCK                                                                                                             |

### 可选择设置Server酱通知

> 设置Server酱
> Server 酱的KEY获取地址
>
> http://sc.ftqq.com/3.version
> ![](https://i0.hdslb.com/bfs/album/74882a3398ba9fc8e6ebbf45c2e165188727d8f7.png)
>
> 添加密钥 SCK



## 三、启用 Action
1. ### 点击 ***Actions***，再点击 **I understand my workflows, go ahead and enable them**

   ![](https://i0.hdslb.com/bfs/album/da43935eda722fabe97f66011bd8ae27f147cc07.png)

2. ### 点击右侧的 ***Star***

   ![](https://i0.hdslb.com/bfs/album/f2d683b011284293fe2f56da22d205148392d764.png)

## 四、查看运行结果
> Actions --> 签到 --> build
>
> 能看到如下图所示，表示成功

![image-20200727143009081](https://i.loli.net/2020/07/27/kvV31BJKYDp9MRm.png)

## 注意事项

1. ### 每天运行两次，在上午 8 点和晚上 20 点。

2. ### 可以通过 ***Star*** 手动启动一次。

   ![image-20200727142617807](https://i.loli.net/2020/07/27/87oQeLJOlZvU3Ep.png)