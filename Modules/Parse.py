#!/usr/bin/python

import ConfigParser

def configParser():
    config = ConfigParser.ConfigParser()

    #   reading
    #config.read('config.ini')
    #print config.get('main', 'key1') # -> "value1"

    config.add_section('settings')
    config.set('settings', 'mode', 'degree')
    config.set('settings', 'history', '50')

    with open('../Assets/file.ini', 'w+') as configfile:    # save
        config.write(configfile)
