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
RUN yum -y install make

RUN yum -y install gcc
RUN yum -y install zlib-devel
RUN yum -y install libxml2-devel
RUN yum -y install libyaml-devel
RUN yum -y install libxslt
RUN yum -y install libxslt-devel

# ----- Perl
RUN yum -y install perl
RUN yum -y install perl-CGI
RUN yum -y install cpan

# ----- Clean
RUN yum clean all

# httpd perl config
ADD perl-cgi.conf /etc/httpd/conf.d/perl-cgi.conf

# index.cgi
ADD index.cgi /var/www/html/index.cgi
RUN chmod -v u+x /var/www/html/index.cgi
RUN chmod -v g+x /var/www/html/index.cgi
RUN chown -v apache:apache /var/www/html/index.cgi
