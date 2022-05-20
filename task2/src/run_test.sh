#!/bin/sh

file_name=$1
for num in {1..7}
do
    python $file_name "./test_case/case$num.txt"
done