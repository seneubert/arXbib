# arXbib
`arXbib` is a simple command line tool to generate [bibtex](http://www.bibtex.org/) entries from [arXiv](http://arxiv.org) identifiers. It allows automatic patching of bibtex bibliography files, checking for double entries.

```
> ./arXbib.py 1507.03414


%%% contains utf-8, see: http://inspirehep.net/info/faq/general#utf8
%%% add \usepackage[utf8]{inputenc} to your latex preamble

@article{Aaij:2015tga,
      author         = "Aaij, Roel and others",
      title          = "{Observation of J/ψp Resonances Consistent with
                        Pentaquark States in Λ$_b^0$ → J/ψK$^-$p Decays}",
      collaboration  = "LHCb",
      journal        = "Phys. Rev. Lett.",
      volume         = "115",
      year           = "2015",
      pages          = "072001",
      doi            = "10.1103/PhysRevLett.115.072001",
      eprint         = "1507.03414",
      archivePrefix  = "arXiv",
      primaryClass   = "hep-ex",
      reportNumber   = "CERN-PH-EP-2015-153, LHCB-PAPER-2015-029",
      SLACcitation   = "%%CITATION = ARXIV:1507.03414;%%"
}

```
`arXbib` uses the bibtex entries generated by [INSPIRE][inspire].

The full options can be viewed by doing
```
> ./arXbib.py
arXbib.py [-o <bibfile to patch>] [-k <new bibtex key> | -i] [-f] <arXiv ID>
```

* `-o <bibfile to patch>` a new entry will be appended to the bibfile. The script checks if the entry is already in the bibliography.
* `-k <new bibtex key>` allows to change the bibtex key from the default one.
* `-f` forces the entry to be written to the bibfile, even if duplicate entries are detected (the key has to be unique, though). 
* `-i` use the arXiv ID as bibtex key (instead of the default from [INSPIRE][inspire]

## Installation
Make a python3 environment by using [conda][conda]:
```
conda create --name py3 python=3.4
```
Activate the environment:
```
source activate py3
```
Install `arxbib`
```
pip install git+https://github.com/seneubert/arXbib.git
```
you are good to go.


## Dependencies
`arXbib` is written in Python3.4 and needs the [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) parser.

[inspire]:    https://inspirehep.net/
[conda]:      http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install
