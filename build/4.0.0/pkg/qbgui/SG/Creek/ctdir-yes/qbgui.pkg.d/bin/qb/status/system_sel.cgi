#!/usr/bin/perl
require ("/usr/local/apache/qb/language/qblanguage.cgi");
@qblang = QBlanguage();

use CGI;

my $form=new CGI;
my $id = $form->param("id");


print "Content-type:text/html\n\n";
# print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">';
print '<html lang="en">';
print '<head>';
print '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">';
print '<title></title>';

print '	<style type="text/css">';
print '	button.menu{';
print '	width:70;';
print '	height:18;';
print '	font:10px Verdana;';
print '	color:white;';
print ' background:#336699;';	
print '	border:1px solid black;';
print '	cursor:hand;';
print 'margin-right: 5px;';
print '	}';
print '	</style>';
print '</head><body style="margin: 0px; background-color:#336699;" scroll="no">';
print '<script type="text/javascript" src="../qb.js"></script>';
print '<table style="width: 100%; height: 100%;">';
print '<tr style="height: 25px;"><td>';
print '<button class="menu"  onclick="mainframe.location=\'sys_status.php\'"     style="width: 14%">Real Time</button>';
print '<button class="menu"  onclick="mainframe.location=\'../sys_status_history.cgi\'"     style="width: 14%">History</button>';
print qq (</td></tr><tr><td><iframe frameborder="0" style="height:100%;width:100%" src="$id" name="mainframe"></iframe></td></tr></table></body></html>);
