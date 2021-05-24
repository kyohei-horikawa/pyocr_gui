import PySimpleGUI as sg
from os.path import basename
import os

import convert
import ocr

group1 = [[sg.Text('x方向'), sg.InputText('0')],
          [sg.Text('y方向'), sg.InputText('0')]]

layout = [[sg.Text('ファイル選択', size=(15, 1), justification='left'),
           sg.InputText('ファイル一覧', enable_events=True,),
           sg.FilesBrowse('ファイルを追加', key='-FILES-', file_types=(('pdf', '*.pdf'),))],
          [sg.Listbox([], size=(100, 5), enable_events=True, key='-LIST-')],
          [sg.Radio('日本語', 1, key='-JAPANESE-', default=True), sg.Radio('英語', 1, key='-ENGLISH-')],
          [sg.Button('実行')], [sg.Button('終了')], [sg.Button('デバッグ')]]

window = sg.Window('pdf', layout)

new_files = []
new_file_names = []

while True:             # Event Loop
    event, values = window.read()
    if event in (None, '終了'):
        break

    if event == '実行':
        lang = 'jpn' if values['-JAPANESE-'] else 'eng'
        for file in new_files:
            convert.pdf_image(file)
        for image in os.listdir('./images'):
            ocr.image_text(image, lang)
        sg.popup('done')

    if event == 'デバッグ':
        print(values)

    elif values['-FILES-'] != '':

        tmp_files = values['-FILES-'].split(';')
        for tmp_file in tmp_files:
            if tmp_file not in new_files:
                new_files.append(tmp_file)
                new_file_names.append(basename(tmp_file))

        window['-LIST-'].update(new_file_names)  # リストボックスに表示します

window.close()
