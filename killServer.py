
#coding: utf-8
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import subprocess

@route('/')
@route('/startProcess/<processName>')
def startProcess(processName):
    result = []
    process = subprocess.Popen(processName)
    
    errcode = process.returncode
   
    if errcode is not None:
        return 'FAILED to start: ' + processName

    return 'Start Process: ' + processName

@route('/killProcess/<processName>')
def killProcess(processName):
    subprocess.Popen("taskkill /F /IM " + processName , shell=True)

    return 'Tried to kill: ' + processName

@route('/isProcessActive/<processName>')
def killProcess(processName):
    tlcall = 'TASKLIST', '/FI', 'imagename eq %s' % processName
    # shell=True hides the shell window, stdout to PIPE enables
    # communicate() to get the tasklist command result
    tlproc = subprocess.Popen(tlcall, shell=True, stdout=subprocess.PIPE)
    # trimming it to the actual lines with information
    tlout = tlproc.communicate()[0].strip().split('\r\n')
    # if TASKLIST returns single line without processname: it's not running
    if len(tlout) > 1 and processName in tlout[-1]:
        return ('process "%s" is running!' % processName)
    else:
        print(tlout[0])
        return ('process "%s" is NOT running!' % processName)

@error(404)
def error404(error):
    return '404 error !!!!!'

run(host='localhost', port=8003, reloader=True)