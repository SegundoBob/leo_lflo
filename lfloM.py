#!/usr/bin/python
#coding=utf-8
#@+leo-ver=5-thin
#@+node:bob06.20141008151944.1928: * @file lfloM.py
#@@first
#@@first
#@@language python
#@@tabwidth -4

import os
import shutil
import subprocess
import sys

import leo.core.leoBridge as leoBridge


#@+others
#@-others

TestDir = 'lflo'

def main():
    if os.path.exists(TestDir):
        shutil.rmtree(TestDir)
    os.makedirs(TestDir)
    bridge = leoBridge.controller(gui='nullGui', verbose=False,
        loadPlugins=False, readSettings=False)

    fpn1 = os.path.join(TestDir, 'test{0}.leo'.format(1))
    cmdrx = bridge.openLeoFile(fpn1)
    cmdrx.save()
    cmdrx.close()

    if True:
        returnCode = subprocess.call(['python', 'lfloS.py', fpn1])
        if returnCode:
            print("Subprocess.call() returned {0}".format(returnCode))

if __name__ == "__main__":
    main()

#@-leo
