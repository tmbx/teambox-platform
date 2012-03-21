The sys/ directory contains the seeds of the system packages included in the
Teambox distribution. The seeds were taken as-is from
http://people.canonical.com/~ubuntu-archive/seeds/platform.karmic/. The
'STRUCTURE', 'boot' and the 'teambox' files were hand-crafted. Do not create
extra files in this directory because this will break 'krelease'.

The 'cmd' file is used by 'krelease' to invoke 'germinate'.

Note that germinate works on binary packages, not on source packages.

FDG has written a nice tutorial on 'germinate' which you can find at
http://lostwebsite.wordpress.com/2008/10/21/partial-debian-mirrors/

