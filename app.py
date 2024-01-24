import os

def program_name():
    print('Sᴄʜᴍᴇʟʟᴇʀ Fᴏᴏᴅs\n')

def show_options():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def quit_program ():
    os.system('clear')
    print('finalizando o APP')

def select_options():
    select_option = int (input('Selecione uma opcao: '))
    if select_option == 1:
        print('Cadastrar Restaurante')
    elif select_option == 2:
        print('Listar Restaurantes')
    elif select_option == 3:
        print('Ativar Restaurantes') 
    else:
        quit_program()


def main():
    program_name()
    show_options()
    select_options()

if __name__ == '__main__':
    main()