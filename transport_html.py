#coding:utf-8
# import docx
# from docx2html import convert
# import HTMLParser
# def  docx2html(docx_name,new_name):
#     """
#     :docx转html
#     """
#     try:
#         #读取word内容
#         doc = docx.Document(docx_name,new_name)
#         data = doc.paragraphs[0].text
#         # 转换成html
#         html_parser = HTMLParser.HTMLParser()
#         #使用docx2html模块将docx文件转成html串，随后你想干嘛都行
#         html = convert(new_name)
#         #docx2html模块将中文进行了转义，需要将生成的字符串重新转义
#         return html_parser.enescape(html)
#     except:
#         pass
# if __name__ == '__main__':
#     docx2html('f:/test.docx','f:/test1.docx')
# !/usr/bin/env python
# coding=utf-8
from win32com import client as wc

word = wc.Dispatch('Word.Application')
doc = word.Documents.Open('e:/1.doc')
doc.SaveAs('e:/1.html', 8)
doc.SaveAs('e:/2.pdf', 17)
doc.SaveAs('e:/3.html', 10)
doc.Close()
word.Quit()

'''
win32com download 
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218
这里测试的环境是：windows xp,office 2007,python 2.5.2,pywin32 build 213，原理是利用win32com接口直接调用office API，好处是简单、兼容性好，只要office能处理的，python都可以处理，处理出来的结果和office word里面“另存为”一致。
原文地址：http://www.fuchaoqun.com/2009/03/use-python-convert-word-to-html-with-win32com/
view source
print
?
1.#!/usr/bin/env python 
2.#coding=utf-8 
3.from win32com import client as wc 
4.word = wc.Dispatch('Word.Application') 
5.doc = word.Documents.Open('d:/labs/math.doc') 
6.doc.SaveAs('d:/labs/math.html', 8 ) 
7.doc.Close() 
8.word.Quit()
关键的就是doc.SaveAs(’d:/labs/math.html’, 8)这一行，网上很多文章写成：doc.SaveAs(’d:/labs/math.html’, win32com.client.constants.wdFormatHTML)，直接报错：
AttributeError: class Constants has no attribute ‘wdFormatHTML’
当然你也可以用上面的代码将word文件转换成任意格式文件（只要office 2007支持，比如将word文件转换成PDF文件，把8改成17即可），下面是office 2007支持的全部文件格式对应表：
wdFormatDocument = 0
wdFormatDocument97 = 0
wdFormatDocumentDefault = 16
wdFormatDOSText = 4
wdFormatDOSTextLineBreaks = 5
wdFormatEncodedText = 7
wdFormatFilteredHTML = 10
wdFormatFlatXML = 19
wdFormatFlatXMLMacroEnabled = 20
wdFormatFlatXMLTemplate = 21
wdFormatFlatXMLTemplateMacroEnabled = 22
wdFormatHTML = 8
wdFormatPDF = 17
wdFormatRTF = 6
wdFormatTemplate = 1
wdFormatTemplate97 = 1
wdFormatText = 2
wdFormatTextLineBreaks = 3
wdFormatUnicodeText = 7
wdFormatWebArchive = 9
wdFormatXML = 11
wdFormatXMLDocument = 12
wdFormatXMLDocumentMacroEnabled = 13
wdFormatXMLTemplate = 14
wdFormatXMLTemplateMacroEnabled = 15
wdFormatXPS = 18
照着字面意思应该能对应到相应的文件格式，如果你是office 2003可能支持不了这么多格式。word文件转html有两种格式可选wdFormatHTML、wdFormatFilteredHTML（对应数字 8、10），区别是如果是wdFormatHTML格式的话，word文件里面的公式等ole对象将会存储成wmf格式，而选用 wdFormatFilteredHTML的话公式图片将存储为gif格式，而且目测可以看出用wdFormatFilteredHTML生成的HTML 明显比wdFormatHTML要干净许多。
当然你也可以用任意一种语言通过com来调用office API，比如PHP. 
'''
