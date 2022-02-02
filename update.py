import os

os.system('cmd /c "color a"')
os.system('cmd /c "git pull"')
os.system('cmd /c "pyinstaller -n DynamicFitter --add-data source/images/*.png;./source/images/ driver.py --noconfirm"')