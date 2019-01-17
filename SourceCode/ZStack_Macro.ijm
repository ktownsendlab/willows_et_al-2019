////////////////////////////////////////
// Townsend Arborization ImageJ Macro //
////////////////////////////////////////

// Get file list from the arguments
filelist = getArgument();
file = split(filelist, ',');

// Open all the z positions for this tile
open(file [0]);
open(file [1]);
open(file [2]);
open(file [3]);
open(file [4]);
open(file [5]);
open(file [6]);
open(file [7]);
open(file [8]);
open(file [9]);
open(file [10]);
open(file [11]);
open(file [12]);
open(file [13]);
open(file [14]);
open(file [15]);
open(file [16]);
open(file [17]);
open(file [18]);
open(file [19]);
open(file [20]);

// Create a stack from the z positions, generate a ZMAX Projection, and save.
run("Images to Stack", "name=Stack title=[] use");
run("Z Project...", "projection=[Max Intensity]");
run("8-bit");
saveAs("Tiff", file[21]);
close();
run("Quit");
