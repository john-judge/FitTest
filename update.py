import os
import time

os.system('cmd /c "color a"')
os.system('cmd /c "cd Desktop"')
os.system('cmd /c "cd FitTest"')
os.system('cmd /c "git pull"')
os.system('cmd /c "conda activate FitTest"')  # needed because Pyinstaller doesn't like to include itself as dependency
os.system('cmd /c "pyinstaller -n DynamicFitter --add-data source/images/*.png;./source/images/ driver.py --noconfirm"')
time.sleep(3)