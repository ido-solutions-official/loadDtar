# loadDtar
load and create dataset from .tar files without extraction

## Version Beta 0.1
compatible zip
* .tar
* .tgz
* .tar.gz


# How to use

for example, we are working on PythonCode.py, and given folder structure below;

```
folder
|__file.tar
    |__ image.jpg
    |__ text.txt
|__PythonCode.py
```

**Step1** : clone this git into your folder

just clone this git into your working folder;

```
folder
|__file.tar
    |__ image.jpg
    |__ text.txt
|__loadDtar  <-- put it here
|__PythonCode.py
```
**Step2** : import files on top of your Python project
for example, in your PythonCode.py
```
from loadDtar import loadDtar 
```

and we are ready to use `loadDtar`


## 

