#
# CentOS7
# + utilities
# + httpd
# + perl
#
FROM reneice/centos-httpd:latest
MAINTAINER MASASHI MORITA <morita@mrita-it-lab.jp>

# ----- Update
RUN yum -y update

# ----- Common utilities
RUN yum -y install vim
RUN yum -y install unzip

# ----- Perl
RUN yum -y install perl
RUN yum -y install perl-CGI

# ----- Clean
RUN yum clean all

# httpd perl config
ADD perl-cgi.conf /etc/httpd/conf.d/perl-cgi.conf

# index.cgi
ADD index.cgi /var/www/html/index.cgi
RUN chmod -v u+x /var/www/html/index.cgi
RUN chmod -v g+x /var/www/html/index.cgi
RUN chown -v apache:apache /var/www/html/index.cgi
