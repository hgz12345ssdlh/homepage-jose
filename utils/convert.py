# -*- coding: utf-8 -*-

import os

full, abbr = 'Computer Architecture II', 'computer-architecture-2'

#
# PC.
#
f_raw, f_int = open(abbr+'.html', 'r'), open('int.html', 'w')
count1, count2, bookmarks = 0, 0, []

line = f_raw.readline()
while len(line) > 0:
  if line.strip().startswith('<head>'):
    f_int.write(line+'\n    <!-- Meta -->\n')
  elif line.strip().startswith('<title>'):
    f_int.write('    <title>Jose - '+full+'</title>\n    <link rel="stylesheet" type="text/css" href="../css/style.css" />\n    <link rel="stylesheet" type="text/css" href="../css/auto.css" />\n    <link rel="shortcut icon" href="../icon/favicon.ico" type="image/vnd.microsoft.icon" />\n    <link rel="icon" href="../icon/favicon.ico" type="image/vnd.microsoft.icon" />\n    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />\n    <meta http-equiv="Pragma" content="no-cache" />\n    <meta http-equiv="Expires" content="0" />\n\n')
  elif line.strip().startswith('<body>'):
    f_int.write(line+'    <script type="text/javascript">\n      if (/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {\n        window.location.href = "../m/course-notes/'+abbr+'.html";\n      }\n    </script>\n\n<!-- Decorations -->\n<div class="course-icon"><img src="../icon/'+abbr.lower()+'-show.png" alt="" onclick="location.href=\'#\'"></div>\n<div class="course-pdf" onclick="window.open(\'../files/notes-pdf/'+abbr+'.pdf\')" title="\n数学符号使用 MathJax 引擎，可能被部分浏览器拦截为不安全插件，请放心允许加载以更好地在线浏览，或下载 PDF 版本。\nDisplay of math symbols require the MathJax engine (which might be considered unsafe by several browsers). You can allow loading them for better online browsing experience, or download PDF version.\n">PDF</div>\n<div class="course-announcement" title="\n数学符号使用 MathJax 引擎，可能被部分浏览器拦截为不安全插件，请放心允许加载以更好地在线浏览，或下载 PDF 版本。\nDisplay of math symbols require the MathJax engine (which might be considered unsafe by several browsers). You can allow loading them for better online browsing experience, or download PDF version.\n">Jose 胡冠洲 @ ShanghaiTech</div>\n<div class="course-top" onclick="location.href=\'#\'">↑<br />Top</div>\n\n')
    f_int.write('<!-- Bookmark -->\n<div class="bookmark">\n  <div class="accordian">\n  </div>\n</div>\n<script type="text/javascript" src="../js/accordian.js"></script>\n\n')
    f_int.write('<!-- Main body -->\n<div class="note-body">\n\n')
  elif line.strip().startswith('<p>Author: '):
    f_int.write('<p>Author: Jose 胡冠洲 @ ShanghaiTech</p>\n')
  elif line.strip().startswith('<link rel="stylesheet" type="text/css" href="css/auto.css" /></p>'):
    pass
  elif line.strip().startswith('</body>'):
    f_int.write('\n</div>\n\n'+line)
  else:
    if line.strip().startswith('<h2>'):
      count1 += 1
      count2 = 0
      title1 = line[line.find('<h2>')+4:line.find('</h2>')]
      bookmarks.append([title1, []])
    elif line.strip().startswith('<h3>'):
      count2 += 1
      f_int.write('<a name="'+str(count1)+'.'+str(count2)+'"></a>')
      title2 = line[line.find('<h3>')+4:line.find('</h3>')]
      bookmarks[count1-1][1].append(title2)
    f_int.write(line)
  line = f_raw.readline()

f_raw.close()
f_int.close()

f_int, f_out = open('int.html', 'r'), open('out.html', 'w')

def purify(s):
  return s.replace('<em>', '<i>').replace('</em>', '</i>').replace('<code>', '<i>').replace('</code>', '</i>').replace('&amp;'  , '&')

line = f_int.readline()
while len(line) > 0:
  if line.strip().startswith('<div class="accordian">'):
    f_out.write(line+'\n')
    for i in range(len(bookmarks)):
      title1 = purify(bookmarks[i][0])
      f_out.write('    <button class="unfold">'+str(i+1)+'. '+title1+'</button>\n    <div class="toggle">\n      <ol>\n')
      for j in range(len(bookmarks[i][1])):
        title2 = purify(bookmarks[i][1][j])
        f_out.write('        <li onclick="location.href=\'#'+str(i+1)+'.'+str(j+1)+'\'">'+title2+'</li>\n')
      f_out.write('      </ol>\n    </div>\n\n')
  else:
    f_out.write(line)
  line = f_int.readline()

f_int.close()
f_out.close()

os.remove('int.html')
os.rename('out.html', '../notebook/'+abbr+'.html')

