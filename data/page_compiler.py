import numpy as np
import json
import re

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
                if key == "Text":
                    text += l
                else:
                    text += l.rstrip()
        data[key] = text
    data["Connected quantities"] = extract_connected_quantities_from_text(data['Text'])
    return data

def extract_connected_quantities_from_text(text):
    connections = re.findall(r'\[([A_Za-z0-9_]+).md\]',text)
    return [c + ".md" for c in connections]

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
    text = text.replace("[equation]","\n\n$${}$$\n\n".format(data['Equation']))
    outf += text

    connected_quantities = data["Connected quantities"]

    if len(connected_quantities) > 0:
        outf += """
        
        ## Connected quantities
    
        | Quantity | connection |
        | --- | --- |
        """.replace("    ","")
        quants = connected_quantities
        for q in quants:

            links = "[{}]".format(data_full[q]['Name']) + "({{ site.baseurl }}{% link " + "_{}/{}".format(data_full[q]["category"],q) + " %})"
            outf += "| [{}] | $${}$$ |\n".format(q,data_full[q]["Equation"])
            outf = outf.replace("[{}]".format(q),links)

    outf += "\n"
    if "Alternative symbols" in data.keys() and data["Alternative symbols"] != "":
        outf += """
        ### Alternative symbols
        
        | Symbol | Works |
        | --- | --- |
        """.replace("    ","")
        alts = data['Alternative symbols'].split(";")
        for a in alts:
            symb, ref = a[1:-1].split(",")
            outf += "| {} | [{}] |\n".format(symb.rstrip(),ref.replace(" ", ""))

    if data["Citations"] != "":
        outf += """
        
        ### Citations
        """.replace("    ","")
        citations = data['Citations'].split(",")
        first_citation = np.array([outf.find(cit) for cit in citations])
        idx = np.argsort(first_citation)

        for i in idx:
            ii = i+1
            cit = citations[i].rstrip()
            outf = outf.replace("[{}]".format(citations[i]),"[[{}]]({})".format(ii,citations_json[cit]['url']))
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

    pwd = os.getcwd() + "/data/"
    
    fold1 = "curvatures/"
    fold2 = "global_charges/"
    fold3 = "global_charges/"
    folds = [fold1,fold2,fold3]
    data = {}

    for fold in folds:
        fold_target = pwd.replace("/data/","/colls/_") + fold
        for f in os.listdir(fold_target):
            # Cleans target directories
            os.remove(fold_target + f)
        
        for f in os.listdir(pwd + fold):
            if f[0] == ".":
                continue

            data[f] = read_file_to_json(pwd + fold + f)
            data[f]['folder'] = pwd + fold
            data[f]['category'] = fold.replace("/","")
            data[f]['writefolder'] = fold_target


    with open(pwd + "references.json", 'r') as f:
        citations_json = json.load(f)

    for d in data:
        for conn in data[d]["Connected quantities"]:
            if d not in data[conn]["Connected quantities"]:
                data[conn]["Connected quantities"].append(d)


    write_pages(data,citations_json)

