#!/bin/sh

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="Script executed to setup the machine"
NAME=nextboot.sh
SCRIPTNAME=/etc/init.d/$NAME.sh

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.0-6) to ensure that this file is present.
. /lib/lsb/init-functions

case "$1" in
  start|force-start)
	[ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
	
        cd /update
        ./nextboot.py >> update.log 2>&1
	case "$?" in
		0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
		2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
	esac
	;;
  stop|force-stop)
        ;;
  restart|force-reload)
	;;
  *)
	echo "Usage: $SCRIPTNAME {start|stop|restart|force-reload}" >&2
	exit 3
	;;
esac

:
