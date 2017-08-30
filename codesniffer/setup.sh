#!/bin/sh

if [ ! -d ".git/hooks" ]; then
    mkdir -p .git/hooks
fi

cp ./etc/codesniffer/pre-commit .git/hooks/pre-commit
cp ./etc/codesniffer/config .git/hooks/config
chmod +x .git/hooks/pre-commit
