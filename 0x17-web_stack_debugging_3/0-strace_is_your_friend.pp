# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Ensure the mod_rewrite module is enabled
exec { 'enable_mod_rewrite':
  command => '/usr/sbin/a2enmod rewrite',
  unless  => '/usr/sbin/apache2ctl -M | grep rewrite_module',
  notify  => Service['apache2'],
}

# Ensure Apache is restarted if the module is enabled
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['enable_mod_rewrite'],
}

