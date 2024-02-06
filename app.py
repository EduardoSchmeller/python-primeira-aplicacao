import os
from colorama import init, Fore

init(autoreset=True)

restaurant = [{'name': 'Naruto Lamen', 'category': 'pasta', 'status': False},
              {'name': 'Loja de Tofu Fujiwara', 'category': 'japanese', 'status': True},
              {'name': 'Ichiraku', 'category': 'pasta', 'status': False}]

def program_name():
    print(Fore.GREEN + 'Sᴄʜᴍᴇʟʟᴇʀ Fᴏᴏᴅs\n')

def show_options():
    print(Fore.YELLOW + '1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')

def quit_program():
    invalid_input()

def return_main_menu():
    input(Fore.CYAN + 'Digite uma tecla para retornar ao menu inicial: ')
    main()

def screen_cleaner(input_text):
    os.system('clear')
    print(Fore.CYAN + input_text)

def invalid_input():
    print(Fore.RED + 'Opção inválida!\n')
    return_main_menu()

def list_restaurant():
    screen_cleaner('Listando Restaurantes:')
    for restaurants in restaurant:
        restaurant_name = restaurants['name']
        restaurant_category = restaurants['category']
        restaurant_status = restaurants['status']
        status_text = Fore.GREEN + 'Ativo' if restaurant_status else Fore.RED + 'Inativo'
        print(f'- {restaurant_name} | Categoria: {restaurant_category} | Status: {status_text}')
    return_main_menu()

def new_restaurant():
    screen_cleaner('Cadastro de novos restaurantes:')
    restaurant_name = input('Digite o nome do restaurante: ')
    restaurant_category = input('Digite a categoria do Restaurante: ')
    restaurant.append({'name': restaurant_name, 'category': restaurant_category, 'status': False})
    print(Fore.GREEN + f'O restaurante {restaurant_name} foi cadastrado com sucesso.')
    return_main_menu()

def changing_restaurant_status():
    screen_cleaner('Alterando estado do restaurante')
    restaurant_name = input('Digite o nome do restaurante desejado que deseja Ativar/Desativar: ')
    restaurant_selected = False

    for restaurants in restaurant:
        if restaurant_name == restaurants['name']:
            restaurant_selected = True
            restaurants['status'] = not restaurants['status']
            status_text = Fore.GREEN + 'ativado' if restaurants['status'] else Fore.RED + 'desativado'
            print(Fore.GREEN + f'O restaurante {restaurant_name} foi {status_text} com sucesso')

    if not restaurant_selected:
        print(Fore.RED + 'O restaurante não foi encontrado')

    return_main_menu()

def select_options():
    try:
        select_option = int(input(Fore.CYAN + 'Selecione uma opção: '))
        if select_option == 1:
            new_restaurant()
        elif select_option == 2:
            list_restaurant()
        elif select_option == 3:
            changing_restaurant_status()
        elif select_option == 4:
            print(Fore.YELLOW + 'Finalizando Programa')
        else:
            quit_program()
    except ValueError:
        invalid_input()

def main():
    os.system('clear')
    program_name()
    show_options()
    select_options()

if __name__ == '__main__':
    main()
