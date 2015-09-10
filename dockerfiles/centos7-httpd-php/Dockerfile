#
# CentOS7
# + utilities
# + httpd
# + php
#
FROM centos:7
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>

RUN yum -y update

# ----- Common utilities
RUN yum -y install vim
RUN yum -y install unzip

# ----- httpd
RUN yum -y install httpd

# ----- php
RUN yum -y install php
RUN yum -y install php-mysql

# ----- clean
RUN yum clean all

WORKDIR /var/www/html

RUN echo "<?php phpinfo(); ?>" > /var/www/html/index.php

# http port
EXPOSE 80
# https port
EXPOSE 443

CMD /usr/sbin/apachectl -D FOREGROUND
