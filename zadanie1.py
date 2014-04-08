import urllib
from bs4 import BeautifulSoup
                                       
sock = urllib.urlopen("http://www.fizyka.pw.edu.pl/index.php?option=com_facultyinfo&Itemid=233")  
htmlSource = sock.read()                             
sock.close()

soup = BeautifulSoup(htmlSource)
nowe = soup.prettify()
nowe.encode('ascii')                                        
plik2 = open('plik2', 'w')
plik2.write(nowe)
plik2.close()