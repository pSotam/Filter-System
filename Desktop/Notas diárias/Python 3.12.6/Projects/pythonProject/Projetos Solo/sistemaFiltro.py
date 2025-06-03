#Vai pedir por uma palavra que você deseja que seja filtrada, exemplo "laranja".
#Quando o usuário digitar, essa palavra vai ser colocada numa lista
#Uma caixa de texto vai pedir para o usuário testar
#O usuário vai poder acessar a lista quando quiser
#O usuário vai poder adicionar itens a lista
#O usuário vai poder remover itens da lista
#O usuário vai poder limpar os itens da lista

from time import sleep

palavras = [] #variável declarada antes do Loop pra poder ter resultados guardados na memória

while True:
    print('\n📓 Para ver a lista, digite "list"\n➕ Para adicionar uma palavra digite "add"\n➖ Para remover uma palavra, digite "del"\n❎ Para limpar a lista, digite "clear"\n⛔ Para sair, digite "quit"')
    escolha = str(input('Digite aqui: ').upper().strip())

    def filtrar_palavras():
        while True:
            palavraFiltrada = str(input('-------------------\nDigite uma palavra que você deseja filtrar: '))

            #.append serve para adicionar um termo ao final da lista
            palavras == palavras.append(palavraFiltrada)
            print('✅ Palavra filtrada com Sucesso!')
            print('📓 A nova lista de palavras filtradas é: {}\n-------------------'.format(palavras))
            while True:
                escolhaAdd = str(input('-------------------\nDeseja adicionar mais palavras?\n Digite "S" para adicionar ou "N" para não: ').upper().strip())

                if(escolhaAdd == "S"):
                    break
                elif(escolhaAdd == "N"):
                    sleep(2)
                    return
                elif (escolha not in ["S", "N"]):
                    print('❌ Escolha uma função válida!')
                    continue

    def remover_palavras():
        print("-------------------\nLista: {}".format(palavras))
        delPalavra = str(input('Digite uma palavra que você quer remover da lista (Certifique-se de que a palavra está escrita corretamente): '))
        checkPalavra = delPalavra in palavras
        if(checkPalavra == True):
            print('✅ Palavra removida com sucesso!')
            offPalavra = palavras.remove(delPalavra)
            print('📓 Sua nova lista é: \n{}\n-------------------'.format(palavras))
        elif(checkPalavra == False):
            print('❌ Não foi possível remover a palavra\nCertifique-se de que está escrita corretamente\n-------------------')
        sleep(2)
        return

    def limpar_lista():
        print("-------------------\nLista: {}".format(palavras))
        while True:
            checkAns = str(input('-------------------\nDeseja limpar a lista?\nDigite "S" para prosseguir ou "N" para cancelar: ').upper().strip())
            if(checkAns == 'S'):
                palavras.clear()
                print('✅ Lista limpada com sucesso!\n-------------------')
                print('📓 Sua nova lista é: {}\n-------------------'.format(palavras))
                sleep(2)
                break
            elif(checkAns == 'N'):
                sleep(2)
                return
            elif (checkAns not in ["S", "N"]):
                print('❌ Escolha uma opção válida!')
                continue

    def ver_lista():
        print('-------------------\nSua lista é:\n{}\n-------------------' .format(palavras))
        sleep(2)
        return

    def quit():
        print("👋 Adeus!")
        exit()

    if(escolha == "ADD"):
        filtrar_palavras()
    elif(escolha == "LIST"):
        ver_lista()
    elif(escolha == 'DEL'):
        remover_palavras()
    elif(escolha == 'CLEAR'):
        limpar_lista()
    elif(escolha == 'QUIT'):
        quit()
    elif(escolha not in ["ADD", "LIST", "DEL", "CLEAR", "QUIT"]):
        print('-------------------\n❌ Escolha uma função válida!\n-------------------')
        sleep(2)
        continue
