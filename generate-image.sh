#!/bin/bash
for FILE in *dot; do
    echo "$FILE"
    dot -Tsvg $FILE -o docs/data/$FILE.svg
done