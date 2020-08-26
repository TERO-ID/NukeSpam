import os
while True:
  num =str(input())
  if num == ('1') :
    os.system("clear")
    print('Загрузка NukeSpam...')
      os.system("git clone https://github.com/TERO-ID/NukeSpam/")
      os.system("cd NukeSpam")
      os.system("pip install -r requirements.txt")
    print('Запуск NukeSpam...')
      os.system("python NukeSpam.py")