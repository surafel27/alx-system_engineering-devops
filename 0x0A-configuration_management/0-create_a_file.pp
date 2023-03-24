# Creating a file
file { '/tmp/school': # the path of the new file
    ensure  => 'present',
    replace => 'no',
    content => 'I love Puppet', # the content of the file
    mode    => '0744', # permission to the file
    owner   => 'www-data',
    group   => 'www-data',
}
