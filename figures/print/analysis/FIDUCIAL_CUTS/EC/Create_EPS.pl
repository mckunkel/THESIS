#!/apps/bin/perl -w
use strict;
use warnings;

my $file_list = "totfile";

open my $FILE_f, "<", $file_list or die "Cannot open $file_list for read :$!";


while (<$FILE_f>) {
	chop($_);
	my $file = $_;
  my $match = $_;
  chop($match);chop($match);chop($match);
	my $epsF = $match."eps";
  #print "$epsF and $file \n";
  
	if(-e $epsF){
		print "Skipping this because $epsF exists. \n";
	}
	else{
    my $pdf2ps = "/Volumes/Mac_Storage/Work_Codes/PDF2THINGS/xpdfbin-mac-3.04/bin64/pdftops -eps $file";
    system($pdf2ps);
    #print " $pdf2ps  on   $file \n";
	}
}
close $FILE_f;
