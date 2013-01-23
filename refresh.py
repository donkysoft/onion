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
    tpls = {}
    compiles = {}

    def scanning(target):
        files = os.listdir(target)
        for file in files:
            if file[0] == '.':
                continue
            filename = os.path.join(target, file)
            if os.path.isdir(filename):
                scanning(filename)
            ext_flag = 0
            if len(ext) > 0:
                for e in ext:
                    if file.endswith(e):
                        ext_flag = 1
                        break;
            if ext_flag == 0:
                continue
            abs = filename.replace(document_root + os.sep, '')
            print 'file: %s' % abs
            filedir = []
            if (os.sep in abs) == True:
                arr = abs.split(os.sep)
                del arr[-1]
                filedir = arr[:]
            f = open(filename, 'r')
            html = f.read()
            f.close()
            html_org = html
            # looking for template tag
            tag_names = re.findall(r"<!--onion_tpl:(.*?)-->", html)
            if len(tag_names) <= 0:
                print ' - onion_tpl tag not found.'
                continue
            update_flag = 0
            for tag_name in tag_names:
                if not tag_name in tpls:
                    tpl_filename = os.path.join(dirname, 'item', tag_name + '.tpl')
                    if os.path.isfile(tpl_filename) == False:
                        print ' - %s.tpl not found.' % tag_name
                        continue
                    f = open(tpl_filename, 'r')
                    tpls[tag_name] = f.read()
                    f.close()
                if not tag_name in compiles:
                    compiles[tag_name] = re.compile(r"<!--onion_tpl:" + tag_name + r"-->((?:.|\n)+)<!--\/onion_tpl:" + tag_name + r"-->")
                tpl = pathtool.set_adjust_tpl(tpls[tag_name], filedir)
                html = re.sub(compiles[tag_name], "<!--onion_tpl:" + tag_name + "-->" + tpl + "<!--/onion_tpl:" + tag_name + "-->", html)
                if update_flag == 0 and html != html_org:
                    update_flag = 1
            if update_flag == 1:
                f = open(filename, 'w')
                f.write(html)
                f.close()
                print ' - update.'
            else:
                print ' - no update.'
                pass

    config = ConfigParser.SafeConfigParser()
    try:
        config.read(os.path.join(dirname, 'config.ini'));
    except Exception, e:
        print 'error: ', e
        quit()
    try:
        path = config.get('site', 'path')
        ext = config.get('site', 'ext')
        ext = ext.split(',')
    except Exception, e:
        print 'error: failed to get the configuration.'
        quit()
    document_root = os.path.join(os.getcwdu(), path)
    if os.path.isdir(document_root) == False:
        print 'error: does not exist [%s].' % document_root
        quit()
    scanning(document_root)
    return

if __name__ == '__main__':
    main()

