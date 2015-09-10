#
# CentOS7
# + httpd
#
# https://github.com/CentOS/CentOS-Dockerfiles/tree/master/httpd/centos7
#
FROM centos:7
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>

RUN yum -y update
RUN yum -y install httpd
RUN yum clean all

VOLUME /var/www/html

WORKDIR /var/www/html

# http port
EXPOSE 80
# https port
EXPOSE 443

ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
