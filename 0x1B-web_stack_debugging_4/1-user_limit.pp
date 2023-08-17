#setting reasonable limits for soft and hard file descriptors
#to ensure "holberton" user can log in and open files without encountering resource limit errors

user { 'holberton':
  ensure => present,
}

exec { 'holberton user soft limit':
  command => 'sed -i "/holberton soft nofile/s/.*/holberton soft nofile 4096/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin:/usr/sbin',
  require => User['holberton'],
}

exec { 'holberton user hard limit':
  command => 'sed -i "/holberton hard nofile/s/.*/holberton hard nofile 4096/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin:/usr/sbin',
  require => User['holberton'],
}
