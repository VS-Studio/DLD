#!/bin/sh

if [ -a pid ];then
    kill `cat pid`
    rm -f pid
fi

nohup python dld.py  2>&1 &
echo $! >> pid
