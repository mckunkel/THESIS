use strict;
use warnings;
use POSIX qw/ceil/;
use Scalar::Util qw(looks_like_number);
use constant PI => 4 * atan2(1, 1);
#open(my $fh, '<', 'kuthesis_edit.dat') or die $!;
#open(my $fh, '<', 'kuthesis.dat') or die $!;
open(my $fh, '<', 'thesis_check.dat') or die $!;

open my $my_README, ">complete_thesis.dat" or die "cannot open README file:$!";

my $f1th; my $f2th; my $f3th; my $f4th; my $f5th; my $f6th; my $f7th; my $f8th; my $f9th; my $f10th; my $f11th; my $f12th; my $f13th; my $f14th;
my $f5th_sub; my $f9th_sub;

my $nn = 0;
while (<$fh>){
  $_=~ s/\r//;
  chomp;
  $nn++;
  
  $f1th = (split ' ', $_)[0];
  $f2th = (split ' ', $_)[1];
  $f3th = (split ' ', $_)[2];
  $f4th = (split ' ', $_)[3];
  $f5th = (split ' ', $_)[4];
  #chop($f5th); chop($f5th); chop($f5th);
  $f5th_sub  = substr $f5th, 0, 5;
  #$f5th =~ s/\D+//g;
  #$f5th =~s/[^\d.]//g;
  #$#f5th  =  $f5th*10;
  #$f5th  = substr $f5th, 4, 3;
  
  $f6th = (split ' ', $_)[5];
  $f7th = (split ' ', $_)[6];
  $f8th = (split ' ', $_)[7];
  $f9th = (split ' ', $_)[8];
  $f9th_sub  = substr $f9th, 0, 5;

  $f10th = (split ' ', $_)[9];
  $f11th = (split ' ', $_)[10];
#  $f12th = (split ' ', $_)[11];
#  $f13th = (split ' ', $_)[12];
#  $f14th = (split ' ', $_)[13];
  #print "$f1th $f2th $f3th $f4th $f5th $f6th $f7th $f8th $f9th \n";
  #print "############################### \n \n";

  my $g1th; my $g2th; my $g3th; my $g4th; my $g5th; my $g6th; my $g7th; my $g8th; my $g9th; my $g10th; my $g11th; my $g12th; my $g13th;
  
  my $g5th_sub; my $g9th_sub;
  
  
  my $catch; my $count =0;
  
  #open(my $fh_2comp, '<', 'thesis_check.dat') or die $!;
  open(my $fh_2comp, '<', 'kuthesis_new.dat') or die $!;

  while (<$fh_2comp>){
    $_=~ s/\r//;
    chomp;
    
    $g1th = (split ' ', $_)[0];
    $g2th = (split ' ', $_)[1];
    $g3th = (split ' ', $_)[2];
    $g4th = (split ' ', $_)[3];
    $g5th = (split ' ', $_)[4];
    $g5th_sub  = substr $g5th, 0, 5;

    $g6th = (split ' ', $_)[5];
    $g7th = (split ' ', $_)[6];
    $g8th = (split ' ', $_)[7];
    $g9th = (split ' ', $_)[8];
    $g9th_sub  = substr $g9th, 0, 5;
    $g10th = (split ' ', $_)[9];
    $g11th = (split ' ', $_)[10];
    $g12th = (split ' ', $_)[11];
    $g13th = (split ' ', $_)[12];
    #print "$g1th $g2th $g3th $g4th $g5th_sub $g6th $g7th $g8th $g9th \n";
#    if($f5th_sub==0.390 && $f1th==$g1th){
#    print "$f1th $f5th_sub $f9th_sub $g1th $g5th_sub $g9th_sub \n";
#    }
    if($f1th==$g1th && $f5th_sub==$g5th_sub ){ #&& $f9th_sub==$g9th_sub
      #print "match \n";
      #print $my_README "$f1th $f2th $f3th $f4th $f5th $f6th $f7th $f8th $f9th $f10th $f11th $f12th $f13th $f14th\n";
      #print $my_README "$f1th $f2th $f3th $f4th $f5th_sub $f6th $f7th $f8th $f9th $f10th $f11th \n";
      
      print $my_README "$g1th $g2th $g3th $g4th $g5th $g6th $g7th $g8th $g9th $g10th $g11th $g12th $g13th  \\ \n";
      
#      #For error points
#      print $my_README "$f1th $f5th_sub $f9th \n";
#      
#      print $my_README "$g1th $g5th_sub $g9th \n";
#      print $my_README "############################### \n \n";

      $count++;
      #last;
    }
    
  }
  close $fh_2comp;

  
  
}




#next if (($_ =~ /!/)); #|| ($_ =~ /BARTALINI/)
#print "$_ $iter \n";
#my $getter = sprintf("getfile%.03f", $beam);
#print $getter "$_ \n";
#print "$getter \n";

close $fh;






