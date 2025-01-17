#!/usr/bin/env python3

import yaml
import os
import arxiv

#get .bib for files with arXiv identifier
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)

    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='arxiv'):
                if not os.path.exists(f'./papers/{url}.txt'):
                    print('working on ArXiv file ' + url)
                    os.system("python ./scripts/arxiv2bib.py " + str(v) + " > papers/" + url +".txt")
                # also download paper?
                if not os.path.exists(f'./papers/{url}.pdf'):
                    paper = next(arxiv.Search(id_list=[str(v)]).results())
                    paper.download_pdf(dirpath="./papers", filename=f"{url}.pdf")

#get .bib for files with DOI 
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)
    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='doi'):
                print('working on DOI file ' + url)
                os.system("python ./scripts/doi2bib.py " + str(v) + " > papers/" + url +".txt")
                #remove empty lines that doi2bib gives
                open("papers/tmp.bib",'w').write(
                    ''.join(
                        l for l in open("papers/" + url + ".txt") if l.strip()))
                os.system("mv papers/tmp.bib papers/" + url + ".txt")
