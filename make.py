#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import ConfigParser
import re

dirname = os.path.dirname(os.path.abspath(__file__))

def main():
    argvs = sys.argv
    argc = len(argvs)

    if argc < 2:
        print 'Usage: # python %s [filename]' % argvs[0]
        quit()

    config = ConfigParser.SafeConfigParser()
    try:
        config.read(os.path.join(dirname, 'config.ini'));
    except Exception, e:
        print 'error: ', e
        quit()

    if argc == 2:
        try:
            path = config.get('site', 'path')
        except Exception, e:
            print 'error: failed to get the configuration.'
            quit()
        file = os.path.join(os.getcwdu(), path, argvs[1])
        if os.path.isfile(file) == False:
            print 'error: does not exist [%s].' % file
            quit()
        f = open(file)
        html = f.read()
        f.close()
        # looking for template tag
        tag_names = re.findall("<!--onion_tpl:(.*?)-->", html)
        if len(tag_names) <= 0:
            print 'onion_tpl not found.'
            quit()
        for tag_name in tag_names:
            m = re.search("<!--onion_tpl:" + tag_name + "-->((?:.|\n)+)<!--\/onion_tpl-->", html)
            if m:
                inner_html = m.group(1)
                file = os.path.join(dirname, 'item', tag_name + '.tpl')
                try:
                    f = open(file, 'w')
                    f.write(inner_html)
                    f.close()
                    print 'save to [%s].' % tag_name
                except Exception, e:
                    print 'error: failed to save the file [%s].' % file
                    continue
            else:
                print 'warning: no contents [%s].' % tag_name
                continue

if __name__ == '__main__':
    main()

