#!/usr/bin/python3

import os.path
from os import system


str_strike = "\x1b[9m{}\x1b[0m"
filename = '' 
tasks = []

def restore():
    global tasks

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            tasks = [line.replace('\n' ,'') for line in file.readlines()]
            print(tasks)
            print("Restaurado com sucesso.\n")
    else:
        print(f'Você não tem um arquivo chamado {filename}.\n')

    return tasks


def save():
    global tasks
    with open(filename, 'w') as file:
        file.write('\n'.join(tasks))
        print('Salvo com sucesso.\n')


def done():
    global tasks
    print('\n'.join(f"{index + 1}) {task}" for index, task in enumerate(tasks)))
    task_done = input("Qual tarefa foi concluida?\n~ ")
    if task_done.isnumeric():
        tasks[int(task_done) - 1] = str_strike.format(tasks[int(task_done) - 1])

    else:
        for index, task in enumerate(tasks):
            if task.startswith(task_done):
                tasks[index] = str_strike.format(tasks[index])
    
    print("Feito!\n")
    


def add():
    global tasks
    task = input("Digite a tarefa.\n~ ")
    tasks.append(task)
    

def main():
    global filename
    menu = "\n\nManual:\n\ns - Para salvar.\nr - Para recuperar.\na - Adicionar tarefa.\nc - Para marcar tarefa como concluida\nl - Para listar as tarefas.\nq - Para sair\n\n"
    while(True):
        choice = input(menu)
        system("clear")
        match choice:
            case "s":
                if filename == '':
                    filename = input("Digite o caminho até o arquivo.\n")
                save()
            case "r":
                if filename == '':
                    filename = input("Digite o caminho até o arquivo.\n")
                restore()
            case "a":
                add()
            case "c":
                done()
            case "l":
                print('\n'.join(f"{index + 1}) {task}" for index, task in enumerate(tasks)))
            case "q":
                return
        

if __name__ == "__main__":
    main()
                
                

