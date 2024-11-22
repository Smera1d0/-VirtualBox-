# Perfectworld-VirtualBox-Conflict-Resolution-Tools
用于解决安装完美世界对战平台后不能使用VirtualBox虚拟机或其他虚拟化平台的问题。
## 界面预览

![783918fa47c6c1e3c85e1cffcee4322f](https://github.com/user-attachments/assets/bdc0d0d7-93f3-4729-9934-f1014fb7e15d)


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
通过修改完美世界对战平台 plugin 目录下的 `MessageTransfer.sys` 和 `MessageTransfer_x86.sys` 这两个文件的后缀名来实现，修改时，该脚本会在这两个文件后面添加 `.txt` 后缀名；还原时，删除 `.txt` 后缀名。

## 免责声明
若使用该工具导致完美世界对战平台无法启动或造成账号 VAC，作者概不负责，理论上还原之后再使用完美世界对战平台不会出现任何问题。

## 测试
修改后，VirtualBox 虚拟机正常启动。

![a8845d72993ddcda4a2018bb16de1a05](https://github.com/user-attachments/assets/3a13f788-bbd7-4cd8-b6f1-84bfac0582b5)


还原后，反作弊正常启动。

![image](https://github.com/user-attachments/assets/d817bcab-3f1d-46eb-bf1f-34489a3b91fe)
