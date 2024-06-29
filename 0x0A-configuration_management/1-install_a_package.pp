#installing flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  command  => '/usr/bin/pip3',
}

-> exec { 'verify flask installation':
  command     => '/usr/bin/flask --version',
  refreshonly => true,
  subscribe   => Package['flask'],
  path        => ['/usr/local/bin', '/usr/bin', '/bin'],
}
