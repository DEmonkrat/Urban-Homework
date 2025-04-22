import os
import PySimpleGUI as sg

def_fold = r"D:\Program Files (x86)\Steam\steamapps\common\Twinsen's Little Big Adventure Classic\DotEmu\resources\LBA_FILES\VOICES"
cur_fold = def_fold
files_list = []


def set_dir():
    global cur_fold, files_list
    cur_fold = sg.popup_get_folder('Set folder to rename files:', default_path=def_fold, initial_folder=cur_fold)
    if cur_fold is not None:
        window['-STATUS-'].update(cur_fold + '   ')
        files_list = os.listdir(cur_fold)
        window['-M_LINE-'].update(cur_fold + '\n\nFiles:\n' + '\n'.join(files_list))


def rename_fold():
    global cur_fold, files_list
    if files_list:
        file=''
        for file in files_list:
            if file.startswith('EN'):
                os.rename(
                    os.path.join(cur_fold, file),
                    os.path.join(cur_fold, file.replace('EN', 'FR')))
    files_list = os.listdir(cur_fold)
    window['-M_LINE-'].update(cur_fold + '\n\nFiles:\n' + '\n'.join(files_list))


layout = [
    [sg.Text(cur_fold + '   ', expand_x=True, expand_y=True, key='-STATUS-', pad=(0, 10), auto_size_text=True,
             relief='sunken', size=(0, 2))],
    [sg.Button('Browse', key='-DIRECTORY-'),
     sg.Multiline(write_only=True,
                  auto_size_text=True,
                  expand_x=True,
                  size=(80, 10)
                  , key='-M_LINE-'
                  , enable_events=True)],
    [sg.Button('Rename files', key='-RENAME-')]
]

window = sg.Window('Rename_LBA', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EXIT-':  # if user closes window or clicks cancel
        break
    if event == '-DIRECTORY-':
        set_dir()
    if event == '-RENAME-':
        rename_fold()
