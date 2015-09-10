#
# CentOS7
# + utilities
# + httpd
# + php
#
FROM reneice/centos-httpd:latest
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>

# ----- Update
RUN yum -y update

# ----- Common utilities
RUN yum -y install vim
RUN yum -y install unzip

# ----- PHP
RUN yum -y install php
RUN yum -y install php-mysql

# ----- Clean
RUN yum clean all

RUN echo "<?php phpinfo(); ?>" > /var/www/html/index.php
