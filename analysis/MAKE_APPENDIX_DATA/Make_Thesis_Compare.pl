use warnings;



open(my $f2h, '<', 'out.dat') or die $!;
open $my_README, ">thesis_check.dat" or die "cannot open README file:$!";

while (<$f2h>){
  $_=~ s/\r//;
  chomp;

  next if (($_ =~ /0.00000/));
  print "$_ \n";
  
  print $my_README "$_ \n";
  
}
close $my_README;
close $f2h;