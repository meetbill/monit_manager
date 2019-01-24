# monit 管理工具

<!-- vim-markdown-toc GFM -->

* [使用手册](#使用手册)
* [版本](#版本)
* [相关内容](#相关内容)
* [参加步骤](#参加步骤)

<!-- vim-markdown-toc -->

## 使用手册

[monit_manager 使用手册](https://github.com/meetbill/monit_manager/wiki)

## 版本

* v1.0.3，2019-01-25 [Update]: 封装为 monit 包
* v1.0.2，2017-08-24 update: (1) 程序访问 monit web 方式从 requests 换为 urllib2,(2) 更新 xmltodict 库，(3) 增加命令行操作模式
* v1.0.1，2017-05-16 init: 可以获取 monit 状态信息并转换为 json

## 相关内容

> * [monit 使用](https://billwang139967.gitbooks.io/op_practice_book/content/doc/monitor/monit.html)
> * [xml 转换为 dict 库](https://github.com/meetbill/MyPythonLib/tree/master/My_lib/xmltodict)

## 参加步骤

* 在 GitHub 上 `fork` 到自己的仓库，然后 `clone` 到本地，并设置用户信息。
```
$ git clone https://github.com/meetbill/monit_manager.git
$ cd monit_manager
$ git config user.name "yourname"
$ git config user.email "your email"
```
* 修改代码后提交，并推送到自己的仓库。
```
$ #do some change on the content
$ git commit -am "Fix issue #1: change helo to hello"
$ git push
```
* 在 GitHub 网站上提交 pull request。
* 定期使用项目仓库内容更新自己仓库内容。
```
$ git remote add upstream https://github.com/meetbill/monit_manager.git
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master
$ git push -f origin master
```
