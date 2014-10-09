#!/usr/bin/python
#coding=utf-8
#@+leo-ver=5-thin
#@+node:bob06.20141008151944.1929: * @file lfloS.py
#@@first
#@@first
#@@language python
#@@tabwidth -4

import sys

import leo.core.leoBridge as leoBridge


def main():
    fpn1 = sys.argv[1]
    bridge = leoBridge.controller(gui='nullGui', verbose=False,
        loadPlugins=False, readSettings=False)
    cmdr1 = bridge.openLeoFile(fpn1)
    cmdr1.save()
    cmdr1.close()

if __name__ == "__main__":
    main()

#@-leo
