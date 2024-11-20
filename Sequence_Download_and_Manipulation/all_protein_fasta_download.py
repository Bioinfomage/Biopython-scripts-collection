# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:17:22 2024

@author: kanmani
"""

import requests

# UniProt REST API endpoint for downloading sequences
uniprot_url = "https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta"

# Parameters for the query
params = {
    "query": "organism:10090",  # NCBI Taxonomy ID for Mus musculus (mouse)
    "format": "fasta",           # Output format (FASTA)
    "size": "500"                # Number of entries to download per request (up to 500 is typical for iterative download)
}

# Download all mouse proteins
response = requests.get(uniprot_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the FASTA data to a file
    with open("mouse_proteins.fasta", "w") as fasta_file:
        fasta_file.write(response.text)
    print("Download completed and saved as 'mouse_proteins.fasta'.")
else:
    print(f"Failed to download data. Status code: {response.status_code}")
