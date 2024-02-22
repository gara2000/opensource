#!/bin/bash
echo hello
uvicorn main:app --host 172.1.0.3 --port 3000 --reload