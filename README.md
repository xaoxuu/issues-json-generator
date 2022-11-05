# issues-json-generator

自动提取本仓库 issues 中第一段 `JSON` 代码块并保存到仓库中，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。（你可以通过其它 N 种方式访问仓库文件）

例如动态友链：https://github.com/xaoxuu/friends

随意发挥你的创意吧～



## 使用方法

1. fork 本仓库，把 `config.yml` 配置改为自己的：

```yaml
issues:
  repo: xaoxuu/friends # 仓库持有者/仓库名
  label: active # 筛选具有 active 标签的 issue ，取消此项则会提取所有 open 状态的 issue
  sort: updated-desc # 排序，按最近更新，取消此项则按创建时间排序
```

2. 打开 action 运行权限。

## 测试是否配置成功

1. 新建 issue 并按照模板要求填写提交。
2. 等待 Action 运行完毕，检查 `output` 分支是否有 `/v2/data.json` 文件，内容是否正确，如果正确则表示已经配置成功。

