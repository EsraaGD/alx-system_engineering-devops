# Fix error 500 server error of a LAMP stack
exec { 'sed_replace':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
}