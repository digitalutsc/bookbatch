processing scripts for islandora ingests

bookbatch2.py - putting every page into a numbered folder, renaming the page to OBJ

r_v.py - reversing rectos and versos


metadata
1. metadata
2. open refine template
3. clean
4. xml_split

fix manuscripts reversing the page order. recto becomes verso, verso becomes recto. darn terminologies.

1. python r_v.py

bookbatch

1. https://github.com/digitalutsc/bookbatch
2. python bookbatch2.py
3. do a directory listing: ls -LR, find -L, tree confirm everything batched correctly
4. add to FTP
5. delete .DS_STORES

for dir in ./*;
do python bookbatch2.py $dir harleypy/{A..Z};
done
or
for dir in harley_original/*; do python bookbatch2.py $dir harleypy/$dir; done

use this command
for dir in harley_original/*; do python bookbatch2.py $dir harleypy_test/$dir; done


where does the book batch script go?

bookbatch2.py
harley_original
harleypy - dir doesn’t have to exist, will get created

harley_original/
├── menu1
   │   ├── 6-4-1_001.tif
   │   ├── 6-4-1_002.tif
   │   ├── 6-4-1_003.tif
├── menu2
   │   ├── 6-4-1_001.tif
   │   ├── 6-4-1_002.tif
   │   ├── 6-4-1_003.tif
├── menu3
   │   ├── 6-4-1_001.tif
   │   ├── 6-4-1_002.tif
   │   ├── 6-4-1_003.tif


will turn into
bookbatch2.py
harley_original
harleypy

harleypy/
|---harley_original/
   ├── menu1
      │   ├── 000
               ├── OBJ.tif
      │   ├── 001
               ├── OBJ.tif
      │   ├── 002
               ├── OBJ.tif
      │   ├── MODS.xml
etc…………...
