#use strict;
use warnings;
use POSIX qw/ceil/;
use Scalar::Util qw(looks_like_number);
use constant PI => 4 * atan2(1, 1);
open(my $fh, '<', 'ku14b.dat') or die $!;

#my $s = "10";
#if (looks_like_number($s)) {
#  print "$s is a number\n";
#} else {
#  print "$s isn't a number\n";
#}


my $beam = 0;
my $beamplace = 1;
my $beam_val;
my $nth;
my $f1th; my $f2th; my $f3th; my $f4th; my $f5th; my $f6th; my $f7th; my $f8th; my $f9th;


while (<$fh>){
  $_=~ s/\r//;
  chomp;
  
  (undef, $first_word)=split(/\s+/, $_);
  if(($_ =~ /KU/)){
    if(looks_like_number($first_word)){
      $beam_val = $first_word/1000;
    }
  }
  if(($_ !~ /KU/)){
    $f1th = (split ' ', $_)[0];
    $f1th = cos($f1th*PI/180);
    $f2th = (split ' ', $_)[1];
    $f3th = (split ' ', $_)[2];
    $f4th = (split ' ', $_)[3];
    $f4th = cos($f4th*PI/180);

    $f5th = (split ' ', $_)[4];
    $f6th = (split ' ', $_)[5];
    $f7th = (split ' ', $_)[6];
    $f7th = cos($f7th*PI/180);

    $f8th = (split ' ', $_)[7];
    $f9th = (split ' ', $_)[8];

    #print "$f1th $f2th $f3th $f4th $f5th $f6th $f7th $f8th $f9th \n";

    print "$beam_val & 0.025 & $f1th & 0.015625 & $f2th & $f3th \n";
    print "$beam_val & 0.025 & $f4th & 0.015625 & $f5th & $f6th \n";
    print "$beam_val & 0.025 & $f7th & 0.015625 & $f8th & $f9th \n";
  }
  


  
  #next if (($_ =~ /!/)); #|| ($_ =~ /BARTALINI/)
  #print "$_ $iter \n";
  #my $getter = sprintf("getfile%.03f", $beam);
  #print $getter "$_ \n";
  #print "$getter \n";

}
close $fh;






