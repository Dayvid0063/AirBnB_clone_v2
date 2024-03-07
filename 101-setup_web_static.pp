# Install and Start Nginx with the updated config

# Package definition for Nginx
package { 'nginx':
  ensure => 'installed',
}

# Nginx is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

# Define directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>",
}

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test/index.html'],
}

# Nginx config
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
