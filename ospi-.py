# !/usr/bin/env python
# -*- coding: utf-8 -*-

import i18n

import json
import ast
import time
import thread
from calendar import timegm
import sys
sys.path.append('./plugins')
impport datetime

import web  # the Web.py module. See webpy.org (Enables the Python OpenSprinkler web interface)
import gv

from helpers import plugin_adjustment, prog_match, schedule_stations, log_run, stop_onrain, check_rain, jsave, station_names
from urls import urls  # Provides access to URLs for UI pages
from gpio_pins import set_output


# Global variables
PROGRAM_LIST = []


def sort_program_list(programs):
    """
    Sort the program list in reverse chronological order so the first program to
    trigger is first on the list.  This simplifies detection of a triggered
    program because we only have to check the first one.
    """
    pass

MODE_OFF = 0
MODE_AUTO = 1
MODE_TEST = 2

STATE_STOPPED = 0
STATE_FIND_PROGRAM = 1
STATE_RUNNING_PROGRAM = 2

class Controller(object):
    def __init__(self):
        self.mode = MODE_OFF
        self.state = STATE_STOPPED
        self.running_program = None

    def run(self):
        if self.state == STATE_FIND_PROGRAM:
            self.__find_program_state()
        elif self.state == STATE_RUNNING_PROGRAM:
            self.__running_program_state()
        elif self.state == STATE_STOPPED:
            pass

    def __find_program_state(self):
        global PROGRAM_LIST
        current_datetime = datetime.datetime.now()
        mutex.acquire()
        program_to_run = PROGRAM_LIST.get_ready_program(current_datetime)
        if program_to_run:
            # Copy program and any referenced data structures
            # Change state to 'running'
        mutex.release()

    def __running_program_state(self):
        
    


class OSPiApp(web.application):
    """Allow program to select HTTP port."""

    def run(self, port=gv.sd['htp'], *middleware):  # get port number from options settings
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


app = OSPiApp(urls, globals())
#  disableShiftRegisterOutput()
web.config.debug = False  # Improves page load speed
if web.config.get('_session') is None:
    web.config._session = web.session.Session(app, web.session.DiskStore('sessions'),
                                              initializer={'user': 'anonymous'})
template_globals = {
    'gv': gv,
    'str': str,
    'eval': eval,
    'session': web.config._session,
    'json': json,
    'ast': ast,
    '_': _,
    'i18n': i18n
}

template_render = web.template.render('templates', globals=template_globals, base='base')

if __name__ == '__main__':

    #########################################################
    #### Code to import all webpages and plugin webpages ####

    import plugins

    try:
        print _('plugins loaded:')
    except Exception:
        pass
    for name in plugins.__all__:
        print ' ', name

    gv.plugin_menu.sort(key=lambda entry: entry[0])
    #  Keep plugin manager at top of menu
    try:
        gv.plugin_menu.pop(gv.plugin_menu.index(['Manage Plugins', '/plugins']))
    except Exception:
        pass

    thread.start_new_thread(timing_loop, ())

    app.notfound = lambda: web.seeother('/')

    app.run()
