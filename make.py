#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import ConfigParser
import re

dirname = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(dirname, 'libs'))
import pathtool

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print 'Usage: python %s [filename]' % argv[0]
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
        target = argv[1]
        if target.find(path + os.sep) == 0:
            cnt = len(path + os.sep)
            target = target[cnt:]
        file = os.path.join(os.getcwdu(), path, target)
        if os.path.isfile(file) == False:
            print 'error: does not exist [%s].' % file
            quit()
        f = open(file)
        html = f.read()
        f.close()
        # filedir
        filedir = []
        if (os.sep in target) == True:
            arr = target.split(os.sep)
            del arr[-1]
            filedir = arr[:]
        # looking for template tag
        tag_names = re.findall(r"<!--onion_tpl:(.*?)-->", html)
        if len(tag_names) <= 0:
            print 'onion_tpl not found.'
            quit()
        for tag_name in tag_names:
            m = re.search(r"<!--onion_tpl:" + tag_name + r"-->((?:.|\n)+)<!--\/onion_tpl:" + tag_name + r"-->", html)
            if m:
                inner_html = m.group(1)
                # adjust path
                inner_html = pathtool.set_adjust_path(inner_html, filedir)
                # save file
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

