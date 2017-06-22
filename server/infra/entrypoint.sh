#!/bin/bash
if [ ! -f /debug0 ]; then
  if [ -e requirements.txt ]; then
    pip3 install -r requirements.txt
  fi

  touch /debug0

  while getopts 'hdo:' flag; do
    case "${flag}" in
      h)
        echo "options:"
        echo "-h        show brief help"
        echo "-d        debug mode, no uwsgi, direct start with 'python app.py'"
        exit 0
        ;;
      d)
        touch /debug1
        ;;
      *)
        break
        ;;
    esac
  done
fi

if [ -e /debug1 ]; then
  echo "Running app in debug mode!"
  python3 app.py
else
  echo "Running app in production mode!"
  uwsgi --ini /app.ini
fi