package TPMorder;

use ord_sub;
use strict;

#package YourModule;
#require Exporter;
#@ISA = qw(Exporter);
#@EXPORT_OK = qw(file_process frobnicate);


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
	my %seq_hash=();
	open IN,"$file_name" or die("\nFailed To Open The File \n$! !!!!!!!!!!!!!!\n");
		    	
			my $header=();
			while(<IN>)
			{
				chomp;
				
				if($_=~m/^>/)
				{
					$header = $_;
					$header=~s/\s+//;$header=~s/>//;
					$header = substr($header,0,10);
					my $space = 10-length $header;
	
					if($space != 0)
					{
						for(my $i = 0; $i<$space ;$i++)
						{
							$header .=" " ;
						}
					}
					
					$seq_hash{$header}
					
				}
				elsif($_=~m/[ATGC]/g)
				{
				my $seq = $_;
				$seq=~s/\s+//;
						$seq_hash{$header}.=$seq;
				}
				else
				{}
		
			}
			
		return \%seq_hash;

} #END OF THE FILE PROCESS SUB
	
	
sub TPM_main
{
	my $self = shift;
	#my $order = shift;
	my $ref_seq_hash=shift;
	my $header = shift;
	my %mono_nuc=();
	my ($arr_ref,$grandtotal,$TestStatistics)=();
	my $ts=();
foreach(my $order = 1;$order<14;$order++)
{
	$self->{"order"} = $order; 
	#print $self->{"order"},"\n";
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
	elsif($order == 9)
	{
		$arr_ref = ord_sub->ord_9_combination();
	}
	elsif($order == 10)
	{
		$arr_ref = ord_sub->ord_10_combination();
	}
	elsif($order == 11)
	{
		$arr_ref = ord_sub->ord_11_combination();
	}
	elsif($order == 12)
	{
		$arr_ref = ord_sub->ord_12_combination();
	}
	elsif($order == 13)
	{
		$arr_ref = ord_sub->ord_13_combination();
	}
	
		
	my $assi_ind=0;
	
	for(my $i = 0; $i < scalar(@{$arr_ref}); $i++)
		{
					$self->{"mono_nuc"}->{${$arr_ref}[$i]}=$assi_ind;
					$assi_ind++;	
		}
		
		
		
		
		
		
		
		
			for(my $i = 0;$i< scalar(@{$arr_ref});$i++)
			{
				colsum_row_sum($arr_ref,$self,$i,\${$ref_seq_hash});
			}
			
			
			
			my $grandtotal_row =();
			for(my $i = 0;$i < scalar(@{$arr_ref});$i++)
			{					
					$grandtotal +=${$self->{"colsum"}}[$i];
			}
					
					
					#print "GRAND_T====$grandtotal\n";
					#print scalar(@{$arr_ref}),"\n" if($order == 6 );

					${$self->{"grand_total"}} = $grandtotal; 
					for(my $i = 0;$i< scalar(@{$arr_ref});$i++)
					{
						test_statistics($arr_ref,$self,$i,\${$ref_seq_hash});
					}
					
					$self->{"test_statistics"}*=2;
				
				 $ts = test_stat_values($order);
				
				if($self->{"test_statistics"}<=$ts)
				{
					#print "grT_COL ---> $grandtotal\n";
					#print "TEST_Stat ---> ",$self->{"test_statistics"},"\n\n";
					#print $order,"\t",length(${$ref_seq_hash})," \t\t", $self->{"test_statistics"} ,"\n\n";
					#print length($$ref_file)," \t\t\t," $self->{"test_statistics"} ,"\n\n";
					#$self->{"test_statistics"}=();
					#$self->{"grand_total"}=();
					#$self->{"colsum"}=();
					#$self->{"rowsum"}=();
					#$self->{"mono_nuc"}=();
					#$self->{"order"}=();
					last;
				 #return 1;
				}
				else
				{
				$self->{"test_statistics"}=();
				$self->{"grand_total"}=();
				$self->{"colsum"}=();
				$self->{"rowsum"}=();
				$self->{"mono_nuc"}=();
				$self->{"order"}=();
				  
				}

			
		
	}
		


	#return $self->{"order"};
	if($self->{"test_statistics"}<=$ts)
	{
	return $header."\t".$self->{"order"}."\t".length(${$ref_seq_hash})." \t\t". $self->{"test_statistics"} ."\n\n";
	}
	else
	{
	return $header."\tNOT FITTED FOR ANY ORDER !!!!!!";
	}
} # END OF TPM_MAIN
 	
	
sub colsum_row_sum
{
	my $arr_ref = shift;
	my $self=shift;
	
	my $di_num = shift;
	my $ref_file = shift;
	my (@temp_row,@TPMrow,@rowsum,@colsum)=();
	my $ord = $self->{"order"};
	
while ($$ref_file =~ m/(?=(${$arr_ref}[$di_num])(.))/g)
	{
 		my $wrd = $1.$2;
		$wrd=~s/.(.{$ord})/$1/g;
                $temp_row[$self->{"mono_nuc"}->{$wrd}]++;
               
	}

	my $ind=0;	
	
foreach(@{$arr_ref})
	{
		${$self->{"colsum"}}[$ind]+=$temp_row[$ind];
		${$self->{"rowsum"}}[$di_num]+=$temp_row[$ind];
		$ind++;
	}	

	@temp_row=();
	
} # colsum_rowsum subroutine ends here


sub test_statistics
{
	my $arr_ref = shift;
	my $self=shift;
	
	my $di_num = shift;
	my $ref_file = shift;
	my (@temp_row,@TPMrow,@rowsum,@colsum,$TestStatistics)=();
	my $ord = $self->{"order"};
	#print $ord,"\n";
while ($$ref_file =~ m/(?=(${$arr_ref}[$di_num])(.))/g)
	{
		my $wrd = $1.$2;
		$wrd=~s/.(.{$ord})/$1/g;
                $temp_row[$self->{"mono_nuc"}->{$wrd}]++;
	}

	my $ind=0;
	foreach(@{$arr_ref})
	{
		if($temp_row[$ind] != 0 )
		{

			my $num = $temp_row[$ind] * ${$self->{"grand_total"}};

			my $den= ${$self->{"rowsum"}}[$di_num] * ${$self->{"colsum"}}[$ind] ;
			if($den != 0)
			{
				my $temp2 = $num / $den;
				$temp2 = log($temp2);
				$self->{"test_statistics"}+= ($temp_row[$ind] * $temp2);
#print $temp_row[$ind]," \/ ",${$self->{"grand_total"}},"\n";
			}

		}
	$ind++;

	}
@temp_row=();
}

sub test_stat_values
{
	
	my %test_stat_val=(
		1=>21.666,
		2=>58.619,
		3=>188.469,
		4=>704.33,
		5=>2766.694,
		6=>11016.166,
		7=>44014.054,
		8=>176005.606,
		);
return $test_stat_val{$_[0]};	
}

1;
