#!/usr/bin/env bash
python view.py
dev_appserver.py --host 10.244.0.113 --admin_host 10.244.0.113 --enable_host_checking 0 app.yaml
