 # Tp1**********yeduo********

#import requests
#r=requests.get("https://jsonplaceholder.typicode.com/todos")
#users=r.json()

#with open ("users.txt", "w") as f:
#    for user in users:
#        f.write(str(users)+"\n")

#import requests
#r=requests.get("https://jsonplaceholder.typicode.com/todos")
#users=r.json()
#for user in users:
#  if(user["completed"]):
#    print(user["title"])
#    with open ("users_filtre.txt", "w") as f:
#      f.write(str(user["title"])+"\n")

#*********************

#data=input("Entrer une phrase:")
#with open("data.txt", "a") as f:
#  f.write(data +"\n")

#import requests
#r=requests.get("https://jsonplaceholder.typicode.com/todos")
#users=r.json()
#for user in users:
#  if(user["completed"]):
#    print(user)

#*********enlever les doulons d'une list ( par david )
#t = list(dict.fromkeys(t))

#**********version pierre henry*************
#import requests
#r = requests.get ("https://jsonplaceholder.typicode.com/todos")
#users = r.json()

#with open("users.txt","w") as f:
#    for user in users:
#        f.write("users.txt : "+str(user)+"\n")

#with open("users_filtred.txt","w") as f:
#    for user in users:
#        if(user["completed"]):
#            f.write("users_filtred.txt : "+str(user)+"\n")

#************************************** Tp log /yeduo ********
"""f = open ("smush.log","r")
entries = f.readlines()
for i in entries :
  data_type = i.split(" - ")[0]
  type_info = data_type.lstrip("[").rstrip("]")
  type_info_tmp = type_info.split(" : ")
  if(len(type_info_tmp)==2):
    if(type_info_tmp[1] == "INFO"):
      print(type_info_tmp[0])"""


"""names = ["Chrise","Valentin"]
for name in names:
  entries = name.readlines()
  print(name)"""

#*********************
#import requests
#URL=
#html_doc = requests.get(URL).text
html_doc = """ <ol style="list-style-type: decimal">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: decimal-leading-zero">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>
 
<ol style="list-style-type: upper-roman">
  <li class="elements">Élément1</li>
  <li class="elements">Élément2</li>
  <li class="elements">Élément3</li>
</ol>

<ol style="list-style-type: lower-roman">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: upper-alpha">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: lower-alpha">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: lower-greek">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol> """

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.find_all(class_="elements"))

#*********************request.get*****sur whithouse.gov *******ok
"""import requests
URL= "https://www.whitehouse.gov/about-the-white-house/presidents/"
html_doc_1 = requests.get(URL).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc_1,'html.parser')

presidents = soup.find_all(class_="acctext--con grid-item__title h4alt")
for president in presidents:
  print(president.text.strip())"""

#********************requests.get*******sur société.fr avec les datas donnés ***********

#import requests
#URL= "https://www.societe.com/cgi-bin/liste?nom=A&dirig=&pre=&ape=&dep="
#html_doc_2 = requests.get(URL).text

"""html_doc_2 =

<a href="/societe/basalpine-autocars-005450093.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">SARL BAS ALPINE D'AUTOCARS "S.B.A"</span><br />

Autres commerces de détail spécialisés divers (4778C)<br />

04800 GREOUX LES BAINS

</p>




<p class="chevron">></p>

</div>

</a>

<hr />


<a href="/societe/etablissements-a-porquet-005620091.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">ETABLISSEMENTS A PORQUET</span><br />

Fabrication d'autres articles de robinetterie (2814Z)<br />

80132 HAUTVILLERS OUVILLE

</p>




<p class="chevron">></p>

</div>

</a>

<hr />


<a href="/societe/chanel-et-andrieu-battages-005750187.html" class="txt-no-underline">

<div class="resultat">


<p class="iconsearch"><i class="icon-commerical-building"></i></p>

<p>

<span class="Link">SOCIETE DE BATTAGES ET DE MOTOCULTEURS A. CHANUEL & J. ANDRIEU</span><br />


04200 MISON

</p>




<p class="chevron">></p>

</div>

</a>

<hr />

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc_2,'html.parser')

Entreprises = soup.find_all(class_="resultat")
#print(Entreprises)
for Entreprise in Entreprises:
  print(Entreprise.span.text)"""

#**********************requests.post*********** non réussit********
"""import requests
URL= "https://sirene.fr/sirene/public/accueil"
r = requests.post(URL, data = {'recherche.sirenSiret':'' ,'recherche.raisonSociale': 'a','recherche.adresse': '','recherche.commune': '','__checkbox_recherche.excludeClosed':'true','recherche.captcha': ''}).text
print(r)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'html.parser')
Entreprises = soup.find_all(class_="accordion-group")
print(Entreprises)
for Entreprise in Entreprises:
  print(Entreprise.span.text)"""