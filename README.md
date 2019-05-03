# loadDtar
load and get data from zipped files without full extraction

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
.
..
...
```
**Step3** : we are ready to start with `loadDtar` object

```
.
..
...
zip_file_path = 'file.tar' # could use either relative path or absolute path
tar = loadDtar(zip_file_path)

```

***
# command list
## loadDtar(_path_).getHeader()

this function will return all extracted lists in zipped file in numpy array

```
zip_file_path = 'file.tar' # could use either relative path or absolute path
tar = loadDtar(zip_file_path)

tar.getHeader()
```
will output

`['image.jpg','text.txt']`

## loadDtar(_path_).getOneExtract(_selected,mode=None,format='utf-8'_)

this function will extract and return just selected file

* selected : STRING, string of the selected files i.e. 'image.jpg'
* mode : STRING, Default= None | here is the lists of mode
    * 'image' : if an image will be extract.
    * 'text' : if text file will be extract.
* format : STRING, _(specified if only mode = 'text')_,Default= 'utf-8', format of the text file after extract i.e. 'utf-8'

example

```
zip_file_path = 'file.tar' # could use either relative path or absolute path
tar = loadDtar(zip_file_path)

tar.getOneExtract('image.jpg','image')
```

will output extracted numpy array of the image

```
[[4,5,6]
[4,5,7]
[4,5,8]
...
[134,45,95]
```

example

```
zip_file_path = 'file.tar' # could use either relative path or absolute path
tar = loadDtar(zip_file_path)

tar.getOneExtract('text.txt','text','utf-8')
```
will output extracted-formatted text in utf-8
`this is a text!!!!`

