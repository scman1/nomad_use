# Using NOMAD to annotate DFT files

- **Nomad tutorial**: The python files are examples directly from (NOMAD)[https://fairmat-nfdi.github.io/nomad-simulations/tutorials/standalone_schema_tutorial/] (ex_*.py). 
- **Orca Parse example**: There are other two python files which show how an orca example is parsed (run_nomad_parse.py and convert_to_json_ld.py). 
- **Jupyter Example**: The last file is a jupyter notebook that presents the same code as the orca parse example (nomad_use.ipynb)

---

## Setup
The file requirements.txt can be used to restore the files needed to run the examples and the notebook
```
python -m venv .venv

#Linux
source .venv/bin/activate
#Windows
.venv\Scripts\activate

pip install -r requirements.txt
```