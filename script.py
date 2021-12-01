import os
import shutil
from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
  [sg.Text('Pasta'), sg.Input(key='pasta')],
  [sg.Button('Renomear')]
]
#Janela
janela = sg.Window('Script para renomear arquivos', layout)
#Ler os eventos
while True:
  eventos, valores = janela.read()
  if eventos == sg.WIN_CLOSED:
    break
  if eventos == 'Renomear':
    main_folder = valores['pasta']
    print('RENOMEANDO...')

    def rename_file(file):
      file_name, file_extension = os.path.splitext(file)

      new_file =''
      file_aux = file_name
      count = 0
      index = 0

      while (count < 2) and (index < len(file_aux)):
        if file_aux[index] == '_':
          count += 1
          if count < 2:
            new_file += file_aux[index]
        else:
          new_file += file_aux[index]

        index +=1
      return f'{new_file}{file_extension}'

    def file_loop(root, files):
      count = 1
      current_file = ''
      previous_file = ''
      
      for file in files:
        new_file_name = rename_file(file)
        previous_file = current_file
        current_file = new_file_name

        if current_file == previous_file:
          count += 1
          file_name, file_extension = os.path.splitext(new_file_name)
          new_file_name = f'{file_name}({count}){file_extension}'
        else:
          count = 1

        old_file_fill_path = os.path.join(root, file)
        new_file_fill_path = os.path.join(root, new_file_name)

        print(f'RENOMEANDO: {file} para: {new_file_name}') 
        shutil.move(old_file_fill_path, new_file_fill_path)
      

    def main_loop():
      for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)


    if __name__ == '__main__':
      main_loop()
    
    print('FINALIZADO!!!')


# Script desenvolvido por José André
# Github: https://github.com/joseandre1706
# Linkedin: www.linkedin.com/in/josé-andré-psn
