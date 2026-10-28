import json

# 1. Load your standard NOMAD parse output
with open("./outputs/orca_examples/16459/16459_nomad_orca.json", "r") as f:
    nomad_data = json.load(f)

# Extract core information from the NOMAD structure
run_block = nomad_data.get("run", [{}])[0]
calc_block = run_block.get("calculation", [{}])[-1]
system_block = run_block.get("system", [{}])[-1]

# 2. Build the JSON-LD structure mapping NOMAD to Semantic Vocabularies
json_ld_archive = {
    # Establish ontologies for both general metadata and chemical specifics
    "@context": {
        "@vocab": "https://schema.org",
        "chmo": "http://obolibrary.org",  # Chemical Methods Ontology
        "chebi": "http://obolibrary.org",  # Chemical Entities of Biological Interest
        "nomad": "https://nomad-lab.eu",
        "energy": "nomad:run/calculation/energy/total",
        "positions": "nomad:run/system/atoms/positions"
    },
    "@id": "https://doi.org",
    "@type": ["Dataset", "chmo:CHMO_0001402"],  # Dataset + Density Functional Theory Calculation type
    "name": "DFT Simulation of Molecular Catalyst Sample",
    
    # Inject your highly detailed custom sample definitions natively into the schema
    "about": {
        "@type": "chebi:CHEBI_23367",  # Molecular entity identifier
        "name": "Iron-based Coordination Catalyst",
        "description": "Fe(II) complex with a tetradentate nitrogen-donor macrocyclic ligand.",
        "chemicalFormula": "C20H24FeN4",
        "additionalType": "https://example.org"
    },
    
    # Map the standardized calculations exported by NOMAD
    "variableMeasured": [
        {
            "@type": "PropertyValue",
            "name": "Total Electronic Energy",
            "propertyID": "energy",
            "value": calc_block.get("energy", {}).get("total", {}).get("value"),
            "unitText": "eV"
        },
        {
            "@type": "PropertyValue",
            "name": "Atomic Positions",
            "propertyID": "positions",
            "value": system_block.get("atoms", {}).get("positions")
        }
    ],
    
    # Preserve provenance software markers
    "creator": {
        "@type": "SoftwareApplication",
        "name": run_block.get("program", {}).get("name"),
        "softwareVersion": run_block.get("program", {}).get("version")
    }
}

# 3. Save as a dedicated .jsonld file
with open("./outputs/orca_examples/16459_nomad_orca.jsonld", "w") as f:
    json.dump(json_ld_archive, f, indent=2)
