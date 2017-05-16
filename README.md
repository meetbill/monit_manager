# monit_manager
monit 管理工具

[monit 使用手册](https://billwang139967.gitbooks.io/op_practice_book/content/doc/monitor/monit.html)

原理性内容会往 wiki 上整理
[wiki](https://github.com/BillWang139967/monit_manager/wiki)

## version

* v0.1，2017-05-16 init: 可以获取 monit 状态信息并转换为 json

## 参加步骤

* 在 GitHub 上 `fork` 到自己的仓库，然后 `clone` 到本地，并设置用户信息。
```
$ git clone https://github.com/BillWang139967/monit_manager.git
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
$ git remote add upstream https://github.com/BillWang139967/monit_manager.git
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master
$ git push -f origin master
```
