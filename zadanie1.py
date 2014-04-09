import urllib
                          
sock = urllib.urlopen("http://www.fizyka.pw.edu.pl/index.php?option=com_facultyinfo&Itemid=233")  
htmlSource = sock.read()                             
sock.close()
plik = open('strona', 'w')
plik.write(htmlSource)
plik.close()