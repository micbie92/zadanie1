import urllib
from bs4 import BeautifulSoup
                                       
sock = urllib.urlopen("http://www.fizyka.pw.edu.pl/index.php?option=com_facultyinfo&Itemid=233")  
htmlSource = sock.read()                             
sock.close()

soup = BeautifulSoup(htmlSource)
nowe = soup.get_text()
nowe.encode('ascii')
print nowe
plik = open('text', 'w')
plik.write(nowe)
plik.close()