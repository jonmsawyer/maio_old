#!/bin/bash

ps aux | grep uwsgi | awk '{ print $2; }' | sudo xargs -n1 kill -9
