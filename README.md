# willows_et_all-2020

Scripts related to Willows et all 2020 paper.

There were six scripts used in this analysis.

ZStack_FIJI_Automation.pl is a PERL script used to open FIJI on the command line and run a FIJI Macro over all z positions of a tile. The PERL script then cycles through all of the tiles in the tiled z-stack.

ZStack_Macro.ijm is a FIJI macro that the above PERL script runs over all z positions in a single tile. It creates a ZMAX Projection per tile.

Arborization_Initialization.mlx is a MATLAB Live Script that was used to determine the threshold values that would be used in filtering in the High Throughput script.

Arborization_High_Throughput.mlx is a MATLAB Live Script that was used to threshold, skeletonize, and quantify arborization of whole adipose depot.

MetaData2HeatMap.py is a Python script that takes metadata from a Leica TCS SP8 Confocal Microscope and the arborization values from the High_Throughput script. It uses the x and y coordinate of the tiles to produce a csv file with the arborization values in their associated tile (each cell of the csv is a tile) in the same geographic position as the full adipose depot.

HeatMap_Function.mlx is a MATLAB Live Script that was used to generate Heat Maps of the arborization value csv files produced by MetaData2HeatMap.
