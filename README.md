# DomainScreen
Screen Domain in ORFs

Requirement:

```
Biopython
```

Usage:

```
optional arguments:
  -h, --help            show this help message and exit

Required named args:
  -f FAA, --faa FAA     path to the Protein ORF seqs Input (default: None)
  -d DOMAIN, --domain DOMAIN
                        path to the domain list file (default: None)
  -o OUTPUT, --output OUTPUT
                        Folder of results (default: work)
```

Example usage:

```
python screen.py -f example/25.79.protein.faa -d example/domain_list -o work
```