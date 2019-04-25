#!/bin/bash
heroku container:push web -a unrealists
heroku container:release web -a unrealists
aplay /usr/share/sounds/purple/alert.wav
