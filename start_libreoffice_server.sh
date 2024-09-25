#!/bin/bash
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
libreoffice --accept="socket,host=localhost,port=2002;urp;" &
python3 ./lo_raw_server.py