from opentrons import protocol_api

metadata = {
    'apiLevel': '2.15',
    'author': 'Hafsa Kaja Moinudeen',
    'protocolName': 'golden gate assembly of gRNA expression cassettes for CRISPR multiplexing',
    'source': 'Automated protocol from PMC9411621',
    'category': 'Synthetic Biology',
    'createdAt': '2023-12-08',
    'lastModified': '2023-12-08'
}
def generate_alphabet_string(n):
    # Generate a string of alphabets in uppercase depending on the input number
    # A = 1, AB = 2, ABC = 3, and so on
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet[:n]

# edit this before runs

num_of_arrays =  4 # number of subarrays you are running
# below wells can be in any order/ number, however if you are doing mutiple arrays, they should be symmetrical
activation_gRNA_wells = 'ABC'
repression_gRNA_wells = 'DEF'


def run(protocol: protocol_api.ProtocolContext):
    # Labware
    source_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    rxn_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', 5)
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', 6)
    thermal_cycler_module = protocol.load_module(module_name='thermocyclerModuleV2')  # Specify the correct labware and position
    thermal_cycler_plate = thermal_cycler_module.load_labware(name='nest_96_wellplate_100ul_pcr_full_skirt')

    temp_mod = protocol.load_module(module_name="temperature module gen2", location = 'D1')
    temp_plate = temp_mod.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap') 
    # this is where the cold stuff is going to go
    # Pipettes
    p20_single = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_1, tiprack_2])  # Changed to 'right'

    # generating gRNA fragments using PCR - 6 only
    # Set the temperature (e.g., 37 degrees Celsius)
    temp_mod.set_temperature(4)

    # Wait for the Temperature Module to reach the set temperature
    temp_mod.await_temperature(4)

    for j in range(1, num_of_arrays+1):
        # activation
        # add the activation master mix to the three primer-pairs containing wells (hand pippetted)
        # put it in the thermocycler for 5 cycles
        p20_single.pick_up_tip()
        for i in activation_gRNA_wells:
            p20_single.transfer(18, temp_plate['A6'], source_plate[f'{i}{j}'], new_tip='never')
        p20_single.drop_tip()

        # repression
        # add the activation master mix to the three primer/plasmid containing wells (hand pippetted)
        # put it in the thermocycler for 30 cycles
        p20_single.pick_up_tip()
        for i in repression_gRNA_wells:
            p20_single.transfer(18, temp_plate['B6'], source_plate[f'{i}{j}'], new_tip='never')
        p20_single.drop_tip()
        # after 25 cycles, open thermocycler and put the the activation gRNA in pcr plate in the thermocycler for an additional 5 cycles

        thermal_cycler_module.open_lid()
    for j in range(1, num_of_arrays+1):
        # addition of activation gRNA to the PCR plate
        for i in repression_gRNA_wells:
            p20_single.transfer(20, source_plate[f'{i}{j}'], thermal_cycler_plate[f'{i}{j}'])
    thermal_cycler_module.close_lid()

    # # Start the initial 25 cycles of the repression reaction
    # thermal_cycler_module.set_lid_temperature(105)  # Set the lid temperature, adjust as needed

    # # Initial denaturation step
    # thermal_cycler_module.set_block_temperature(98, hold_time_seconds=30)

    # # Cycling steps (25 cycles)
    # for _ in range(25):
    #     thermal_cycler_module.set_block_temperature(98, hold_time_seconds=10)
    #     thermal_cycler_module.set_block_temperature(57, hold_time_seconds=20)
    #     thermal_cycler_module.set_block_temperature(72, hold_time_seconds=30)
    
    # After 25 cycles, open the lid for manual addition of activation gRNA
    thermal_cycler_module.open_lid()

    for j in range(1,  num_of_arrays+1):
        # addition of activation gRNA to the PCR plate
        for i in activation_gRNA_wells:
            p20_single.transfer(20, source_plate[f'{i}{j}'], thermal_cycler_plate[f'{i}{j}'])
        # Close the lid to continue with the remaining 5 cycles
    thermal_cycler_module.close_lid()

    # # Additional denaturation step before the final 5 cycles
    # thermal_cycler_module.set_block_temperature(98, hold_time_seconds=30)

    # # Final 5 cycles with different temperature settings
    # for _ in range(5):
    #     thermal_cycler_module.set_block_temperature(98, hold_time_seconds=10)
    #     thermal_cycler_module.set_block_temperature(61, hold_time_seconds=20)
    #     thermal_cycler_module.set_block_temperature(72, hold_time_seconds=30)

    # # Final denaturation step
    # thermal_cycler_module.set_block_temperature(98, hold_time_seconds=30)

    # # Hold at 10 °C
    # thermal_cycler_module.set_block_temperature(10, hold_time_minutes=10)  # 0 seconds means hold indefinitely

    # # Open the lid at the end
    # thermal_cycler_module.open_lid()

    # Insert a pause
    protocol.pause('Protocol paused. Please resume after manual steps are completed. PCR purification using gel')

    # golden gate assembly
    # input - we have the purified fragments in col 6-9 A to F  
    # CRISPR vector or subarray
    thermal_cycler_module.open_lid()

    for j in range(6, num_of_arrays+6):
        for i in activation_gRNA_wells + repression_gRNA_wells:
            p20_single.transfer(1, source_plate[f'{i}{j}'], thermal_cycler_plate[f'A{j}'])
            
    # total volume of reaction must be twenty
    volume_for_gg_1 = 20 - len(activation_gRNA_wells + repression_gRNA_wells)
        
    # transfer master mix from C1, C2, C3, and C4 to the thermal cycler_plate directly 

    for j in range(6, num_of_arrays+6): 
        tar = j-5
        p20_single.transfer(volume_for_gg_1, temp_plate[f'C{tar}'], thermal_cycler_plate[f'A{j}'])

    thermal_cycler_module.close_lid()

    # # Set the thermal cycling parameters
    # thermal_cycler_module.set_lid_temperature(105)  # Set the lid temperature, adjust as needed

    # # Run the thermal cycling program
    # # (37 °C for 5 min, 16 °C for 5 min) x 30 cycles
    # for _ in range(30):
    #     thermal_cycler_module.set_block_temperature(37, hold_time_minutes=5)
    #     thermal_cycler_module.set_block_temperature(16, hold_time_minutes=5)

    # # Final digestion step at 55 °C for 10 min
    # thermal_cycler_module.set_block_temperature(55, hold_time_minutes=10)

    # # Heat inactivation at 80 °C for 10 min
    # thermal_cycler_module.set_block_temperature(80, hold_time_minutes=10) 

    # # Hold at 10 °C
    # thermal_cycler_module.set_block_temperature(10, hold_time_minutes=10) 

    # open the lid
    thermal_cycler_module.open_lid()

    protocol.pause('Protocol paused. Please resume after manual steps are completed. Transformation, select colonies, and miniprep')


    # final golden gate assembly

    # wells containing the subarrays 
    subarray_wells = generate_alphabet_string(num_of_arrays)

    # final assembly
    thermal_cycler_module.open_lid()
    # transfer all subarrays to the thermal cycler
    for i in subarray_wells:
        p20_single.transfer(1, source_plate[f'{i}11'], thermal_cycler_plate['A11'])

    # total volume of reaction must be twenty
    volume_for_gg_2 = 10 - num_of_arrays
    
    # transfer mastermix D6
    p20_single.transfer(volume_for_gg_2, temp_plate['D6'], thermal_cycler_plate['A11'])   
    thermal_cycler_module.close_lid()

    # # Set the thermal cycling parameters
    # thermal_cycler_module.set_lid_temperature(105)  # Set the lid temperature, adjust as needed

    # # Run the thermal cycling program
    # # (42 °C for 2 min, 16 °C for 5 min) x 25 cycles
    # for _ in range(25):
    #     thermal_cycler_module.set_block_temperature(42, hold_time_minutes=2)
    #     thermal_cycler_module.set_block_temperature(16, hold_time_minutes=5)

    # # Final digestion step at 55 °C for 10 min
    # thermal_cycler_module.set_block_temperature(55, hold_time_minutes=10)

    # # Heat inactivation at 80 °C for 10 min
    # thermal_cycler_module.set_block_temperature(80, hold_time_minutes=10)

    # # Hold at 10 °C
    # thermal_cycler_module.set_block_temperature(10, hold_time_minutes=10)  

    # Optionally, open the lid if your next step requires it
    thermal_cycler_module.open_lid()

    protocol.pause('Protocol complete. Team OT-5 are genius!!!')