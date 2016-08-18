#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sweet'

from bottle import route, run, template
from util import shell

@route('/supervisord/<action>/<target>', method='POST')
def supervisord(action='status', target=''):
    cmd = '/usr/local/bin/supervisorctl ' + action + ' ' + target
    output = shell.execute_command(cmd, shell=True)
    return output


run(host='localhost', port=8080)
