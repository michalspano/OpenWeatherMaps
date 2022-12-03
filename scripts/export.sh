#!/bin/sh

PANDOC=/usr/local/bin/pandoc

# colors
RED='\033[91m'; ORANGE='\033[93m'
GREEN='\033[92m'; RESET='\033[0m'
# check if pandoc is installed
if ! [ -x $PANDOC ]; then
    echo "${RED}ERROR:${RESET} \`pandoc\` is not installed"
    echo "- Docs: https://github.com/jgm/pandoc"
    exit 1
fi

INPUT_FILE=$1; OUTPUT_FILE=$2

# ensure that the input file exists
if ! [ -f $INPUT_FILE ]; then
    echo "${RED}ERROR:${RESET} \`$INPUT_FILE\` is invalid/does not exist"
    exit 1
fi

# if the output file is not specified, use the default one
if [ -z $OUTPUT_FILE ]; then
    echo "${ORANGE}WARNING:${RESET} No output file specified (default: \`out.pdf\`)."
    OUTPUT_FILE="out.pdf"
fi

# perform the conversion
$PANDOC -s -o $OUTPUT_FILE $INPUT_FILE
echo "${GREEN}SUCCESS:${RESET} File \`$OUTPUT_FILE\` created."
