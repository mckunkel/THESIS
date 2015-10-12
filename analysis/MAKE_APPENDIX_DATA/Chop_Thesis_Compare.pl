use warnings;



open(my $f2h, '<', 'kuthesis.dat') or die $!;
open $my_README, ">kuthesis_edit.dat" or die "cannot open README file:$!";

while (<$f2h>){
  $_=~ s/\r//;
  chomp;

  next if (($_ =~ /& 0.025 & 	0.859375/));
  print "$_ \n";
  
  print $my_README "$_ \n";
  
}
close $my_README;
close $f2h;