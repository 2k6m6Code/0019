#!/usr/bin/perl
require ("qbmod.cgi");
print "Content-type:text/html\n\n";

#get all links status (alive or dead)

use CGI;
use Data::Dumper;

    # WAN Link
    
    #my $ispref=XMLread('/usr/local/apache/active/basic.xml');
    #my $isplist=$ispref->{isp};

    #foreach my $isp ( @$isplist )
    #{
        #if ( $isp->{iid} eq 'system' ) { next; }
        #if ( $isp->{isptype} ne 'tunnel' &&  $isp->{isptype} ne 'ipsec' && $isp->{isptype} ne 'dtunnel' )
        #{
            #my $imgsrc = ( $isp->{alive} ) ? ( 'alive.png' ) : ( 'dead.png' );
            #print qq ($isp->{systemip},$imgsrc,);
            #if ( $isp->{alias_subnet1} )
            #{
            #    my @ip=split(/\// ,$isp->{alias_subnet1});
                my $show_status = runCommand(command=>'/usr/local/apache/qb/setuid/checkHuddlestate.sh');
                print qq ($show_status);
            #}
        #}
    #}
    
#
