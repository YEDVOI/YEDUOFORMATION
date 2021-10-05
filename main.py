# ********TP1*********
#ID=input ("Insérer votre votre ID:")
#Mdp=input ("insérer votre mot de passe:")
#if(ID == "admin") and (Mdp == "admin123"):
#  print("Bonjour ADMIN")
#else:
#  print("Mot de passe incorrect")
#
#**********Tp2/test*********
#import random
#random_number=random.randint(2,10)
#print(random_number)
#while(True):
#  selected_number=int(input("Veuillez entre le nombre:"))
#  if(random_number > selected_number):
#    print("trop petit")
#  elif(random_number < selected_number):
#    print("trop grand")
#  else:
#      print("bravo!")
#      break

#*****TP3*********
#for i in range(3):
#  ID=input ("Insérer votre votre ID:")
# Mdp=input ("insérer votre mot de passe:")
#if(ID == "admin") and (Mdp == "admin123"):
# print("Bonjour ADMIN")
#break
#else:
# print("Mot de passe incorrect")
#if(i==2):
# print("operation invalide")

#solution/while/prof************
#cpt =0
#while(True):
 # if(cpt>2):
  #  print("Operation Invalide")
   # break
  #username= input("veuillez entre votre username:")
  #password= input("veuillez entrer votre password:")
  #if (username == "admin" and password == "admin123"):
  #  print("bienvenue admin")
  #  break
  #else:
  #  print("mot de passe incorrect")
  #  cpt+=1

#**********Solution/while/ yeduo ok*********
#ID=input ("Insérer votre votre ID:")
#Mdp=input ("insérer votre mot de passe:")

#i=0
#while(i<2):
#  i+=1
#  if(ID == "admin") and (Mdp == "admin123"):
#    break
#  if(Mdp != "admin123"):
#    Mdp = input ("Reinsérer votre mot de passe:")
#if (Mdp != "admin123"):
#  print("invalid")
#else:
#  print("Bonjour ADMIN")
 


#**********Tp4*******
#import requests
#r=requests.get("https://jsonplaceholder.typicode.com/todos")
#users=r.json()
#for user in users:
#  if(user["completed"]):
#    print(user["title"])


#import requests
#r=requests.get("https://jsonplaceholder.typicode.com/todos")
#users=r.json()
#for user in users:
#  if(user["completed"]):
#    print(user)


#************david*************
#import requests
#data = requests.get("https://jsonplaceholder.typicode.com/todos")
#output=data.json()
#for element in output:
#  if(element['completed']):
#    print(element['userId'])   

#*******pour éliminer les doublons / david / ne marche pas ************
#import requests
#data = requests.get("https://jsonplaceholder.typicode.com/todos")
#output=data.json()

#t=[]
#for element in output:
#  if(element['completed']):

#    t=t.append(element['userId'])
#    t=duplicates(t)

import m3009
import Re_auth
import Re_auth_anti_bruteforce
#import main_1
