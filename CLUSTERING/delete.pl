#code to delete files on timely basis;

use Date::Calc qw(Delta_YMDHMS);

my @files=glob("RESULTS/*");
my @infiles=glob("INPUT_FILES/*");

my @time = `time`;
 $time[0]=~s/(.*is\:|\:|\.|\s)/\_/g;
my @date = `date`;
 $date[0]=~s/(.*is\:|\:|\.|\s|\-)/\_/g;

$str1 ="ABC_$date[0]_$time[0]";

@st1=split(/\_+/,$str1);

push(@files,@infiles);


open(OUT, ">>log");

foreach(@files)
{
	chomp;
	$temp=$_;
	$str2 =$temp;
	$str2 =~s/RESULTS\///g;
	$str2 =~s/INPUT_FILES\///g;
	
	@st2=split(/\_+/,$str2);
	
	($D_y,$D_m,$D_d,$Dh,$Dm,$Ds) = Delta_YMDHMS($st1[3],$st1[2],$st1[1],$st1[4],$st1[5],$st1[6],$st2[3],$st2[2],$st2[1],$st2[4],$st2[5],$st2[6]);
	
	if(abs($D_d)>7)
	{
	
	    print OUT "$temp\n";
		unlink("$temp");	
	}

}