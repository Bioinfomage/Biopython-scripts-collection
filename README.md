# Biopython-scripts-collection
## Overview

Welcome to the **Biopython Scripts Collection**! This repository contains a curated set of Python scripts that leverage the powerful [Biopython](https://biopython.org/) library for various bioinformatics tasks. Whether you're working on DNA/RNA/protein sequence analysis, database queries, BLAST, or file format conversion, you'll find a relevant script here.

## Features
- **Sequence Analysis**: Transcription, translation, ORF identification, GC content, and motif searches.
- **Restriction Analysis**: Simulates restriction enzyme cuts and calculates fragment properties.
- **Alignment and Phylogenetics**: Multiple sequence alignment, pairwise alignments, and phylogenetic tree handling.
- **Entrez Utilities**: Query NCBI databases for literature, nucleotide sequences, and metadata.
- **File Handling**: Convert between FASTA, GenBank, ABI, and other formats.
- **BLAST Integration**: Perform and parse local and online BLAST searches.
- **Parsing Tools**: Work with FASTA, GenBank, MSA, and Newick files.

## Scripts Included
### 1. **Sequence Analysis**
- `Analysing_dna_rna_pro.py`: DNA transcription, translation, and GC content analysis.
- `Dna_rna_protein_seq.py`: ORF extraction and six-frame translation.
- `Sequence_manipulation_methods.py`: Motif searches, slicing, and transformations.

### 2. **File Conversion**
- `fileconversion.biopy.py`: FASTA to two-line FASTA conversion.
- `filecov_biopyassignmnt.py`: ABI to FASTA format conversion.
- `Writing_fasta.py`: GenBank to FASTA format.
- `Writing_gb_files.py`: FASTA to GenBank format.

### 3. **BLAST and Alignment**
- `Local_BLAST.py`: Perform local BLAST and parse results.
- `Online_BLAST.py`: Run online BLAST against NCBI databases.
- `Parsing_BLAST_output.py`: Parse BLAST output summaries.

### 4. **Phylogenetics**
- `Parsing_MSA_files.py`: Handle multiple sequence alignment files.
- `Parsing_newickfile.py`: Parse and visualize Newick phylogenetic trees.

### 5. **Entrez Utilities**
- `egquery_biopython.py`: Query NCBI databases for metadata.
- `efetch_biopython.py`: Fetch nucleotide sequences from NCBI.
- `esearch_biopython.py`: Perform Entrez search and retrieve results.

### 6. **Parsing Tools**
- `Parsing_fasta_biopython.py`: Read and extract details from FASTA files.
- `Parsing_gb_biopy.py`: Extract CDS and annotations from GenBank files.

... and many more scripts in this collection!

## Requirements
- Python 3.6 or higher
- Biopython library (`pip install biopython`)

## Usage
Each script is standalone and can be executed independently. Ensure that the required input files are present in the specified paths and edit the script paths as needed.

```bash
python <script_name>.py
