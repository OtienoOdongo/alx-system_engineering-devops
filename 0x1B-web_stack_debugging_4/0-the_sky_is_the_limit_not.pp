#fixing request limit to enable nginx server handle larger number of connections concurrently.

exec { 'increasing ulimit value':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => '/usr/bin:/usr/sbin:/bin',
  notify  => Service['nginx']
}

service { 'nginx':
  ensure => running,
  enable => true,
}
