# TOC:

- [01. Windows](#01-windows)
- [02. MacOS](#02-macos)
- [03. Code](#03-code)

- - -

# 01. Windows

## 1. 系统

### 1.1. PE

- [微PE工具箱](https://www.wepe.com.cn/download.html)

### 1.2. 镜像

- [MSDN](https://next.itellyou.cn/Original/Index)（[备用网址](https://msdn.itellyou.cn/)）
- [HelloWindows](https://hellowindows.cn/)

### 1.3. 关键操作

- |No|Name|Value|
  |:-:|:-|:-|
  |1|跳过硬件限制|1. `SHIFT+F10` -> `regedit`<br />2. `HKEY_LOCAL_MACHINE\SYSTEM\Setup` -> 新建`项`：`LabConfig`<br />3. `LabConfig` -> 新建5个`DWORD（32位）值`：`BypassTPMCheck`=`1`、`BypassSecureBootCheck`=`1`、`BypassRAMCheck`=`1`、`BypassStorageCheck`=`1`、`BypassCPUCheck`=`1`|
  |2|跳过强制联网|`SHIFT+F10` -> `OOBE\BYPASSNRO.cmd`|
  |3|激活|[KMSCX](https://kms.cx/)、[KMSPico](https://kms-full.com/)|

## 2. 软件

### 2.1. 系统

- |No|Name|Reference|Work|
  |:-:|:-|:-|:-:|
  |01|7-Zip|[官网](https://www.7-zip.org/)|√|
  |02|DiskGenius|[官网](https://www.diskgenius.cn/download.php)|×|
  |03|搜狗输入法|[官网](https://shurufa.sogou.com/windows)|√|
  |04|迅雷|[官网](https://www.xunlei.com/)|×|
  |05|Snipate|[官网](https://www.snipaste.com/)|√|
  |06|Bandicam|[官网](https://www.bandicam.cn/downloads/)|×|
  |07|腾讯电脑管家|[官网](https://guanjia.qq.com/page/product_download.html)|×|
  |08|向日葵|[官网](https://sunlogin.oray.com/en/download?categ=personal)|√|
  |09|Microsoft Office|[Office Tool Plus](https://www.coolhub.top/archives/11)|×|
  |10|WPS|[官网](https://platform.wps.cn/)|√|
  |11|OfficeBox|[官网](https://www.wofficebox.com/)|√|
  |12|Clash Verge|[GitHub](https://github.com/clash-verge-rev/clash-verge-rev/tree/v2.3.2)|√|
  |13|TrafficMonitor|[GitHub](https://github.com/zhongyang219/TrafficMonitor)|√|
  |14|PowerShell|[GitHub](https://github.com/powershell/powershell)|√|
  |15|打印机驱动|[官网](https://support.hp.com/in-en/drivers/printers)|×|

### 2.2. 程序

- |No|Name|Reference|Work|
  |:-:|:-|:-|:-:|
  |01|Chrome|[官网](https://www.google.cn/chrome/)|√|
  |02|QQ|[官网](https://im.qq.com/download)|√|
  |03|QQ音乐|[官网](https://y.qq.com/download)|√|
  |04|微信|[官网](https://pc.weixin.qq.com/)|√|
  |05|钉钉|[官网](https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/)|√|
  |06|Foxmail|[官网](https://www.foxmail.com/)|√|
  |07|百度网盘|[官网](https://pan.baidu.com/download#pan)|×|
  |08|格式工厂|[官网](http://www.pcgeshi.com/download.html)|×|
  |09|光影魔术手|[官网](http://www.neoimaging.cn/)|×|
  |10|暴风影音|[官网](http://www.baofeng.com/download)|×|
  |11|Steam|[官网](https://store.steampowered.com/about/)|×|
  |12|Watt Toolkit|[官网](https://steampp.net/)|×|
  |13|Ubisoft|[官网](https://ubisoftconnect.com/zh-CN/)|×|

# 02. MacOS

## 1. 软件

### 1.1. 系统

- |No|Name|Reference|
  |:-:|:-|:-|
  |01|MacZip|[官网](https://ezip.awehunt.com/)|
  |02|搜狗输入法|[官网](https://pinyin.sogou.com/)|
  |03|迅雷|[官网](https://www.xunlei.com/)|
  |04|Snipate|[官网](https://www.snipaste.com/)|
  |05|ScreenFlow|[黑苹果社区](https://osx.cx/?s=screenflow)|
  |06|柠檬清理|[官网](https://lemon.qq.com/)|
  |07|向日葵|[官网](https://sunlogin.oray.com/download?categ=personal)|
  |08|WPS|[官网](https://platform.wps.cn/)|
  |09|Clash Verge|[GitHub](https://github.com/clash-verge-rev/clash-verge-rev/tree/v2.3.2)|
  |10|Scroll Reverser|[官网](https://pilotmoon.com/scrollreverser/)|
  |11|NTFS|[官网](https://uc.paragon-software.com/cabinet/#/)|
  |12|Homebrew|[官网](https://brew.sh/zh-cn/)|
  |13|Oh My Zsh|[官网](https://ohmyz.sh/#install)<br /><br />`~/.zshrc` -> `ZSH_THEME="apple"`、`ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=yellow'`、`plugins=(git zsh-autosuggestions)`（参考[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)）|
  |14|MonitorControl|[GitHub](https://github.com/MonitorControl/MonitorControl/releases)|
  |15|iStat Menus|[官网](https://bjango.com/mac/istatmenus/)|
  |16|Parallels|[官网](https://kb.parallels.com/5802)|
  |17|VMware Fusion|[官网](https://customerconnect.vmware.com/group/vmware/evalcenter?p=fusion-player-personal)|

### 1.2. 程序

- |No|Name|Reference|
  |:-:|:-|:-|
  |01|Chrome|[官网](https://www.google.cn/chrome/)|
  |02|Edge|[官网](https://www.microsoft.com/zh-cn/edge)|
  |03|QQ|[官网](https://im.qq.com/macqq/)|
  |04|QQ音乐|[官网](https://y.qq.com/download/mac.html)|
  |05|微信|[官网](https://mac.weixin.qq.com/)|
  |06|钉钉|[官网](https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/)|
  |07|百度网盘|[官网](https://pan.baidu.com/download#pan)|
  |08|Photoshop|[黑苹果社区](https://osx.cx/?s=photoshop)|
  |09|IINA|[官网](https://iina.io/)|
  |10|TubeGet|[官网](https://www.tubegetpro.com/zh/)|
  |11|万兴优转|[官网](https://uniconverter.wondershare.cn/)|

# 03. Code
  
- |No|Name|Reference|Work|
  |:-:|:-|:-|:-:|
  |01|Git|[官网](https://git-scm.com/downloads)|√|
  |02|Sublime Text|[官网](http://www.sublimetext.com/)|×|
  |03|Visual Studio Code|[官网](https://code.visualstudio.com/)|√|
  |04|Python|[官网](https://www.python.org/)|√|
  |05|PyCharm|[官网](https://www.jetbrains.com/pycharm/download/)|√|
  |06|Postman|[官网](https://www.postman.com/downloads/)|√|
  |07|Dev-C++|[GitHub](https://github.com/Embarcadero/Dev-Cpp/releases)|√|
  |08|JDK|[参考教程](https://www.runoob.com/java/java-environment-setup.html)|√|
  |09|MySQL|[参考教程](https://www.cnblogs.com/winton-nfs/p/11524007.html)|×|
  |10|R|[官网](https://cran.r-project.org/)|√|
  |11|R Studio|[官网](https://www.rstudio.com/products/rstudio/download/)|√|
  |12|SPSS Modeler|[通过网盘分享的文件：IBM SPSS Modeler 18 (提取码: efa3)](https://pan.baidu.com/s/1D8wlbnKo9n2Al86g7rlrDQ)|×|
