import time 
from time import sleep
import os


largura=50
fio=''
torção='S','Z'


def capturar_dados(lote,n_métrico,cor,torção):
    return{
        'Lote':lote,
        'Número métrico':n_métrico,
        'Cor':cor,
        'Torção':torção
    }

def main():

    producao=[]

    def limpar_tela():
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('Clear')

    print('«»'*30)
    print('Gerenciamento de lotes de produção:'.center(largura))
    print('«»'*30)
    sleep(1)
    

    while True:
            try:
                print('-='*30)
                opçoes=int(input('''ESCOLHA UMA OPÇÃO:\n[1]Cadastrar novo lote\n[2]Ver lotes cadastrados\n[3]Sair do sistema\n'''))

                if opçoes==1:
                    
                    while True:
                        try:
                           


                            lote=int(input('Digite o número do lote:'))
                            sleep(0.5)
                            n_métrico=float(input(f'Número métrico:'))
                            sleep(0.5)
                            cor=str(input('Cor do Fio:')).upper().strip()
                            sleep(0.5)
                            torção=str(input('Torção do Fio [S/Z]')).upper().strip()
                            sleep(0.5)
                            if torção not in ('S','Z'):
                                print('Valor inválido,tente novamente!!')
                                continue
                            producao.append(capturar_dados(lote,n_métrico,cor,torção))
                            print('Lote cadastrado com sucesso!!')
                            sleep(1)
                            break
                        except ValueError:
                            print('Valor inválido,tente novamente!!')
                           
                elif opçoes==2:
                    limpar_tela()
                   
                    if not producao:
                        print('Nenhum lote cadastrado!!')
                    else:
                        print('Lotes cadastrados:'.center(largura))
                        for lote in producao:
                            print('-='*30)
                            for k,v in lote.items():
                                print(f'{k}:{v}')
                    
                    sleep(1)

                else:
                    if opçoes==3:
                        limpar_tela()
                        print('Saindo do Sistema...')
                        time.sleep(1)
                        print('Obrigado por utilizar nosso sistema!!')
                        break


                    else:
                        print('Opção inválida,tente novamente!!')
                        continue
                    
                    

        
    
            except ValueError:
              print('Erro eminente,digite uma opção !!')
            except Exception as erro:
              print(f'Erro inesperado,tente novamente!!\n{erro}')


if __name__=='__main__':
    main()

