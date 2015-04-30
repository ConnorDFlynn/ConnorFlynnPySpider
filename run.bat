@echo off
python setup.py install
pyspider -c config.json
pause