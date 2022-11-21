#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")
day=$(date +"%d")

target_dir="$year/$month/$day"
mkdir -p "$target_dir"

pushd "$target_dir"
ln -s ../../../logo.png logo.png
popd
