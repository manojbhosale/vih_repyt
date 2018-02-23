package ord_sub;

use strict;



sub ord_1_combination
{
	
	
	my (@di_nuc)=();
	my %temp_hs=();
	my @atgc = ("A","T","C","G");
	my $assi_ind = 0;
   
		for(my $i = 0; $i < 4; $i++)
		{
				push(@di_nuc,$atgc[$i]);
				
				$assi_ind++;	
		}
	
	return \@di_nuc;
}

sub ord_2_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;

for(my $i = 0; $i < 4; $i++)
		{
			for(my $j = 0; $j < 4; $j++)
			{
				push(@di_nuc,$atgc[$i].$atgc[$j]);
				
				$assi_ind++;
			}
		}
		return \@di_nuc;
	
}

sub ord_3_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
for(my $i = 0; $i < 4; $i++)
	{
		for(my $j = 0; $j < 4; $j++)
		{
			for(my $k = 0; $k < 4; $k++)
			{
				push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k]);
				
				$assi_ind++;
			}
		}
	}
	return \@di_nuc;
	
}

sub ord_4_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
for(my $i = 0; $i < 4; $i++)
	{
		for(my $j = 0; $j < 4; $j++)
		{
			for(my $k = 0; $k < 4; $k++)
			{
			for(my $l = 0; $l < 4; $l++)
			{
			
				push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l]);
				
				$assi_ind++;
			
		        }
			}
		}
	}
	return \@di_nuc;
}


sub ord_5_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m]);
						
						$assi_ind++;
					}
				        }
					}
				}
	}
return \@di_nuc;
}

sub ord_6_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n]);
						
						$assi_ind++;
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}

sub ord_7_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o]);
						
						$assi_ind++;
						}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}

sub ord_8_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p]);
						
						$assi_ind++;
						
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}




sub ord_9_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
					for(my $q = 0; $q < 4; $q++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p].$atgc[$q]);
						
						$assi_ind++;
					}
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}



sub ord_10_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
					for(my $q = 0; $q < 4; $q++)
					{
					for(my $r = 0; $r < 4; $r++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p].$atgc[$q].$atgc[$r]);
						
						$assi_ind++;
					}
					}
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}



sub ord_11_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
					for(my $q = 0; $q < 4; $q++)
					{
					for(my $r = 0; $r < 4; $r++)
					{
					for(my $s = 0; $s < 4; $s++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p].$atgc[$q].$atgc[$r].$atgc[$s]);
						
						$assi_ind++;
					}
					}
					}
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}


sub ord_12_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
					for(my $q = 0; $q < 4; $q++)
					{
					for(my $r = 0; $r < 4; $r++)
					{
					for(my $s = 0; $s < 4; $s++)
					{
					for(my $t = 0; $t < 4; $t++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p].$atgc[$q].$atgc[$r].$atgc[$s].$atgc[$t]);
						
						$assi_ind++;
					}
					}
					}
					}
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}


sub ord_13_combination
{
		my (@di_nuc)=();
		my %temp_hs=();
		my @atgc = ("A","T","C","G");
		my $assi_ind = 0;
		
		for(my $i = 0; $i < 4; $i++)
			{
				for(my $j = 0; $j < 4; $j++)
				{
					for(my $k = 0; $k < 4; $k++)
					{
					for(my $l = 0; $l < 4; $l++)
					{
					for(my $m = 0; $m < 4; $m++)
					{
					for(my $n = 0; $n < 4; $n++)
					{
					for(my $o = 0; $o < 4; $o++)
					{
					for(my $p = 0; $p < 4; $p++)
					{
					for(my $q = 0; $q < 4; $q++)
					{
					for(my $r = 0; $r < 4; $r++)
					{
					for(my $s = 0; $s < 4; $s++)
					{
					for(my $t = 0; $t < 4; $t++)
					{
					for(my $u = 0; $u < 4; $u++)
					{
						push(@di_nuc,$atgc[$i].$atgc[$j].$atgc[$k].$atgc[$l].$atgc[$m].$atgc[$n].$atgc[$o].$atgc[$p].$atgc[$q].$atgc[$r].$atgc[$s].$atgc[$t].$atgc[$u]);
						
						$assi_ind++;
					}
					}
					}
					}
					}
					}
					}
					}
					}
				        }
					}
				}
	}
return \@di_nuc;
}



1;