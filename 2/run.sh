for i in {0000..0006}; do
    input_file="${i}_in.txt"
    output_file="${i}_out.txt"
    
    if [ -e "$input_file" ]; then
       

    else
        echo "Input file $input_file not found."
    fi
done