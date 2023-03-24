file { '/tmp/school':
    ensure  => 'present',
    replace => 'no',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
