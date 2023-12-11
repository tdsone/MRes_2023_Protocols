# MResSSB_S5_Grp4

# Ni-NTA purification + ELISA for Polizzi group

Following protocols provided by the Polizzi group (from Andre Ohara), this script purifies 16 centrifuged P.pastoris 1 mL cultures, then performs an ELISA to determine protein of interest concentration. Supernatants from cultures are extracted, then their pH corrected to allow purification. The samples are then purified through His-tagged protein purification using Ni-NTA magnetic agarose beads. The purified samples are serially diluted (2-fold to 32-fold), then an ELISA is conducted producing samples that are ready for analysis by a plate reader.

In this ReadMe: deck set up, protocol overview, problems overcome, problems remaining.

## Deck set up:
- Left pipette: P300 Multi Gen 2
- Slot 1: USA Scientific 12 well reservoir (22 mL) containing reagents:
  - A1: 6.5 mL 2 M NaOH
  - A2: 20 mL Ni-NTA equilibration buffer (50 mM NaPO4, 300 mM NaCl, 20 mM imidazole, pH 7.4)
  - A3: 1 mL Pierce Ni-NTA agarose magnetic bead slurry
  - A4: 20 mL Ni-NTA wash buffer (50 mM NaPO4, 300 NaCl, 40 mM imidazole, pH 7.4)
  - A5: 3.5 mL Ni-NTA elution buffer (50 mM NaPO4, 300 mM NaCl, 300 mM imidazole, pH 7.4)
  - A6: 8 mL ELISA coating solution (50 mM Na2CO3)
  - A7: 20 mL ELISA blocking buffer (PBS-T, 5% non-fat dry milk)
  - A8: 22 mL ELISA PBS-T (Phosphate buffered saline-0.05% Tween 20 solution)
  - A9: 10 mL ELISA primary antibody (Anti-His-tag Mouse)
  - A10: 10 mL ELISA conjugated secondary antibody (Anti-Mouse)
  - A11: 10 mL ELISA PnPP (conjugated secondary antibody substrate)
- Slot 2: Corning 96 deep well plate (360 µL) of 1 mL cultures, 16 samples in columns 1 & 2
- Slot 3: Thermo Fisher 96 well plate (400 µL)
- Slot 4: Magnetic module with Opentrons 96 flat bottom adapter and Thermo Fisher 96 well plate (400 µL)
- Slot 5: P300 pipette tips
- Slot 6: P300 pipette tips
- Slot 7: P300 pipette tips
- Slot 8: N/A
- Slot 9: P300 pipette tips
- Slot 10: P300 pipette tips
- Slot 11: USA Scientific 12 well reservoir (22 mL) for waste liquids
  - A1-7: waste liquids
  - A8-11: 22 mL ELISA PBS-T (Phosphate buffered saline-0.05% Tween 20 solution)

## Protocol overview (16 samples): 
Raw sample preparation:
  1. 800 µL supernatant is extracted from 1 mL centrifuged cultures (slot 2 cols 1&2)
  2. Add 80 µL NaOH, wait 1 hour for salts to settle
  3. Extract 600 µL neutralised supernatant for purification (leaves 280 µL in slot 2 cols 3&4 for reserve)

Ni-NTA magnetic bead purification:
  1. Equilibrate 1 mL of Ni-NTA magnetic beads
  2. Add 30 µL beads to 300 µL supernatant (two replicates per sample, slot 4 sample 1-8 cols 2&3, sample 9-16 cols 4&5)
  3. Wash twice with 300 µL wash buffer
  4. Add 100 µL elution buffer, combine replicates (total 200 µL per sample), elute (total 200 µL slot 2 sample 1-8 col 11, sample 9-16 col 12)

ELISA:
  1. Uses 100 µL purified samples, leaving 100 µL for reserve (slot 2 sample 1-8 col 11, sample 9-16 col 12)
  2. Serially dilute 100 µL samples with coating solution 2x to 32x (slot 3 sample 1-8 cols 1-6, sample 9-16 cols 7-12), pause 2 hours
  4. Add 200 µL blocking buffer, pause 1 hour, wash 3 times with PBS-T
  5. Add 100 µL primary antibody, pause for 1 hour, wash 3 times with PBS-T
  6. Add 100 µL conjugated secondary antibody, pause for 1 hour, wash 3 times for 5 minutes with PBS-T
  7. Add 100 µL PnPP conjugated antibody substrate, mix, pause for 15 minutes for colour to develop
  8. Add 50 µL NaOH to stop reaction
  9. Measure absorbance at 405 nm in plate reader (slot 3 sample 1-8 cols 1-6, sample 9-16 cols 7-12, starting with 2x dilution to 32x)
  10. Use data from previously ran standards to determine protein of interest concentration in the samples

## Problems overcome:
- Can’t fit deep well onto magnet – had to divide samples into 2x 300 µL.
-	Avoid centrifuged pellet / beads when pipetting – changed z value.
-	Liquid uptake not uniform – increased all z values, may not remove all liquid?
-	Magnet too strong, affects bead binding / elution – transferred off magnet for these steps.
-	ELISA wash 5 min agitating – mixed lots instead.
-	Waste liquid - function to avoid overflowing, pipette dispenses over top to avoid contamination.
-	Large volume of PBS - function to determine which well to use.

## Problems remaining:
- Shaking steps (no shaker module, had manually move to shaker) – removed these.
-	Invert plate & tap to remove excess liquid – removed these.
-	Not reproducible – volumes should be assigned variables and calculated in the script.
-	Scale limited by deck space / tips – could split into two scripts (purification + ELISA).
-	Tip use – could improve by reusing same tips for washes.
-	ELISA standards not included to accommodate all 16 samples – uses data from previous run. If not limited by number of plate wells / deck space, it would be better to run standard alongside.
