package TPMorder;

use DISC::Discrete;
use ord_sub;
use strict;
use Storable;


################################################################
# 							       #
#  Name: Transition Probability Matrix[TPM] Calculation        #
#  Copyright: MSB Pvt.Ltd.				       #
#  Author: Manojkumar S. Bhosale			       #
#  Date: 03/02/11 17:54					       #
#  							       #
#							       #
#  Description: 					       #
#							       #
#	 METHODS in THE package				       #
#							       #
# 		new					       #
# 		file_process				       #
# 		TPM_main				       #
# 		distance_matrix				       #
# 		neighbor				       #
#							       #
################################################################

sub new
{
	
	my $self={};
	shift;
	$self->{"ATGC"} =["A","T","G","C"]; 
	
	bless($self);
	
	return $self;	
	
}

sub file_process
{
	my $self = shift;
	my $file_name = shift;
	$self->{"file_name"}=$file_name;	
	open IN,"$file_name" or die("\nFailed To Open The File \n$! !!!!!!!!!!!!!!\n");
		    	
			my $header=();
			while(<IN>)
			{
				chomp;
				
				if($_=~m/^>/)
				{
					$header = $_;
					#$header=~s/\s+//;$header=~s/>//;
					#$header = substr($header,0,10);
					#my $space = 10-length $header;
	
					#if($space != 0)
					#{
					#	for(my $i = 0; $i<$space ;$i++)
					#	{
					#		$header .=" " ;
					#	}
					#}
					
					$self->{"seq_hash"}->{$header};
					
				}
				elsif($_=~m/[ATGC]/g)
				{
						$self->{"seq_hash"}->{$header}.=$_;
				}
				else{}
		
			}
			
		return $self->{"seq_hash"};

} #END OF THE FILE PROCESS SUB
	
	
sub TPM_main
{
	my $self = shift;
	my $order = shift;
	$self->{"order"} = $order; 
	my %mono_nuc=();
	my $arr_ref=();
	
	if($order == 1)
	{
		$arr_ref = ord_sub->ord_1_combination();
	}
	elsif($order == 2)
	{
		$arr_ref = ord_sub->ord_2_combination();
	}
	elsif($order == 3)
	{
		$arr_ref = ord_sub->ord_3_combination();
	}
	elsif($order == 4)
	{
		$arr_ref = ord_sub->ord_4_combination();
	}
	elsif($order == 5)
	{
		$arr_ref = ord_sub->ord_5_combination();
	}
	elsif($order == 6)
	{
		$arr_ref = ord_sub->ord_6_combination();
	}
	elsif($order == 7)
	{
		$arr_ref = ord_sub->ord_7_combination();
	}
	elsif($order == 8)
	{
		$arr_ref = ord_sub->ord_8_combination();
	}
	
	$self->{"combi_array"} = $arr_ref; 
	
	my $assi_ind=0;
	for(my $i = 0; $i < 4; $i++)
		{
					$self->{"mono_nuc"}->{$self->{"ATGC"}[$i]}=$assi_ind;
					$assi_ind++;	
		}
		
		
		
		
		foreach my $header (keys %{$self->{"seq_hash"}})
		{
		
			for(my $i = 0;$i< scalar(@{$arr_ref});$i++)
			{
				colsum_row_sum($arr_ref,$self,\$header,$i,\$self->{"seq_hash"}->{$header});
			}

		}	


	return $self->{"test"};
} # END OF TPM_MAIN
 	
	
sub colsum_row_sum
{
	my $arr_ref = shift;
	my $self=shift;
	my $header =shift;
	my $di_num = shift;
	my $ref_file = shift;
	my (@temp_row,@TPMrow,@rowsum)=();
			
while ($$ref_file =~ m/(?=(${$arr_ref}[$di_num])(.))/g)
	{
 	                $temp_row[$self->{"mono_nuc"}->{$2}]++;
        }

	my $ind=0;	
	
foreach(@{$self->{"ATGC"}})
	{
		$rowsum[$di_num]+=$temp_row[$ind];
		$ind++;
	}	
	
	 $ind=0;	

foreach(@{$self->{"ATGC"}})
	{
		if($rowsum[$di_num] != 0)
		{
			$TPMrow[$ind]=$temp_row[$ind]/$rowsum[$di_num];	
		}
		else
		{
			$TPMrow[$ind]=0;
		}
			
			$ind++;
	}	
push(@{$self->{"test"}->{$$header}->{${$arr_ref}[$di_num]}},@TPMrow);

	@temp_row=();
	@TPMrow=();
	
} # colsum_rowsum subroutine ends here


