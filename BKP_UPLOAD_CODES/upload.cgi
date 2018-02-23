#!c:\perl\bin\perl5.10.1.exe
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);


my $cgi = new CGI;
#my $dir = $cgi->param('dir'); 
my $text_file = $cgi->param('text_seq');
my $file = $cgi->param('file');

print "Content-type: text/html\n\n";

#print $file,"\n";

#print "$text_file \n";
# $file=~m/^.*(\\|\/)(.*)/; 
# strip the remote path and keep the filename 
my $name = (); 

#print $name,"\n";




	
	#print "$file has been successfully uploaded... thank you.\n";
	#print << "HTML"; $file,"111111111-----\n"; 	HTML;

	


my @file_data=();
if($file=~m/(\.txt|\.fasta)$/ig )
{
 	$name = $file; 
	open(LOCAL, ">","$name") or carp $!; 
	while(<$file>) { print LOCAL $_; } 
	#print $file,"-----\n";
}
else
{
	open(LOCAL, ">","text_area_file.txt") or carp $!; 
	#push( @file_data ,split(/\n/,$text_file));
	#foreach(@file_data) { print LOCAL $_; } 
	print LOCAL $text_file;
	$name="text_area_file.txt";
}


close(LOCAL);

#print @file_data,"\n";

  #print $cgi->header(); 
 
  #print end_html;
  
  

  
  #$name =~s/.*\\//g;
  
  use strict;
  
  use TPMorder;
  
  use Benchmark;
  #my @files=glob("*.fasta");
  

  my $st = Benchmark->new();
  
  my $tpm_2 = TPMorder->new();
  # PROCESS MULTIPLE FASTA FILE IN TO HASH
  
  my $seq_hash1 = $tpm_2->file_process($name);
  
  #print $name,"\n";
  
  # CALCULATE TPM FOR GIVEN ORDER
  
  my $order = 2;
  
  my $self_mod1 = $tpm_2->TPM_main($order);
  # DISTANCE MATRIX OF THE SEQUENCES
  
  my $dist_mat2 = $tpm_2->distance_matrix();
  
  # MAKING TREE FROM THE DISTANCE MATRIX GENERATED
  
  $tpm_2->neighbor();

  
  #print "$file has been successfully uploaded... thank you.\n";
  
    $name =~s/.*\\//g;
    $name=~s/\.txt//g;
    $name=~s/\.fasta//g;
    
    my $path = "$order--$name";
    
  # print "$name";
  
  my $name_f="$order-outTREE-$name";
  
print "<a href = $path/phylo_svg.cgi>$order-outTREE-$name</a>";
  
 # print "$file has been successfully uploaded... thank you.\n";

 
  my $end = Benchmark->new();
  
 my $lag = timediff($st,$end);
  
#print "TIME REQUIRED FOR THE PROGRAM IS   ",timestr($lag),"   \n";






