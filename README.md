# Issues-Json Generator

> [!IMPORTANT]
> 本项目已经归档不再维护，请使用功能更强大的 [动态友链及链接检查器](https://github.com/xaoxuu/links-checker) 使用方法更简单！还支持搭配 [友链文章订阅](https://github.com/xaoxuu/feed-posts-parser) 功能。
 

这是一个基于 GitHub 的自动化工具，自动提取本仓库 issues 中第一段 `JSON` 代码块并保存到仓库中，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。（你可以通过其它 N 种方式访问仓库文件）

应用场景：
- [收录友链，并定期检查链接是否可访问](https://xaoxuu.com/friends/)
- [收录主题用户，并定期检查网站是否仍在使用该主题](https://xaoxuu.com/wiki/stellar/examples.html)



## 快速开始

1. Fork 本仓库到你的 GitHub 账号下
2. 修改 `config.js` 文件中的配置信息
3. 在你的仓库中创建一个新的 Issue 来提交网站信息

## 功能特点

- 自动解析包含网站信息的 GitHub Issues
- 定期检查网站的可访问性和主题使用状态
- 自动更新 Issue 标签以反映网站状态

## 配置说明
### 生成器配置

```js
// config.js
export const config = {
  generator: {
    // 是否启用生成器
    enabled: true,
    // 目标仓库地址（格式：用户名/仓库名）
    repo: 'xaoxuu/hexo-theme-stellar-showcase',
    // Issue排序方式
    // updated/created: 更新时间/创建时间
    sort: 'created',
    // desc/asc: 降序/升序
    direction: 'desc',
    // 需要排除的Issue标签
    // 包含这些标签的Issue将不会被解析
    exclude_labels: ["审核中"]
  }
}
```

### 主题检查器配置

```js
// config.js
export const config = {
  theme_checker: {
    // 是否启用网站主题检查
    enabled: true,
    // 包含这些关键词的Issue将被检查
    include_keyword: '# 站点信息',
    // 包含这些标签的Issue将不会被检查
    exclude_labels: ["审核中"],
    // 主题标识meta标签选择器
    meta_tag: 'meta[name="hexo-theme"]',
    // 期望的主题名称
    theme_name: 'Stellar',
    // 主题版本号属性名
    version_attr: 'theme-version',
    // 主题名称属性名
    name_attr: 'theme-name',
    // 主题内容属性名
    content_attr: 'content',

  }
}
```

### 链接检查器配置

```js
// config.js
export const config = {
  link_checker: {
    // 是否启用链接检查
    enabled: true,
    // 包含这些关键词的Issue将被检查
    include_keyword: '# 友链信息',
    // 包含这些标签的Issue将不会被检查
    exclude_labels: ["审核中"],
    // 目标链接
    link: 'https://xaoxuu.com',
  }
}
```

## 工作流程

1. **Issue 解析**
   - 通过 GitHub Actions 定期运行
   - 解析带有指定标签的 Issues
   - 从 Issue 内容中提取网站信息
   - 生成 `v2/data.json` 数据文件

2. **网站检查**
   - 定期检查所有已收录网站
   - 验证网站是否使用 Stellar 主题
   - 检测主题版本信息
   - 更新 Issue 标签以反映检查结果

## 标签说明

- `审核中`: 网站正在审核中
- `x.x.x`: 网站正在使用的 Stellar 主题版本号
- `无效站点`: 网站未使用 Stellar 主题或已失效
- `无法访问`: 网站无法访问
- `未添加友链`: 网站未添加友链

## 许可证

[MIT License](LICENSE)
