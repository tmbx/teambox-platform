#!/bin/bash
# Invoke shell if build fails.

apt-get install -y --force-yes vim less 
cd /tmp/buildd/*/debian/..
/bin/bash < /dev/tty > /dev/tty 2> /dev/tty

