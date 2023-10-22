#!/usr/bin/env bash
# using puppet to make changes to our configu file

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
        ensure => present,

content =>"

        #SSH client configuration
        host*
        IdentityFile ~/.ssh/school
        PasswordAuthentification no
	",
}
