READ ME _ TEAM 2 _ CHERRY PICKER 

- Overview
    This code provides an accessible way to create custom cherrypicking protocols from a variety of different data sources provided
    that the data is in a 96 well plate list format.
- Features of Opentron script generator (code A)
  - able to specify your directory (/Users/Cassandra/Downloads)
  - able to specify the number of input CSV files (number of input plates) and names (sample_1.csv, sample_2.csv, sample_3.csv)
  - able to specify your column for sorting data (fluorescence, optical density etc.)
  - able to Specify source well column (Well, Well_Id, etc.)
  - able to Specify if there are any blanks in the input data and declare specific wells
  - optional to blank correct
  -   if no, remove blanks from the input data
  -   if yes, average blanks per plate and blank corrects data. removes blanks from the input data
  - able to sort data by min/max values or by a user-specified range (1000-1200)
  - able to choose the number of hits selected
  - able to choose how many duplicates you want in the destination plate
  - code tells user if the muber of destination wells exceeds 96 values
  - able to add blanks in the destination plate at user specified locations
  - able to create and name a fully customisable and opentron ready script.
  - easy to use interface that increases accessability of opentron codes.

After naming your new opentron cherrypicking script it will appear in your downloads ready to be uploaded into opentron directly.
 
- Featured of Opentron Script (Code B)
  - Using the inputs and data provided from Code A to create a ready to use opentron script
  - number of source hardware is determined by number of csv files submitted by user
  - protocol transfers 50ul of liquid from hit wells in the source 1500ul growth plates (number user defined)
    and consolidates them into one round bottom 1500ul 96-well plate with user user defined duplicates.
