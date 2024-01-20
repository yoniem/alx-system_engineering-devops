#!/usr/bin/env bash
# making changes to our configuration file using puppet

file { 'ect/ssh//ssh_cofig':
	ensure => present,

content =>"

	#ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	passwordAuthentication no

}
