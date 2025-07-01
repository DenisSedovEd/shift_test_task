#!/bin/sh

set -e

echo "!!! Apply Django migrations !!!"
uvicorn main:app --reload
echo "!!! Successfully Django migrations !!!"

exec "$@"