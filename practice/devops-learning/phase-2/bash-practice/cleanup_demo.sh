#!/bin/bash
set -e

cleanup() {
    echo "Cleaning up temporary files..."
    rm -f /tmp/demo_lock
}

trap cleanup EXIT

touch /tmp/demo_lock
echo "Working..."
cat /this/file/does/not/exist
echo ""This won't print"