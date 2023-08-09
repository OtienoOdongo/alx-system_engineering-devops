# fixing Apache 500 internal server error

exec { 'fix_php_extension issue':
  command => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin/:/usr/bin/:/usr/local/bin/:/usr/sbin/'
}
