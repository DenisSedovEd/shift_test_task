#!/bin/sh

set -e

echo "!!! Run app !!!"
cd app
uvicorn main:app --host 0.0.0.0 --port 8000

exec "$@"