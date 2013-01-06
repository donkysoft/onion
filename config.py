#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import ConfigParser

dirname = os.path.dirname(os.path.abspath(__file__))

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print 'Usage: # python %s [key]' % argv[0]
        print 'Usage: # python %s [key] [value]' % argv[0]
        quit()

    config = ConfigParser.SafeConfigParser()
    try:
        config.read(os.path.join(dirname, 'config.ini'));
    except Exception, e:
        print 'error: ', e

    if argc == 2:
        try:
            print config.get('site', argv[1])
        except Exception, e:
            print 'error: does not exist [%s].' % argv[1]
            quit()

    if argc == 3:
        try:
            value = config.get('site', argv[1])
        except Exception, e:
            print 'error: does not exist [%s].' % argv[1]
            quit()
        try:
            config.set('site', argv[1], str(argv[2]))
            config.write(open(os.path.join(dirname, 'config.ini'), 'w'))
        except Exception, e:
            print 'error: could not write to config file: %s' % e
            quit()
        print 'set config[%s]: %s -> %s' % (argv[1], value, argv[2])
        # isdir check
        path = os.path.join(os.getcwdu(), argv[2])
        if os.path.isdir(path) == False:
            print 'warning: does not exist [%s].' % path

if __name__ == '__main__':
    main()

