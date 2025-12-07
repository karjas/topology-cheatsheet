import numpy as np
import json

import os

def read_file_to_json(fnam):

    with open(fnam) as f:
        data = {}
        text = ""
        key = None
        for i,l in enumerate(f):
            if i == 0:
                name = l.rstrip().replace("# ","")
                data["Name"] = name
                continue

            if "##" in l:
                if key != None:
                    data[key] = text
                key = l.replace("## ","").rstrip()
                text = ""
            else:
                text += l.rstrip()
        data[key] = text
    return data

def_pre = """---
layout: post
title: [title]
category: [category]
---"""

def generate_markdown(data_full, curr, citations_json, preamble = def_pre):
    data = data_full[curr]
    outf = def_pre
    outf = outf.replace("[title]",data["Name"])
    outf = outf.replace("[category]",data["category"])

    outf += "\n"
    text = data["Text"]
    text = text.replace("[equation]","\n\n$${}$$\n".format(data['Equation']))
    outf += text

    outf += """## Connected quantities
    
    | Quantity | connection |
    | --- | --- |
    """.replace("    ","")
    quants = data["Connected quantities"].split(",")
    for q in quants:
        outf += "| {} | ${}$ |".format(data_full[q]['Name'],data_full[q]["Equation"])

    outf += "\n"
    if data["Alternative symbols"] != "":
        outf += """
        ### Alternative symbols
        
        | Symbol | Work |
        | --- | --- |
        """.replace("    ","")
        alts = data['Alternative symbols'].split(";")
        for a in alts:
            symb, ref = a[1:-1].split(",")
            outf += "| {} | [{}] |".format(symb.rstrip(),ref.replace(" ", ""))

    if data["Citations"] != "":
        outf += """
        
        ### Citations
        """.replace("    ","")
        citations = data['Citations'].split(",")
        first_citation = np.array([outf.find(cit) for cit in citations])
        idx = np.argsort(first_citation)

        for i in idx:
            ii = i+1
            outf = outf.replace("[{}]".format(citations[i]),"[{}]".format(ii))
            cit = citations[i]
            outf += "[[{}] {}]({})".format(ii,citations_json[cit]['url'],citations_json[cit]['url'])
        
    return outf    

def write_pages(data,citations_json):
    for d in data:
        outf = data[d]["writefolder"] + d

        file_md = generate_markdown(data,d,citations_json=citations_json)

        print("writing to", outf)
        with open(outf,"w") as f:
            f.write(file_md)
    

if __name__ == "__main__":
    
    fold1 = "curvatures/"
    fold2 = "global_charges/"
    fold3 = "global_charges/"
    folds = [fold1,fold2,fold3]
    data = {}

    for fold in folds:
        for f in os.listdir(fold):
            if f[0] == ".":
                continue

            data[f] = read_file_to_json(fold + f)
            data[f]['folder'] = fold
            data[f]['category'] = fold.replace("/","")
            data[f]['writefolder'] = "../colls/_{}".format(fold)

    with open("references.json", 'r') as f:
        citations_json = json.load(f)

    write_pages(data,citations_json)

