# [Case 6. 国家医保服务平台](https://fuwu.nhsa.gov.cn/nationalHallSt/#/search/drug-directory)

## 6.1. 异步

- 浏览器发送请求时提供了异步机制，会在阻塞时继续执行后面的代码
- 但必须使用回调函数或者`Promise`的写法

## 6.2. `Promise`

- 不断地绑定回调函数 -> 回调地狱 -> 使用`Promise`解决（好看 -> 好维护）
- 最直观的理解：在函数内部调用绑定的回调函数，`Promise`只是一个封装
- 怎样找到函数：找`new Promise(函数)`
- 怎样绑定回调函数：`.then()`

## 6.3. `webpack`

- ```JavaScript
  lennon = '';

  !function() {
      function 加载器(t) { // t是要加载的模块
          if(n[t]) { // n存放所有已加载模块
              return n[t].exports;
          }

          lennon += `'${t}': ${e[t] + ''},\n`; // 筛选需要的模块

          return e[t].call(i.exports, i, i.exports, 加载器); // e存放所有模块
      }
  }(一个大数组或者大对象)
  ```

## 6.4. 搜索

- `interceptors.response.use`（拦截器） 关键字

## 6.5. 进制转换

- 数字转`16`进制：`(16).toString(16)`（`python`：`bytes.hex()`），需要注意前面要不要加一个0的问题（比如浏览器结果：`0a`，node结果：`a`）
- `16`进制转数字：`parseInt('f', 16)`（`python`：`bytes.fromhex()`）
