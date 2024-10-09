# 1. Windows

## 1.1. 安装

### 1.1.1. PE

- [微PE工具箱](https://www.wepe.com.cn/download.html)

### 1.1.2. 系统

- [HelloWindows](https://hellowindows.cn/)
- [MSDN](https://next.itellyou.cn/Original/Index)（[备用网址](https://msdn.itellyou.cn/)）

### 1.1.3. 安装

- |No|Name|Value|
  |:-:|:-|:-|
  |1|跳过硬件限制|1. `SHIFT+F10` -> `regedit`<br />2. `HKEY_LOCAL_MACHINE\SYSTEM\Setup` -> 新建`项`：`LabConfig`<br />3. `LabConfig` -> 新建5个`DWORD（32位）值`：`BypassTPMCheck`=`1`、`BypassSecureBootCheck`=`1`、`BypassRAMCheck`=`1`、`BypassStorageCheck`=`1`、`BypassCPUCheck`=`1`|
  |2|跳过强制联网|`SHIFT+F10` -> `OOBE\BYPASSNRO.cmd`|
  |3|激活|[KMSPico](https://kms-full.com/)|

## 1.2. 配置

- |No|Name|Value|
  |:-:|:-|:-|
  |1|系统|私人：<br />1. `User`: `Hzm`<br />2. `Name`: `Hzm-Desktop`<br /><br />办公（台式）：<br />1. `User`: `YangTeng`<br />2. `Name`: `Lennon-Desktop`<br /><br />办公（笔记本）：<br />1. `User`: `YangTeng`<br />2. `Name`: `Lennon-Laptop`|
  |2|git|私人：<br />1. `git config --global user.name 'Hzm'`<br />2. `git config --global user.email '1210882202@qq.com'`<br /><br />办公（台式）：<br />1. `git config --global user.name 'Lennon_Desktop'`<br />2. `git config --global user.email 'mktg88@cht-group.net'`<br /><br />办公（笔记本）：<br />1. `git config --global user.name 'Lennon_Laptop'`<br />2. `git config --global user.email 'mktg88@cht-group.net'`|

## 1.3. 软件

- `MD5`校验：`certutil -hashfile `<ins>`file`</ins>` md5`

### 1.3.1. 系统

- |序号|名称|来源 / 校验|
  |:-:|:-|:-|
  |01|<span style="color: violet;">腾讯电脑管家</span>|[官网](https://guanjia.qq.com/page/product_download.html)|
  |02|<span style="color: violet;">7-Zip</span>|[官网](https://www.7-zip.org/)|
  |03|【<span style="color: violet;">迅雷</span>】|[官网](https://www.xunlei.com/)|
  |04|<span style="color: violet;">搜狗输入法</span>|[官网](https://pinyin.sogou.com/)|
  |05|【<span style="color: violet;">Clash</span>】|[Clash导航](https://clashxhub.com/)|
  |06|<span style="color: violet;">向日葵</span>|[官网](https://sunlogin.oray.com/download?categ=personal)|
  |07|【<span style="color: violet;">QtScrcpy</span>】|[GitHub](https://github.com/barry-ran/QtScrcpy)|
  |08|<span style="color: violet;">Snipate</span>|[官网](https://www.snipaste.com/)|
  |09|【<span style="color: violet;">Bandicam</span>】|[官网](https://www.bandicam.cn/downloads/)|
  |10|Office|[Office Tool Plus](https://www.coolhub.top/archives/11)|
  |11|【<span style="color: violet;">WPS</span>】|[官网](https://platform.wps.cn/)|
  |12|【<span style="color: violet;">OfficeBox</span>】|[官网](http://www.wofficebox.com/)|
  |13|打印机驱动|[官网](https://support.hp.com/in-en/drivers/printers)|

### 1.3.2. 应用

- |序号|名称|来源 / 校验|
  |:-:|:-|:-|
  |01|【<span style="color: violet;">Chrome</span>】|[官网](https://www.google.cn/chrome/)|
  |02|【<span style="color: violet;">Firefox</span>】|[官网](http://www.firefox.com.cn/)|
  |03|【<span style="color: violet;">QQ</span>】|[官网](https://im.qq.com/download)|
  |04|【<span style="color: violet;">QQ音乐</span>】|[官网](https://y.qq.com/download)|
  |05|【<span style="color: violet;">微信</span>】|[官网](https://pc.weixin.qq.com/)|
  |06|【<span style="color: violet;">钉钉</span>】|[官网](https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/)|
  |07|【<span style="color: teal;">Foxmail</span>】|[官网](https://www.foxmail.com/)|
  |08|坚果云|[官网](https://www.jianguoyun.com/s/downloads)|
  |09|【<span style="color: violet;">百度网盘</span>】|[官网](https://pan.baidu.com/download#pan)|
  |10|【阿里云盘】|[官网](https://www.aliyundrive.com/)|
  |11|【<span style="color: violet;">格式工厂</span>】|[官网](http://www.pcgeshi.com/download.html)|
  |12|【<span style="color: violet;">光影魔术手</span>】|[官网](http://www.neoimaging.cn/)|
  |13|【<span style="color: violet;">暴风影音</span>】|[官网](http://www.baofeng.com/download)|
  |14|Steam|[官网](https://store.steampowered.com/about/)|
  |15|Watt Toolkit|[官网](https://steampp.net/)|
  |16|Ubisoft|[官网](https://ubisoftconnect.com/zh-CN/)|

# 2. MacOS

## 2.1. 安装

- [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)

## 2.2. 配置

- |No|Name|Value|
  |:-:|:-|:-|
  |1|Homebrew|[官网](https://brew.sh/zh-cn/)|
  |2|Oh My Zsh|[官网](https://ohmyz.sh/#install)<br /><br />`~/.zshrc` -> `ZSH_THEME="apple"`、`ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=yellow'`、`plugins=(git zsh-autosuggestions)`（参考[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)）|
  |3|git|1. `git config --global user.name 'Hackintosh'`<br />2. `git config --global user.email '1210882202@qq.com'`|


## 2.3. 软件

- `MD5`校验：`md5 `<ins>`file`</ins>

### 2.3.1. 系统

- |序号|名称|来源 / 校验|
  |:-:|:-|:-|
  |01.|Hackintool|<https://github.com/headkaze/Hackintool/releases>|
  |02.|ProperTree|<https://github.com/corpnewt/ProperTree>|
  |03.|MonitorControl|<https://github.com/MonitorControl/MonitorControl/releases>|
  |04.|VideoProc Converter|<https://www.videoproc.com/video-editing-software/compare/products-comparison.htm>|
  |05.|Disk Speed Test|App Store|
  |06.|Geekbench|<https://www.geekbench.com/download/>|
  |07.|OpenCanopy Generator|<https://github.com/chris1111/OpenCanopy-Generator/releases>|
  |02.|柠檬清理|<https://lemon.qq.com/>|
  |03.|MacZip|<https://ezip.awehunt.com/>|
  |01.|Scroll Reverser|<https://pilotmoon.com/scrollreverser/>|
  |04.|NTFS|<https://uc.paragon-software.com/cabinet/#/>|
  |06.|迅雷|<https://www.xunlei.com/>|
  |05.|搜狗输入法|<https://pinyin.sogou.com/>|
  |05|<span style="color: violet;">Clash</span>|[Clash导航](https://clashxhub.com/)|
  |10.|向日葵|<https://sunlogin.oray.com/download?categ=personal>|
  |x|QtScrcpy|https://github.com/barry-ran/QtScrcpy|
  |08.|Snipate|<https://www.snipaste.com/>|
  |09.|ScreenFlow|<https://osx.cx/?s=screenflow>|
  |07.|WPS|<https://platform.wps.cn/>|
  |13.|iStat Menus|<https://beta.bjango.com/mac/istatmenus/>|
  |15.|Dynamic Wallpaper|App Store|
  |12.|Cheat Sheet|<https://www.mediaatelier.com/CheatSheet/>|

### 2.3.2. 应用

- |序号|名称|来源 / 校验|
  |:-:|:-|:-|
  |01.|Chrome|<https://www.google.cn/chrome/>|
  |02.|Firefox|<http://www.firefox.com.cn/>|
  |03.|Edge|<https://www.microsoft.com/zh-cn/edge>|
  |04.|QQ|<https://im.qq.com/macqq/>|
  |05.|QQ音乐|<https://y.qq.com/download/mac.html>|
  |06.|微信|<https://mac.weixin.qq.com/>|
  |07.|钉钉|<https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/>|
  |08.|坚果云|<https://www.jianguoyun.com/s/downloads>|
  |10.|百度网盘|<https://pan.baidu.com/download#pan>|
  |09.|阿里云盘|<https://www.aliyundrive.com/>|
  |11.|夸克网盘|<https://pan.quark.cn/>|
  |13.|Photoshop|<https://osx.cx/?s=photoshop>|
  |12.|IINA|<https://iina.io/>|
  |15.|TubeGet|<https://www.tubegetpro.com/zh/>|
  |14.|万兴优转|<https://uniconverter.wondershare.cn/>|
  |14|<span style="color: violet;">Steam</span>|<https://store.steampowered.com/about/>|
  |16|Ubisoft|<https://ubisoftconnect.com/zh-CN/>|
  |16.|Parallels|<https://www.parallels.com/products/desktop/download/>|
  |17.|VMware|<https://customerconnect.vmware.com/group/vmware/evalcenter?p=fusion-player-personal>|

# 3. Code
  
- |序号|名称|来源 / 校验|
  |:-:|:-|:-|
  |01|git|[官网](https://git-scm.com/downloads)|
  |02|【Sublime Text】|[官网](http://www.sublimetext.com/)|
  |03|【Visual Studio Code】|[Visual Studio Code](https://code.visualstudio.com/)|
  |03|Python|[官网](https://www.python.org/)|
  |05|【Postman】|[官网](https://www.postman.com/downloads/)|
  |12|Dev-C++|<https://github.com/Embarcadero/Dev-Cpp/>|
  |06|JDK|<https://www.runoob.com/java/java-environment-setup.html><br>(<https://www.oracle.com/java/technologies/downloads/>)|
  |07|MySQL|<https://www.cnblogs.com/winton-nfs/p/11524007.html>|
  |08|R|<https://cran.r-project.org/>|
  |09|R Studio|<https://www.rstudio.com/products/rstudio/download/>|
  |10|SPSS Modeler|百度网盘：<https://pan.baidu.com/s/1D8wlbnKo9n2Al86g7rlrDQ><br>提取码：efa3|
