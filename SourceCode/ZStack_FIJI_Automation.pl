#!/usr/bin/perl -w
#############################################
# Townsend Arborization Analysis PERL Script#
#############################################

# The purpose of this script is to run the ZStack Macro over all the tiles in your tiled z-stack

# Keep this section, it helps maintain good PERL code
use strict;
use warnings;

# Set the directory to where the single tile images are being stored
my $directory = "/Volumes/Carl_Friedrich_Gauss/HET3_Whole_Depot/Single_Tile_Tiffs/AF10_ch00/";

# Define the naming prefix associated with the images, ensure all your images use the same prefix
my $prefix = "HET3_AF10_17Dec18_JW_s";

# Define variables set at the lowest and highest number that the prefix will reach (i.e. the first and last tiles)
my $begin = 0;
my $end = 1113;

# For All Stacks:
my $i = $begin; 				# Sets the variable i to the first image
for ($i; $i <= $end; $i++){		# This for loop will cycle through all the images
	my $file;					# Creates a variable called 'file'
	# This section just ensures the numbering will be uniform and accurate (i.e. 1620 vs 0620 vs. 062 vs 006)
	# Currently set to four digits, remove one zero from lines 29 & 31, while making line 33 mirror line 35 if using three digits
	if ($i < 10){
		$file = "00"."$i";
	}elsif ($i <100) {
		$file = "0"."$i";
	}elsif ($i <1000) {
		$file = $i;
	}else{
		$file = $i;
	}
	# Opens FIJI and opens the Macro made for this analysis (Set up for Mac FIJI version)
	my $command = "/Applications/Fiji.app/Contents/MacOS/ImageJ-macosx --ij2 -macro ZStack_Macro.ijm ";
	# This for loop will pass each image in the image stack to the Macro
	for (my $z=0; $z<=21; $z++){
		my $slice = $z;
		if ($slice<10){$slice = "0$slice"}
		$command .= "${directory}${prefix}${file}_z${slice}_ch00.tif,"; # This is where the final naming structure of each file is determined
	}

# This section defines where to save the files that the macro creates and how to name them
# ZMAX Projection
$command .= "/Volumes/Big_Red/HET3_Whole_Depot/ZMAX_Projections/AF10_ch00/${file}_zmax.tif,";

# Run on the command line
print "\n$file\n";
print "$command\n";
system $command;
}
