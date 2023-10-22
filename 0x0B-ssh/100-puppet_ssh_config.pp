#!/usr/bin/env bash
# using puppet to make changes to our configu file

file { 'etc/ssh/ssh_cofig':
        ensure => present,

content =>"

        #SSH client configuration
        host*
        IdentityFile ~/.ssh/school
        PasswordAuthentification no
	",
}
