# 4. 浏览器调试工具

## 4.1. 打开方式

1. `F12`
2. 鼠标右键 -> 检查
3. 浏览器右上角三个点 -> 更多工具 -> 开发者工具（推荐）

### 4.1.1. 禁用`F12`按键

- ```JavaScript
  addEventListener('keydown', function(e) {
    if(e.key === 'F12') {
        e.preventDefault();
        return false;
    }
  });
  ```

### 4.1.2. 禁用右键菜单

- ```JavaScript
  addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
  });
  ```

### 4.1.3. 停靠至单独的窗口

- 注意`innerWidth`和`innerHeight`

## 4.2. 网络（Network）

- 保留日志（Preserve log）：当页面重新加载时，是否清除网络日志（抓包抓到的数据包）
- 停用缓存（Disable cache）：已经请求加载过的文件是否使用本地的缓存数据，而不重新向服务端请求
- 过滤（Filter）：筛选`url`中包含指定字符的请求
- 左上角红色按钮：停止抓包
- 左上角白色按钮：清除网络日志
- `ctrl` + `f`：在所有请求中进行搜索（无法搜索到请求体中的数据）
- 请求分类：
  - `Fetch/XHR`：由网站`js`代码发送的请求
  - 文档：页面加载的第一个`HTML`

## 4.3. 控制台（Console）

- 用户消息：由`js`代码触发的打印信息
- 错误：console.error
- 警告：console.warn
- 信息：console.log
- 详细信息：console.debug
- 呼出悬停控制台界面：
  - `ctrl` + `shift` + `f`
  - 右上角三个点 -> 搜索

## 4.4. 源代码（Sources）

- 在这个页面调试`js`代码
- 代码段（Snippets）：编写并运行多段`js`代码

## 4.5. 应用程序（Application）















