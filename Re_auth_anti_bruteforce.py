cpt = 0 
while(True):
    if(cpt == 3):
        print("Operation Invalide")
        break
    username = input("Veuillez entrer votre username: ")
    password = input("Veuillez entrer votre password :")
    if (username == "admin" and password == "admin123"):
        print("Bienvenue Admin")
        break
    else : 
        print("Mot de passe incorrect")
        cpt+=1