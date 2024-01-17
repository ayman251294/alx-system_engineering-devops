# Fixing Apache returning a 500 error

exec { 'fix config typo':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
