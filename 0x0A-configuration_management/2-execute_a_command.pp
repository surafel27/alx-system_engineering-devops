# Execution of commands to kill process
exec {'pkill killmenow':
    path => '/usr/bin:/usr/sbin:/bin:'
}
