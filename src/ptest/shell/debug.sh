#!/bin/sh

gcc -g3 src/ptest/main.cpp && \
echo '' > src/ptest/log/result_calculate.log && \
gdb -q -x src/ptest/test/gdb_script_calculate.py a.out && \
echo '' && \
echo '' && \
echo '----- Next Test -----' && \
echo '' && \
echo '' > src/ptest/log/result_pair.log && \
gdb -q -x src/ptest/test/gdb_script_pair.py a.out && \
echo '' && \
echo '' && \
echo '----- Next Test -----' && \
echo '' && \
echo '' > src/ptest/log/result_bp.log && \
gdb -q -x src/ptest/test/gdb_script_bp.py a.out
