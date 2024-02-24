# make changes to our config file to allow
# configured to use the private key ~/.ssh/school
# configured to refuse to authenticate using a password

include stdlib

# Ensure the SSH private key is added to the SSH config file
file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => 'IdentityFile ~/.ssh/school',
  match              => '^IdentityFile ~/.ssh/id_rsa',
  replace            => false,
}

# Ensure password authentication is disabled in the SSH config file
file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => 'PasswordAuthentication no',
  match              => '^PasswordAuthentication yes',
  replace            => false,
}