#
# Wap.
#
f_raw, f_int = open(abbr+'.html', 'r'), open('int.html', 'w')
count1, count2, bookmarks = 0, 0, []

line = f_raw.readline()
while len(line) > 0:
  if line.strip().startswith('<head>'):
    f_int.write(line+'\n    <!-- Meta -->\n')
  elif line.strip().startswith('<title>'):
    f_int.write('    <title>Jose - '+full+'</title>\n    <link rel="stylesheet" type="text/css" href="../../css/mobile.css" />\n    <link rel="stylesheet" type="text/css" href="../../css/auto.css" />\n    <link rel="shortcut icon" href="../../icon/favicon.ico" type="image/vnd.microsoft.icon" />\n    <link rel="icon" href="../../icon/favicon.ico" type="image/vnd.microsoft.icon" />\n    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />\n    <meta http-equiv="Pragma" content="no-cache" />\n    <meta http-equiv="Expires" content="0" />\n\n')
  elif line.strip().startswith('<body>'):
    f_int.write(line+'    <script type="text/javascript">\n      if (!/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {\n        window.location.href = "../../course-notes/'+abbr+'.html";\n      }\n    </script>\n\n<!-- Decorations -->\n<div class="course-topmenu">\n  <div class="course-icon"><img src="../../icon/'+abbr.lower()+'-show.png" alt="" onclick="location.href=\'#\'"></div>\n  <div class="course-announcement">Jose 胡冠洲<br />@ShanghaiTech</div>\n  <div class="course-pdf" onclick="window.open(\'../../files/notes-pdf/'+abbr+'.pdf\')">PDF</div>\n  <button class="course-attention"><img src="../../icon/attention.png"></button>\n</div>\n<div class="course-top" onclick="location.href=\'#\'">↑<br />Top</div>\n\n<!-- Attention words -->\n<div class="attention-toggle">\n  <div class="up-triangle"></div>\n  <div class="attention-words">\n    数学符号使用 MathJax 引擎，可能被部分浏览器拦截为不安全插件，请放心允许加载以更好地在线浏览，或下载 PDF 版本。<br />\n    Display of math symbols require the MathJax engine (which might be considered unsafe by several browsers). You can allow loading them for better online browsing experience, or download PDF version.\n  </div>\n</div>\n\n')
    f_int.write('<!-- Bookmark -->\n<button class="trigger">\n  <img src="../../icon/bookmark.png" alt="">\n</button>\n<div class="bookmark">\n  <div class="accordian">\n  </div>\n</div>\n\n')
    f_int.write('<!-- Main body -->\n<div class="note-body">\n\n')
  elif line.strip().startswith('<p>Author: '):
    f_int.write('<p>Author: Jose 胡冠洲 @ ShanghaiTech</p>\n')
  elif line.strip().startswith('<link rel="stylesheet" type="text/css" href="css/auto.css" /></p>'):
    pass
  elif line.strip().startswith('</body>'):
    f_int.write('\n</div>\n\n    <script type="text/javascript" src="../../js/accordian.js"></script>\n    <script type="text/javascript" src="../../js/bookmark.js"></script>\n    <script type="text/javascript" src="../../js/attention.js"></script>\n'+line)
  else:
    if line.strip().startswith('<h2>'):
      count1 += 1
      count2 = 0
      title1 = line[line.find('<h2>')+4:line.find('</h2>')]
      bookmarks.append([title1, []])
    elif line.strip().startswith('<h3>'):
      count2 += 1
      f_int.write('<a name="'+str(count1)+'.'+str(count2)+'"></a>')
      title2 = line[line.find('<h3>')+4:line.find('</h3>')]
      bookmarks[count1-1][1].append(title2)
    f_int.write(line)
  line = f_raw.readline()

f_raw.close()
f_int.close()

f_int, f_out = open('int.html', 'r'), open('out.html', 'w')

def purify(s):
  return s.replace('<em>', '<i>').replace('</em>', '</i>').replace('<code>', '<i>').replace('</code>', '</i>').replace('&amp;'  , '&')

line = f_int.readline()
while len(line) > 0:
  if line.strip().startswith('<div class="accordian">'):
    f_out.write(line+'\n')
    for i in range(len(bookmarks)):
      title1 = purify(bookmarks[i][0])
      f_out.write('    <button class="unfold">'+str(i+1)+'. '+title1+'</button>\n    <div class="toggle">\n      <ol>\n')
      for j in range(len(bookmarks[i][1])):
        title2 = purify(bookmarks[i][1][j])
        f_out.write('        <li onclick="location.href=\'#'+str(i+1)+'.'+str(j+1)+'\'">'+title2+'</li>\n')
      f_out.write('      </ol>\n    </div>\n\n')
  else:
    f_out.write(line)
  line = f_int.readline()

f_int.close()
f_out.close()

os.remove('int.html')
os.rename('out.html', '../m/notebook/'+abbr+'.html')
