#!c:\perl\bin\perl.exe
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use threads;

my $cgi = new CGI;
my $text_file = $cgi->param('text_seq');
my $file = $cgi->param('file');


my $name = (); 
 
 my @file_data=();
 
 if($file=~m/(\.txt|\.fasta)$/ig )
 {
  	$name = $file; 
 	open(LOCAL, ">","$name") or carp $!; 
 	while(<$file>) { print LOCAL $_; } 
 }
 else
 {
 	open(LOCAL, ">","text_area_file.txt") or carp $!; 
 	print LOCAL $text_file;
 	$name="text_area_file.txt";
 }
 
 
 close(LOCAL);
 
 
 use strict;
   
   use TPMorder;
   use Storable;
   use Benchmark;
   
   my $st = Benchmark->new();
   
   
  
   
   # MAKE OBJECT OF THE TPMorder CLASS
  my @result = (); 
  push(@result,"QUERY\tORDER\tCHARACTER COUNT");


# MAKE OBJECT OF THE TPMorder CLASS
my $tpm_1 = TPMorder->new();

# PROCESS MULTIPLE FASTA FILE IN TO HASH
my $seq_hash = $tpm_1->file_process($name);

my @threads=();
my @header=();
foreach my $header (keys %{$seq_hash})
{
	
	push(@threads,threads->new(\&sub1,$header));
	
		
	
}

my $i=0;

foreach my $myThread(@threads)
     {
         my $ReturnData = $myThread->join ;
         #print "@ReturnData\n";
		 push(@result,$ReturnData);
         $i++;
      }
print "Content-type: text/html\n\n";




print "<html>

<head>

<title>MC_CLUSTER</title>

<LINK href=\"../CSS/ser.css\" rel=\"stylesheet\" type=\"text/css\">

<script type=\"text/javascript\">
function eraseText() {
document.getElementById(\"reset\").value = \"\";
}
</script>

</head>

<body bgcolor = \"\#5F5353\">

<div align=\"center\">
  <table border =\"0\" width=\"75%\" height=\"1\" cellpadding=\"0\" frame=\"box\" cellspacing = 1>
    <tr bgcolor = \"\#EBEBCC\">
      <td width=\"75%\" height=\"1\" colspan=\"6\">
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <a href = \"../index.html\">  Home</a>&nbsp;&nbsp;&nbsp;&nbsp; <a href = \"../CONTACTS/contacts.html\"> Contact us</a></p>
      </td>
    </tr>
  <center>
    <tr>
      <td width=\"75%\" height=\"200\" colspan=\"6\"><img border=\"0\" src=\"../IMAGES/sh.jpeg\" width=\"100%\" height=\"100%\"></td>
    </tr>
    <tr bgcolor = \"\#CECBCB\" align = \"center\">
      <td width=\"328\" height=\"16\"></td>
      <td width=\"189\" height=\"16\"><a style=\"font-family: Times New Roman; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium\" href=\"../tools.htm\">HIV
        Subtyping</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
      <td width=\"90\" height=\"16\"><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \"></span><a href=\"\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Datasets</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;<span class=\"Apple-converted-space\">&nbsp;</span></span></td>
      <td width=\"99\" height=\"16\"><a href=\"\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Validation</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
      <td width=\"125\" height=\"16\"><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \"><span class=\"Apple-converted-space\">&nbsp;&nbsp;</span></span><a href=\"\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">References</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;<span class=\"Apple-converted-space\">&nbsp;</span></span></td>
      <td width=\"95\" height=\"16\"><a href=\"\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Examples</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
    </tr>
    <tr bgcolor =\"\#EBEBEB\" cellpadding = \"100\">
      <td width=\"75%\" height=\"495\" colspan=\"6\"  >
      ";
 

print "
<p>&nbsp;&nbsp;&nbsp;&nbsp;
<blockquote>
<font size = 5 face =\"cambria\" ><b>ORDER RESULTS :</b></font></p><br><br>
";

print "<table  align = center  cellpadding = 5 frame=box>";     
my @split_result=();
my $count = 1;
my $flag = 0;
 

foreach my $res (@result)
{
#print $res,"\n";
@split_result= split("\t",$res); 
#print "$split_result[0]";
	if($count == 1)
	{
		print "<tr align =center bgcolor = pink><th>$split_result[0]</th><th>$split_result[1]</th><th>$split_result[2]</th></tr>";
		$count=0;
	}
	elsif($flag==0)
	{
		print "<tr align =center bgcolor =#ECC87A><td>$split_result[0]</td><td>$split_result[1]</td><td>$split_result[2]</td></tr>";
		$flag=0;
	}
	elsif($flag==1)
	{
		print "<tr align =center ><td>$split_result[0]</td><td>$split_result[1]</td><td>$split_result[2]</td></tr>";
		$flag=1;
	}
@split_result=();
}

print "</table>";           


sub sub1
{

$tpm_1 = TPMorder->new();
$tpm_1->TPM_main(\${$seq_hash}{$_[0]},$_[0]);

}
 
 
    
     my $end = Benchmark->new();
     
   my $lag = timediff($st,$end);
 print "<br><br> &nbsp;&nbsp;&nbsp;&nbsp;";
 #print "Time Required for results is", timestr($lag);
          
print "  </td>
    </tr>
    <tr bgcolor = \"#FF9900\">
      <td width=\"75%\" height=\"19\" colspan=\"6\" align = \"center\">© Bioinformatics Centre, University of Pune, India</td>
    </tr>
    
  </table>
  <blockquote>
</div>

</body>

</html>
";

      
      
      
      
      
      
      
      
    