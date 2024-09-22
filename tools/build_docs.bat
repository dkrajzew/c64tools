set PYTHONPATH=%PYTHONPATH%;..\src\
python C:\Python38\Lib\pydoc.py -w ..\c64tools\__init__.py
python C:\Python38\Lib\pydoc.py -w ..\c64tools\charpacker.py
python C:\Python38\Lib\pydoc.py -w ..\c64tools\charset2png.py
python C:\Python38\Lib\pydoc.py -w ..\c64tools\filemerge.py
python C:\Python38\Lib\pydoc.py -w ..\c64tools\mem2png.py
mkdocs build

