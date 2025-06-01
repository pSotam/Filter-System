import random
from time import sleep
#Tamanho da senha (quantos caracteres)
#Se deve usar letras maiúsculas
#Se deve usar números
#Se deve usar símbolos

while True:
    while True:
        try:
            lenSenha = int(input('🔁 Quantas vezes cada opção vai se repetir? ').strip())
            if(lenSenha <= 0):
                print("❌ O número deve ser maior que zero!")
                continue
            else:
                break
        except ValueError:
            print("❌ Digite um número por favor!")

    print('Digite "sim" para aceitar ou aperte qualquer tecla para não')
    lowLetras = str(input('🔡 Deve ter letras minúsculas? ').upper().strip())
    capLetras = str(input('🔠 Deve ter letras maiúsculas? ').upper().strip())
    useNum = str(input('1️⃣ Deve usar números? ').upper().strip())
    useSimbol = str(input('❕ Deve usar símbolos?' ).upper().strip())
    useShuffle = str(input('🔂 Usar Shuffle na senha? ').upper().strip())

    listLow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listUpp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    listNum = ["1","2","3","4","5","6","7","8","9","0"]
    listSim = ["!","@","#","$","%","&","*","-","_","=","+","/","?",";",":",".",","]

    senha = ""

    for i in range(lenSenha):

        if(lowLetras == "SIM"):
            senha += random.choice(listLow)
        if(capLetras == "SIM"):
            senha += random.choice(listUpp)

        if(useNum == "SIM"):
            senha += random.choice(listNum)

        if(useSimbol == "SIM"):
            senha += random.choice(listSim)

        if(useShuffle == "SIM"):
            senha = list(senha)
            random.shuffle(senha)
            senha = ''.join(senha)

        if(i == lenSenha):
            break

    print("------------------\n🔑 Sua nova senha será: {}\n------------------".format(senha))
    sleep(2)
    print("Criar outra senha?")
    retornar = str(input('Digite "sim" para aceitar ou aperte qualquer tecla para não: ').upper())
    if(retornar == "SIM".upper().strip()):
        continue
    elif(retornar != "SIM".upper().strip()):
        break