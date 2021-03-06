#!/usr/bin/perl

require ('/usr/local/apache/qb/qbmod.cgi');

# ---------------------------------------------------------------
# main program start routine
# --------------------------------------------------------------
my $QB_BASIC_XML="/usr/local/apache/qbconf/basic.xml";
my $XL2TP_CONF="/etc/xl2tpd/xl2tpd.conf";

my $ispref=XMLread($QB_BASIC_XML);
my $isplist=$ispref->{isp};
my $ispname = $ARGV[0];
my $pptpserver = $ARGV[1];
my $pppoename = $ARGV[2];

open(L2TPD, "> $XL2TP_CONF" );

   if ( $ispname ) 
   { 
     print L2TPD qq(\[lac $ispname\] \n);
     print L2TPD qq(lns = $pptpserver \n);
     print L2TPD qq(redial = yes \n);
     print L2TPD qq(autodial = yes \n);
     print L2TPD qq(require chap = yes \n);
     print L2TPD qq(name = $pppoename \n);
     print L2TPD qq(length bit = yes \n);
     print L2TPD qq(ppp debug = no \n);
     print L2TPD qq(pppoptfile = /etc/ppp/options.xl2tpd.$ispname \n);
     print L2TPD qq(\n);
   }
foreach my $isp ( @$isplist ) 
{  
   if ( $isp->{isptype} eq "l2tp" && $isp->{pptpserver} ne "" ) 
   { 
     print L2TPD qq(\[lac $isp->{ispname}\] \n);
     print L2TPD qq(lns = $isp->{pptpserver} \n);
     print L2TPD qq(redial = yes \n);
     print L2TPD qq(autodial = yes \n);
     print L2TPD qq(require chap = yes \n);
     print L2TPD qq(name = $isp->{pppoename} \n);
     print L2TPD qq(length bit = yes \n);
     print L2TPD qq(ppp debug = no \n);
     print L2TPD qq(pppoptfile = /etc/ppp/options.xl2tpd.$isp->{ispname} \n);
     print L2TPD qq(\n);
   } 
}
close(L2TPD);
