#!/bin/bash

for i in {0000..0006}; do
    input_file="./000${i}_in.txt"
    output_file="./000${i}_out.txt"
    
    if [ -e "$input_file" ]; then
        input=$(cat $input_file)
        output=$(cat $output_file)

        python3 2.py "$input" "$output"
    else
        echo "Input file $input_file not found."
    fi
done