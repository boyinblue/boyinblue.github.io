#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")
day=$(date +"%d")

target_dir="$year/$month/$day"
mkdir -p "$target_dir"

cp _index.md "$target_dir/index.md"