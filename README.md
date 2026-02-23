# 《极度深寒》简体中文汉化

## 依赖资源

- [ColdFearLngBundler](https://github.com/meltnoexit/ColdFearLngBundler"ColdFearLngBundler")  ：使用此工具获取游戏原始英语资源文件的附加信息并在此基础上使用它生成简中资源文件
- [寒蝉点阵体](https://github.com/Warren2060/ChillBitmap"寒蝉点阵体") ：使用此字体用于生成简体中文位图字库

##  使用方法

替换`<游戏路径>\data\english`中的对应文件

## 贡献

翻译文本由[melt没路逃](https://github.com/meltnoexit) 整理制作
部分翻译文本由[梅毛臭气弹](https://www.xiaoheihe.cn/app/user/profile/25444364) 提供

## 许可证

本仓库包含多类文件，使用多种许可证：

|     文件类型     |                           文件路径                           |                许可证                 |           许可证路径           |                            备注                            |
| :--------------: | :----------------------------------------------------------: | :-----------------------------------: | :----------------------------: | :--------------------------------------------------------: |
|       代码       | `/README.md`<br/>`/generateCharsetFiles.py`<br/>`/.github/*` |                  MIT                  |       `/LICENSE-MIT.txt`       |                             无                             |
|    结构化文本    | `/fmv/text_sections.json`<br/>`/level/text_sections.json`<br/>`/menu/text_sections.json`<br/> |            CC BY-NC-SA 4.0            | `/LICENSE-CC BY-NC-SA 4.0.txt` |   CC BY-NC-SA 4.0仅针对翻译后文本，不包括未翻译原始文本    |
|       字体       |                   `/ChillBitmap_16px.ttf`                    | SIL OFL 1.1 + GPLv2 + GNU字体嵌入例外 |      `/LICENSE-Font.txt`       |    Github Actions运行过程中下载，字库图像使用此字体生成    |
|     字库图像     | `/fmv/font_raster0.png`<br/>`/level/font_raster0.png`<br/>`/menu/font_raster0.png`<br/> |            CC BY-NC-SA 4.0            | `/LICENSE-CC BY-NC-SA 4.0.txt` | Github Actions运行过程中间产物，最终产物中包含字库图像数据 |
| 原始文件拆解产物 | `/fmv/font_line_height0.txt`<br/>`/fmv/font_name0.txt`<br/>`/fmv/text_identifiers.csv`<br/>`/level/font_line_height0.txt`<br/>`/level/font_name0.txt`<br/>`/level/text_identifiers.csv`<br/>`/menu/font_line_height0.txt`<br/>`/menu/font_name0.txt`<br/>`/menu/text_identifiers.csv`<br/> |                  无                   |               无               |              文件数据内数据提取自游戏原始文件              |
