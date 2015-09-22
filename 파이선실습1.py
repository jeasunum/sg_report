import urllib
file = urllib.urlopen('http://www.naver.com')
htmlcontents = file.read()
print htmlcontents

