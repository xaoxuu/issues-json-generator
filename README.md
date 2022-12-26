# Issues-Json Generator

自动提取本仓库 issues 中第一段 `JSON` 代码块并保存到仓库中，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。（你可以通过其它 N 种方式访问仓库文件）

例如动态友链：https://github.com/xaoxuu/friends

随意发挥你的创意吧～

> 本项目基于 [IJGP v1](#ijgp-协议) 协议

## 使用方法

1. fork 本仓库，把 `config.yml` 配置改为自己的：

```yaml
issues:
  repo: xaoxuu/friends # 仓库持有者/仓库名
  label: active  # 只能配置1个或留空，留空则所有open的issue都会被抓取。配置1个时，issue只有在具有该标签时才被抓取
  groups: # 填写用来分组的label名称。留空则所有被抓取的issue输出至data.json，否则按照输出与组名同名的json文件
  sort: updated-desc # 排序，按最近更新，取消此项则按创建时间排序
```
配置实例说明如下
| label         | groups                      | 输出文件                | 抓取issue                                         |
| ------------- | --------------------------- | ----------------------- | ------------------------------------------------- |
| label: active | groups:                     | data.json               | 所有open的、label包含active的issue                |
| label: active | groups: ["ordinary", "top"] | ordinary.json, top.json | open的、label包含active且包含ordinary或top的issue |
| label:        | groups:                     | data.json               | 所有open的issue                                   |
| label:        | groups: ["ordinary", "top"] | ordinary.json, top.json | open的、label包含ordinary或top的issue             |

2. 打开 action 运行权限。

## 测试是否配置成功

1. 新建 issue 并按照模板要求填写提交。
2. 等待 Action 运行完毕，检查 `output` 分支是否有 `/v2/data.json` 文件或`/v2/<组名>.json`，内容是否正确，如果正确则表示已经配置成功。


## IJGP 协议

**[IJGP](https://github.com/topics/ijgp)** 全称为 **Issues-Json Generator Protocol**，本协议目的在于减少重复造轮子和碎片化，改善大家跨项目使用体验。

在设计工具时，在满足如下场景的需求的地方需要使用与之对应的字段名：

### v1

| 字段 | 类型 | 用途 |
| :-- | :-- | :-- |
| title | string | 主标题 |
| url | string | 主链接 |
| avatar | string | 头像链接 |
| description | string | 描述，建议200字以内 |
| keywords | string | 关键词，英文逗号隔开 |
| screenshot | string | 屏幕截图 |

```json
{
  "content": [
    {
      "title": "",
      "url": "",
      "avatar": "",
      ...
    }
    ...
  ]
}
```

### v2（修订中，暂未发布）

> 相比 v1 版本，缩略图字段发生变动，且数据增加 `ijgp` 字段用来表示使用的协议版本。

| 字段 | 类型 | 用途 |
| :-- | :-- | :-- |
| title | string | 主标题 |
| url | string | 主链接 |
| avatar | string | 头像链接 |
| description | string | 描述，建议200字以内 |
| keywords | string | 关键词，英文逗号隔开 |
| thumbnail | string | 缩略图（旧版的“屏幕截图”含义不明） |


```json
{
  "ijgp": "v2",
  "data": [
    {
      "title": "",
      "url": "",
      "avatar": "",
      ...
    }
    ...
  ]
}
```

### 如何使用协议

> 协议会根据需要增加新的字段，但已有字段不会更改，如需更改，将会创建新的协议版本，这样使用同一个版本协议的所有前后端输出和得到的数据字段都是一致的。

例如网站需要显示只有头像和昵称的极简友链，那么模板可以配置为：

```json
{
  "title": "",
  "url": "",
  "avatar": ""
}
```

例如希望显示友链关键词、描述，那么模板可以配置为：

```json
{
  "title": "",
  "url": "",
  "avatar": "",
  "keywords": "",
  "description": ""
}
```

例如带有缩略图的网站收藏夹，那么模板可以配置为：

```json
{
  "title": "",
  "url": "",
  "avatar": "",
  "thumbnail": ""
}
```

前端（数据使用端）只需要根据实际需要，依据协议中的字段进行读取和显示。