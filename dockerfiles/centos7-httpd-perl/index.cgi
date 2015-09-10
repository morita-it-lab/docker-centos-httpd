#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "<html><body>";
print "<h1>Perl CGI</h1>";

print "<h2>perl -v</h2>";
print "<pre>";
print `perl -v`;
print "</pre>";

print "<h2>perl -V</h2>";
print "<pre>";
print `perl -V`;
print "</pre>";

print "<h2>PM</h2>";
print "<pre>";
print `find \`perl -e 'print "@INC"'\` -name '*.pm' -print`;
print "</pre>";

print "</body></html>";
