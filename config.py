#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import ConfigParser

dirname = os.path.dirname(os.path.abspath(__file__))

def main():
    argvs = sys.argv
    argc = len(argvs)

    if argc < 2:
        print 'Usage: # python %s [key]' % argvs[0]
        print 'Usage: # python %s [key] [value]' % argvs[0]
        quit()

    config = ConfigParser.SafeConfigParser()
    try:
        config.read(os.path.join(dirname, 'config.ini'));
    except Exception, e:
        print 'error: ', e

    if argc == 2:
        try:
            print config.get('site', argvs[1])
        except Exception, e:
            print 'error: does not exist [%s].' % argvs[1]
            quit()

    if argc == 3:
        try:
            value = config.get('site', argvs[1])
        except Exception, e:
            print 'error: does not exist [%s].' % argvs[1]
            quit()
        try:
            config.set('site', argvs[1], str(argvs[2]))
            config.write(open(os.path.join(dirname, 'config.ini'), 'w'))
        except Exception, e:
            print 'error: could not write to config file: %s' % e
            quit()
        print 'set config[%s]: %s -> %s' % (argvs[1], value, argvs[2])
        # isdir check
        path = os.path.join(os.getcwdu(), argvs[2])
        if os.path.isdir(path) == False:
            print 'warning: does not exist [%s].' % path

if __name__ == '__main__':
    main()

