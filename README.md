# Perfectworld-VirtualBox-Conflict-Resolution-Tools
用于解决安装完美世界对战平台后不能使用VirtualBox虚拟机或其他虚拟化平台的问题。
## 使用方法
使用 `win键+R` 输入 `cmd` 打开命令行，执行下面的命令：
```shell
git clone https://github.com/Smera1d0/Perfectworld-VirtualBox-Conflict-Resolution-Tools.git
cd .\Perfectworld-VirtualBox-Conflict-Resolution-Tools\
.\完美世界对战平台VirtualBox适配工具.exe
```
然后选择完美世界竞技平台的 plugin 目录，通常在 `\perfectworldarena\plugin` 这个位置。
### 使用 VirtualBox 时
选择 `修改`， **此操作需要重启电脑**，重启后即可正常使用 VirtualBox。
### 使用 完美世界对战平台 时
选择 `还原`， **此操作需要重启电脑**，重启后即可正常使用 完美世界对战平台。

## 原理
通过修改完美世界对战平台 plugin 目录下的 `MessageTransfer.sys` 和 `MessageTransfer_x86.sys` 这两个文件的后缀名来实现，修改时，该脚本会在这两个文件后面添加 `.txt` 后缀名。
