#!/bin/bash

RETURN_CODE=0
echo "pylama ." \
&& pylama . \
&& echo "black" \
&& black --check . \
&& echo "pytest tests..." \
&& cd tests \
&& py.test -s -v test_sample.py \
&& py.test -s -v test_sample2.py \
&& py.test -s -v test_class1.py \
&& py.test -s -v test_class2.py \
&& py.test -s -v test_class3.py \
&& py.test -s -v test_class4.py \
&& py.test -s -v test_class5.py \
&& py.test -s -v test_class6.py \
&& py.test -s -v test_class7.py \
&& py.test -s -v test_class8.py \
&& py.test -s -v test_class9.py \
&& py.test -s -v test_class10.py \
&& py.test -s -v test_bonus1.py \
&& py.test -s -v test_bonus2.py \
&& py.test -s -v ../bonus2/exercises/test_ex3/test_simple.py \
&& py.test -s -v ../bonus2/exercises/test_ex4/test_netmiko.py \
&& py.test -s -v ../bonus2/exercises/test_ex5/test_netmiko_conftest.py \
\
|| RETURN_CODE=1

exit $RETURN_CODE
