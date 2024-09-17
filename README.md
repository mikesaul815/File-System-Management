This requires the following folders at the highest level "Input", "Archive" and "Error". 
Then there should be 5 folders called "TopLevel1" (with whatever number of folder it is), 
then "SubLevel2" (with whatever number of folder it is) 
and "SubSubLevel5" (with whatever number of folder it is). 

The files should live in "Input" and then when the script is run, it will move them to their respective folder if named appropriately. 
For example, a file named "TopLevel1-SubLevel2-SubSubLevel5.xlsx" will go to the folder TopLevel1\SubLevel2\SubSubLevel5, 
it will copy the file there and add a time stamp and user stamp to the file name. It will also move the file from the Input folder to the Archive folder. 

Key point, put a "-" between each layer of the hierarchy to ensure that they go to their correct path.
