#!/usr/bin/expect -f
# ssh
spawn ssh asusadmin@192.168.1.1 -p 1234
expect "*: "
sleep 1
# send password
send "password_here"
expect "$ "
send "reboot\r"
expect eof