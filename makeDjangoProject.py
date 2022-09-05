
import pyautogui as p
import time


######################## you need to install pyautogui and time to use this program #########################

confirm = p.confirm('Dont use your compute while this running **Only confirm the prompts**', 'confirm')


if confirm == 'OK':

    dir = p.prompt('Directory', 'Where do you want the virtual env to be saved?', default='desktop')
    venvName = p.prompt('Virtual env name', 'What do you want to name your virtual-env file?', default='django-venv')
    projectName = p.prompt('Project Name', 'Project name:', default='myProject')

    def deployProject():
       
        p.hotkey('win', 'r')
        p.write('cmd.exe')
        time.sleep(1)
        p.hotkey('enter')
        p.sleep(3)
        p.write('cd ' + dir)
        p.hotkey('enter')
        p.write('python -m venv ' + venvName)
        p.hotkey('enter')
        p.write(venvName + '\Scripts\\activate')
        p.hotkey('enter')
        p.write('cd '+ venvName)
        p.hotkey('enter')
        p.write('pip install django')
        p.hotkey('enter')
        time.sleep(1)
        p.write('django-admin startproject ' + projectName)
        p.hotkey('enter')
        p.write('cd ' + projectName)
        p.hotkey('enter')
        time.sleep(1)
        p.write('python manage.py migrate')
        p.hotkey('enter')
        p.write('python manage.py runserver')
        p.hotkey('enter')





def createApp():
    confirmApp = p.confirm('Do you want to create an app and a templates file?', 'Create App')
    
    if confirmApp == 'OK':
        createApp = p.prompt('Create App', 'Whats the name of your app?', default='name')
        time.sleep(2)
        p.hotkey('Ctrl', 'C')
        p.write('python manage.py startapp '  + createApp)
        p.hotkey('enter')
        time.sleep(1)
        p.write('md templates')
        p.hotkey('enter')

        
    else:
        exit()



deployProject()
time.sleep(15)
createApp()
