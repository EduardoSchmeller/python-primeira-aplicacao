import os

restaurant = [{'name' : 'Naruto Lamen', 'category':'pasta', 'status' :False},
              {'name' : 'Loja de Tofu Fujiwara', 'category':'japanese', 'status' :True},
              {'name' : 'Ichiraku', 'category':'pasta', 'status' :False}]

def program_name():
    print('Sᴄʜᴍᴇʟʟᴇʀ Fᴏᴏᴅs\n')

def show_options():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def quit_program ():
    invalid_input()

def return_main_menu():
    input('digite uma tecla para retornar ao menu inicial: ')
    main()

def screen_cleaner(input):
    os.system('clear')
    print(input)         

def invalid_input():
    print('Opcao invalida!\n')
    return_main_menu()   

def list_restaurant():
    screen_cleaner('Listando Restaurantes:')
    for restaurants in restaurant:
        restaurant_name = restaurants ['name']
        restaurant_category = restaurants ['category']
        restaraunt_status = restaurants ['status']
        print(f'- {restaurant_name} | Category: {restaurant_category} | Status: {restaraunt_status}')
    return_main_menu()

def new_restaurant():
    screen_cleaner('Cadastro de novos restaurantes:')
    restaurant_name = input('Digite o nome do restaurante:')
    restaurant_category = input('Digite a categoria do Restaurante:')
    restaurant.append({'name':restaurant_name, 'category':restaurant_category, 'status':False })
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso.')
    return_main_menu()   

def select_options():
    try:
        select_option = int (input('Selecione uma opcao: '))
        if select_option == 1:
            new_restaurant()
        elif select_option == 2:
            list_restaurant()
        elif select_option == 3:
            print('Ativar Restaurantes') 
        elif select_option == 4:
            print('Finalizando Programa')    
        else:
            quit_program()
    except:
        invalid_input()   

def main():
    os.system('clear')
    program_name()
    show_options()
    select_options()

if __name__ == '__main__':
    main()
