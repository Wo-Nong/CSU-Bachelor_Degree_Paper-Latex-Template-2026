# 初版作者说明
# 中南大学本科生毕业设计论文LaTex模板
> 本模板适合有一定LaTex基础的学习者使用
>
> 初学者可配合[首页](https://github.com/heyzbw/CSU_Thesis_Template)的LaTex常用语法学习使用
## 使用指南
- `main.tex`为主源文件，使用模板时编译此文件
- `cover.tex`编辑论文封面
- `abstract.tex`编辑论文标题与中英文的摘要
- `body.tex`编辑论文正文（包括结束语）
- `appendix.tex`编辑论文附录
- 文件夹`literature`存放文献数据库`thesis.bib`文件
- 文件夹`picture`存放论文中引用的图片
- 模板编译效果见<a href="main.pdf" target="_blank">main.pdf</a>

## 致谢
参考文献格式文件`gbt7714.sty`、`gbt7714-numerical.bst`和`gbt7714-author-year.bst`来源于GitHub项目：[GB/T 7714-2015 BibTeX Style](https://github.com/CTeX-org/gbt7714-bibtex-style)

Python引用格式文件`pythonhighlight.sty`来源于GitHub项目：[python-latex-highlighting](https://github.com/olivierverdier/python-latex-highlighting)





## 中南大学本科生毕业论文latex模板 2026再版 作者说明
> 作者系泥南26届毕业牲，11月份才想起来上传模板，应该不耽误27届学弟学妹。
> 首先感谢学长的模板，模板制作较为完备，结构清晰，进行修改也比较容易。（在此再吐槽一下CSU，竟然还没有官方模板）。
> 在前辈模板的基础上做了修改，以满足2026年新规以及对比部分差距，具体修改见下。

## 修改说明
- `statement.tex`：增加了声明以及使用授权书等26年新增标准
- `word_template`改为2026年新版
- 将`main.tex`以外的其他tex文件，转移至pages文件夹下，修改代码缩进，更加符合编程习惯（纯粹个人喜好）
- 文件夹pitures改为figures
- 将原版中某些细微差距进行修改与添加，如页边距、华文新魏字体、各级标题的缩进格式等等
- 保证了封面网格中文字的自动居中换行  
- 修改了appendix中的代码显示样式，并将代码引入方式由代码粘贴改为文件引入，单独定义了附录及其各模块在目录显示格式以及\ref引用格式
- 正文body.tex中增加了单图、双图、有说明单图；三线表、并列三线表以及公式的示例
- 图表引用格式由默认的英文`fig 1-2 `形式改为中文` 图 1-2`形式
- 重写了目录显示样式，以保证字体的对齐
- 增加了大量注释，仅作为学习参考。其中，跨页三线表等符合毕设要求

## 说明：
- 图表交叉引用时用 \cref，附录交叉引用用\ref

## 未实现但是无大碍的特征
- 页眉文字的透明度设置