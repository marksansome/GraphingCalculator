#!/usr/bin/python

import ConfigParser

def configParser():
    config = ConfigParser.ConfigParser()

    #   reading
    config.read('../Assets/Settings.ini')
    print config.get('settings', 'mode') # -> "value1"

    #config.add_section('settings')
    #config.set('settings', 'mode', 'degree')
    #config.set('settings', 'history', '50')

    #with open('../Assets/Settings.ini', 'w+') as configfile:    # save
        #config.write(configfile)
