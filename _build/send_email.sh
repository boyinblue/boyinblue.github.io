#!/bin/bash

contents_file="${1}"
TMP_EMAIL_FILE="tmp/email.txt"

cp email_header.txt ${TMP_EMAIL_FILE}
cat ${contents_file} >> ${TMP_EMAIL_FILE}
cat ${TMP_EMAIL_FILE} | ssmtp -t -v
