#!/bin/sh
# Don't rebuild man-db.

echo "I: Preseed man-db/auto-update to false."
debconf-set-selections <<EOF
man-db man-db/auto-update boolean false
EOF
echo "I: Touching /CurrentlyBuilding for mandb."
touch /CurrentlyBuilding

