# Define SSH client configuration file resource
file { 'ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  mode    => '0644',
  content => "
    Host 512587-web-01
        HostName '54.144.134.136'
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}

