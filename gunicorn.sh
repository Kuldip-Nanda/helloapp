#!/bin/bash
gunicorn --config /app/gunicorn.config.py wsgi:app
