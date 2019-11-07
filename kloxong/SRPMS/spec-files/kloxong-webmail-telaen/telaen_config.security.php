<?php

defined('I_AM_TELAEN') or die('Direct access not permitted');

########################################################################
# Enable visualization of HTML messages
# *This option afect only incoming messages, the  HTML editor
# for new messages (compose page) is automatically activated 
# when the client's browser support it (IE5 or higher)
########################################################################

$allow_html 			= yes;

########################################################################
# FILTER javascript (and others scripts) from incoming messages
##  $allow_script is DEPRECIATED and exists for backward
##  compatibility only. Instead, use $sanitize_html
########################################################################
$allow_scripts			= no;
$sanitize_html                  = yes;


########################################################################
# Block external images.
# If an HTML message have external images, it will be 
# blocked. This feature prevent spam tracking
########################################################################

$block_external_images = no;

########################################################################
# Session timeout for inactivity
########################################################################

$idle_timeout = 20; //minutes

########################################################################
# Require cookies enabled to handle session
########################################################################

$enable_cookies			= yes;

########################################################################
# Control the default permissions of files and directories created
# by Telaen. For max security, the value of $default_umask should be 0077
# and $dirperm should be 0700, but in shared environments, this
# may need to be adjusted
########################################################################

$default_umask = 0077;
$dirperm = 0700;

?>
