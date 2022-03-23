#!/bin/bash
set -e

git pull

python3 002_upbit_get_daily_candle.py
git add ..
git commit -m "[UPBit] auto generated site map & main page"
git push origin main