sub distance_matrix
{
	
	my $self = shift;
	my $hashref = shift;
	my @mat_id = ();
	my $ke = keys %{$hashref};
	my @mat_id = keys %{$hashref};
	my @test_arr = keys %{$self->{"test"}};
		#print @test_arr,"\n";
		my @dist_data = ();
		my @sec_dist_arr=();
		my @select_dist =();
		my @result=();
my $k=0;
my $score =0;


my $sq_sub = ();
my $distance = 0;

#open OUT,">RESULT.txt";

my %hash_dist=();

#print OUT "QUERY SEQUENCE\tPREDICTED_SUBTYPE\tZ_SCORE\n"; 
push(@result,"QUERY SEQUENCE\tPREDICTED SUBTYPE");
for(my $j = 0 ; $j < scalar(@test_arr) ; $j++)
{
	for(my $i = 0 ; $i < scalar(@mat_id) ; $i++)
	{
	
		foreach(@{$self->{"combi_array"}})
		{
			for(my $l = 0 ; $l < 4 ; $l++ )
			{
				$sq_sub += (${${$hashref}{$mat_id[$i]}{$_}}[$l]-${$self->{"test"}->{$test_arr[$j]}->{$_}}[$l])**2;
			}
			
		}
		
		$distance = sqrt($sq_sub);
		
		$hash_dist{$mat_id[$i]}=$distance;
		push(@dist_data,$distance);
		#printf OUT "%.3f  ",$distance;
		$sq_sub=0;
		$distance=0;
		
	}
	
	
				
	
	
	foreach(sort {$hash_dist{$a} <=> $hash_dist{$b}} keys %hash_dist)
	{

		my @predicted_header = split(/\|/,$_);
		$predicted_header[0]=~s/>//g;
		$test_arr[$j]=~s/[>\n]//g;
		$predicted_header[0]=~s/[\s+\n]//g;

		@sec_dist_arr=map{$hash_dist{$_}}@select_dist=grep{$_=~m/^>$predicted_header[0]/}keys %hash_dist;

		my $stats = new DISC::Discrete;
		$stats->add_data(@sec_dist_arr);
		my $mean = $stats->mean();
		
		my @return_parameters = z_score_parameters($predicted_header[0]);
		
		if($hash_dist{$_} <= $return_parameters[2])
		{
		#print $return_parameters[3],"  mmmmmmmm\n";
		my $z_score = (($mean-$return_parameters[0])/($return_parameters[1]/sqrt($return_parameters[3])));
		#print "$predicted_header[0] :: ",$mean-$return_parameters[0],"\n";
		if($z_score <= 1.96  && $z_score >= -1.96)
		{
		
		#print OUT $split_test_head[2],"\t\t\t",$split_test_head[0],"\t\t\t",$predicted_header[0],"\t\t\t",$z_score,"\n";
		push(@result,$test_arr[$j]."\t".$predicted_header[0]."\t".$z_score);
		#print $mean,"---",$return_parameters[0],"\n",
		}
		else
		{
		#print OUT $split_test_head[2],"\t\t\t",$split_test_head[0],"\t\t\tNA","\t\t\t",$z_score,"\n";
		push(@result,$test_arr[$j]."\t".$predicted_header[0]."\t"."NA");
		}
		
		
		
		}
		else
		{
		
		#print OUT $split_test_head[2],"\t\t\t",$split_test_head[0],"\t\t\tNA","\t\t\tNA","\n";
		push(@result,$test_arr[$j]."\t."."NA"."\t"."NA");
		
		}
		
		
		#print OUT $split_test_head[2],"\t\t\t",$split_test_head[0],"\t\t\t",$predicted_header[0],"\t\t\t",$score,"\n";
		
		
		#print $split_test_head[2],"\n" if($split_test_head[0] == $predicted_header[0]);
		last;

	}
	%hash_dist=();
	@dist_data=();
	@sec_dist_arr=();
	@select_dist =();
}	
#close(OUT);	

return \@result;

}


sub z_score_parameters
{
my %mean=(
 A=>36.5191278786483,
 B=>35.0709783032266,
 C=>35.5170829363281,
 D=>36.9380667115412,
 G=>35.3400020909224,
 );
 my %std_dev=(
A=>4.3359769109101, 
B=>2.51984570059568, 
C=>1.86880900678546,
D=>2.42526573021522,
G=>1.69161920230059,
);

my %max=(
A=>41.761459215322,
B=>40.8954974231827, 
C=> 40.3783284121037, 
D=> 43.0071933588459, 
G=> 39.2492456759067,
 );

my %sqt_no=(
A=>7,
B=>8,
C=>8,
D=>8,
G=>8,
);


return $mean{$_[0]},$std_dev{$_[0]},$max{$_[0]},$sqt_no{$_[0]};
}

1;

=head
my %max=(
A=>40.761459215322 ,
B=>37.6081191920811 , 
C=> 36.3558597153803, 
D=> 42.0071933588459, 
G=> 38.0013635788336,
 );


