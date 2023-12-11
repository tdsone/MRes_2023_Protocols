# Team 3 OpenTrons: Making randomised plates for GMOs

We took Noah Sprent's protocol for growing and monitoring the efficiency of carbon sequestering bacterial cells. The original protocol is fully automated using a Hamilton Robot, our objective was to extract key steps and demonstrate the OpenTrons 2's capabilities as a cheaper, more accessible substitute.

In this submission file you will find 5 python files. These scripts help you generate a randomised plate with growth medium and nutrients to measure cell growth and then a finak step to remove supernatant.

The steps and subsequent files are:

1. protocol-commented+fixed.py - prepares mastermix of solutions and randomises concerntrations into a 96 well plate
2. silicabeads.py - plates 200ul of silica beads in a 96 well plate
3. supernatant_aspirate_speed.py - aspirates supernatant after centrifuging silica beads

4. protocol-commented+fixed.py
   The protocol has been optmized for varying 2 components and 2 supplements i.e. 6 conditions. The control is the component without the supplement, components (C) ex: c1=glucose and c2=gluconate, supplements (S) ex: S1=vitamin A and S2=vitamin B, commponents are in mM and supplements mg/ml. The first step is making master mixes for each condition suing available stock in lab. Then we defined conditions, volumes and concentrations. We then calculate liquid handling to generate mastermixes for each condition.

5. silicabeads.py
   This file allows you to test the calibration of your opentrons machine. It will load 200ul of silica beads into the 96 well plate mimicking the cells that will be added prior to centrifuging.

6. supernatant_aspirate_speed.py
   This file allows for the supernatant removal. We ensured to add a slow aspiration speed and low Z value to ensure that the pellet of cells is not distrubed when aspirating hte supernatant.
