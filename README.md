# FitTest
GUI for controlling bicycle fitting adjustment machine over COM serial ports

![image](https://user-images.githubusercontent.com/40705003/152251496-2f409a41-8eb7-4f5b-a06b-87832392b7fd.png)

# Easy Update Process
If everything is set up and running smoothly, open an Anaconda prompt and run
```
conda activate FitTest
```
Then
```
python update.py
```
This will pull updates from Github and rebuild the DynamicFitter executable.

# Building from Source (for complete beginners)

## Software Requirements

- Install [Git for Windows](https://git-scm.com/download/win).
- Install [Anaconda](https://www.anaconda.com/products/individual)

## Setting up Development Environment

From Git Bash, download the repository and change into its directory
```
git clone https://github.com/john-judge/FitTest.git
```

Then launch the Anaconda prompt and navigate to the directory just created:

```
cd FitTest
```

Create a Conda environment (which will install several packages) and activate it:
```
conda env create -f environment.yml --name FitTest
conda activate FitTest
```

## Building the DynamicFitter Executable

With the Conda environment activated, from the Anaconda prompt

```
pyinstaller -F -n fit --add-data source/images/*.png;./source/images/ driver.py
```

I recommend creating a shortcut to the application `fit.exe` and placing the shortcut on your desktop, to avoid having to move the executable. Otherwise, if moving the executable to a new location, the PNG images need to be in relative path `/source/images/` from the executable's directory.

## Updating
Run 
```git pull```
and then follow the instructions in the previous section (Building Executable). 

