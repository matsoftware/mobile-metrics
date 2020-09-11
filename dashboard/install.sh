#!/usr/bin/env bash

set -e

top=$(dirname $0)
python3 -m venv ${top}/venv

${top}/venv/bin/python3 ${top}/venv/bin/pip3 install -r ${top}/requirements.txt