#
# CentOS7
# + httpd
#
FROM centos:7
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>

RUN yum -y update
RUN yum -y install httpd
RUN yum clean all

WORKDIR /var/www/html

# http port
EXPOSE 80
# https port
EXPOSE 443

CMD /usr/sbin/apachectl -D FOREGROUND
