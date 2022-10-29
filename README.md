# issues-json-generator

自动提取本仓库 issues 中的 JSON 代码块

## 使用方法

fork 本仓库，把 `config.yml` 配置改为自己的：

```yaml
issues:
  repo: xaoxuu/friends # 仓库持有者/仓库名
  label: active # 筛选具有 active 标签的 issue ，取消此项则会提取所有 open 状态的 issue
  sort: updated-desc # 排序，按最近更新，取消此项则按创建时间排序
```