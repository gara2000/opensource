#!/bin/bash
echo hello
uvicorn main:app --host 172.1.0.4 --port 3001 --reload