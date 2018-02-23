#!c:\perl\bin\perl.exe
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);


my $cgi = new CGI;
my $text_file = $cgi->param('text_seq');
my $file = $cgi->param('file');
my $order = $cgi->param('order');




 system("perl delete.pl");

 my $name = (); 
 my @file_data=();
 my @time = `time`;
 $time[0]=~s/(.*is\:|\:|\.|\s|\/)/\_/g;
 my @date = `date`;
 $date[0]=~s/(.*is\:|\:|\.|\s|\-|\/)/\_/g;



my $temp_name= $file;

 if($file=~m/(\.txt|\.fasta)$/ig )
 {
	 $temp_name=~s/(\.txt|\.fasta)$//;
	  $temp_name=~s/\_/\-/g;

	$name = "INPUT_FILES/$temp_name$date[0]$time[0].fasta"; 
	
 	open(LOCAL, ">","$name") or carp $!; 
 	while(<$file>) { print LOCAL $_; } 
 }
 else
 {
 	open(LOCAL, ">","INPUT_FILES/text-area-file$date[0]$time[0].txt") or carp $!; 
 	print LOCAL $text_file;
 	$name="INPUT_FILES/text-area-file$date[0]$time[0].txt";
 }
 
 
 close(LOCAL);
 
 
 use strict;
   
   use TPMorder;
   use Date::Calc qw(Delta_YMDHMS);
   use Benchmark;
   my $st = Benchmark->new();
   
   
    my $tpm_2 = TPMorder->new();
     # PROCESS MULTIPLE FASTA FILE IN TO HASH
     
     my $seq_hash1 = $tpm_2->file_process($name);
     
    
     # CALCULATE TPM FOR GIVEN ORDER
     
     # my $order = 2;
     
     my $self_mod1 = $tpm_2->TPM_main($order);
     
     # DISTANCE MATRIX OF THE SEQUENCES
     
     my $dist_mat2 = $tpm_2->distance_matrix();
     
     # MAKING TREE FROM THE DISTANCE MATRIX GENERATED
     
     $tpm_2->neighbor();
   
     
       $name =~s/.*\\//g;
       $name=~s/\.txt//g;
       $name=~s/\.fasta//g;
       
       my $path = "$order--$name";
       
 
    my @files=glob("RESULTS/*.*");

$name=~s/INPUT\_FILES\///g;
     my $name_f="$order-outTREE-$name";


print "Content-type: text/html\n\n";

print "
<html>

<head>

<title>CLUSTER_RESULT</title>

<LINK href=\"../CSS/ser.css\" rel=\"stylesheet\" type=\"text/css\">

<script type=\"text/javascript\">
function eraseText() {
document.getElementById(\"reset\").value = \"\";
}
</script>

</head>

<body bgcolor = \"#5F5353\">

<div align=\"center\">
  <table border =\"0\" width=\"75%\" height=\"1\" cellpadding=\"0\" frame=\"box\">
    <tr bgcolor = \"#EBEBCC\">
      <td width=\"75%\" height=\"1\" colspan=\"6\">
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <a href = \"../index.html\">  Home</a>&nbsp;&nbsp;&nbsp;&nbsp; <a href = \"../CONTACTS/contacts.html\"> Contact us</a></p>
      </td>
    </tr>
  <center>
    <tr>
      <td width=\"75%\" height=\"200\" colspan=\"6\"><img border=\"0\" src=\"../IMAGES/sh.jpeg\" width=\"100%\" height=\"100%\"></td>
    </tr>
    <tr bgcolor = \"#CECBCB\" align = \"center\">
      <td width=\"328\" height=\"16\"></td>
      <td width=\"189\" height=\"16\"><a style=\"font-family: Times New Roman; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium\" href=\"../tools.htm\">
     Tools</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
      <td width=\"90\" height=\"16\"><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \"></span><a href=\"../DATASETS/dataset.html\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Datasets</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;<span class=\"Apple-converted-space\">&nbsp;</span></span></td>
      <td width=\"99\" height=\"16\"><a href=\"../VALIDATION/validation.html\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Validation</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
      <td width=\"125\" height=\"16\"><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \"><span class=\"Apple-converted-space\">&nbsp;&nbsp;</span></span><a href=\"../REFERENCES/references.html\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">References</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;<span class=\"Apple-converted-space\">&nbsp;</span></span></td>
      <td width=\"95\" height=\"16\"><a href=\"../EXAMPLES/examples.html\" style=\"font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; \">Example</a><span style=\"color: rgb(0, 0, 0); font-family: 'Times New Roman'; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-align: -webkit-right; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; font-size: medium; display: inline !important; float: none; \">&nbsp;</span></td>
    </tr>
    <tr bgcolor =\"#EBEBEB\" cellpadding = \"100\">
      <td width=\"75%\" height=\"495\" colspan=\"6\" vlign =\"center\" >

      ";

     
print "<blockquote>
<font size=\"5\" face = \"cambria\"><b>RESULTS OF PHYLOGENETIC TREE RECONSTRUCTION</b></font><br><br><br> <b>DOWNLOAD </b>FILE HERE  ";
   print "<a href = RESULTS/$order-outTREE-$name.dnd>$order-outTREE-$name</a><br><br>OR<br><br><font size = 4><b>View</b> Tree In Browser <br>Select layout from List :<br>
   <form name = tree_view action = phylo_svg.cgi>

<select name = \"view_type\">
  <option value = \"\">Rectangular</option>
  <option value = \"circular\">Polar Tree Layout</option>
</select>
 <input type=\"submit\" value=\"View\">

   </form><blockquote>
   ";
     
 
    
     my $end = Benchmark->new();
     
   my $lag = timediff($st,$end);
 
          
          
          
print "       
</td>  </tr>
          <tr bgcolor = #FF9900>
            <td width=946 colspan=6 align = center>� Bioinformatics Centre, University of Pune, India</td>
          </tr>
          
        </table>
        </center>
      </div>
      
      </body>
      
      </html>";

      
      
      
      
      
      
      
      
    