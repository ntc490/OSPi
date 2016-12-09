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
import sets
import datetime
import gv
import web


from helpers import plugin_adjustment, prog_match, schedule_stations, log_run, stop_onrain, check_rain, jsave, station_names
from urls import urls  # Provides access to URLs for UI pages
from gpio_pins import set_output

from program import *
p = Program()
print p
sys.exit(0)

def timing_loop():
    """ ***** Main timing algorithm. Runs in a separate thread.***** """
    pass

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
