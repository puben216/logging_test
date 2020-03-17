#! /usr/bin/bash

file=/home/mob/logging_test/example.log
echo "start hello" >> ${file}
python ./test.py ${file}
echo "end hello" >> ${file}
