# This file was generated using:
#    python -m iam_units.update emissions
# DO NOT ALTER THIS FILE MANUALLY!

import re

# All recognised emission species usable with convert_gwp(). See *pattern*.
SPECIES = [
    'C10F18',
    'C2F6',
    'C3F8',
    'C4F10',
    'C5F12',
    'C6F14',
    'CCl4',
    'CF4',
    'CFC11',
    'CFC113',
    'CFC114',
    'CFC115',
    'CFC12',
    'CFC13',
    'CH2Cl2',
    'CH3Br',
    'CH3CCl3',
    'CH3Cl',
    'CH4',
    'CHCl3',
    'HCFC123',
    'HCFC124',
    'HCFC141b',
    'HCFC142b',
    'HCFC21',
    'HCFC22',
    'HCFC225ca',
    'HCFC225cb',
    'HCFE235da2',
    'HFC125',
    'HFC134',
    'HFC134a',
    'HFC143',
    'HFC143a',
    'HFC152',
    'HFC152a',
    'HFC161',
    'HFC227ea',
    'HFC23',
    'HFC236cb',
    'HFC236ea',
    'HFC236fa',
    'HFC245ca',
    'HFC245fa',
    'HFC32',
    'HFC365mfc',
    'HFC41',
    'HFC4310mee',
    'HFE125',
    'HFE134',
    'HFE143a',
    'HFE227ea',
    'HFE236ca12',
    'HFE236ea2',
    'HFE236fa',
    'HFE245cb2',
    'HFE245fa1',
    'HFE245fa2',
    'HFE263fb2',
    'HFE329mcc2',
    'HFE338mcf2',
    'HFE338pcc13',
    'HFE347mcc3',
    'HFE347mcf2',
    'HFE347pcf2',
    'HFE356mec3',
    'HFE356pcc3',
    'HFE356pcf2',
    'HFE356pcf3',
    'HFE374pc2',
    'HFE4310pccc124',
    'HFE449sl',
    'HFE569sf2',
    'Halon1201',
    'Halon1211',
    'Halon1301',
    'Halon2402',
    'N2O',
    'NF3',
    'PFPMIE',
    'SF5CF3',
    'SF6',
    'cC3F6',
    'cC4F8',
    ]

# Regular expression for one *SPECIES* in a pint-compatible unit string.
pattern = re.compile('(?<=[ -])(' + '|'.join(SPECIES) + ')(?=[ -/]?)')
