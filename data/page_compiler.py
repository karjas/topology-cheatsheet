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

    data['Text'], data["Connected quantities"] = extract_connected_quantities_from_text(data['Text'])
    data["Citations"] = extract_citations_from_text(data['Text'])
    data["Equations"] = extract_equations(data["Equations"])
    return data


def extract_connected_quantities_from_text(text):
    # Extracts all [eq_num,otherfile.md] combinations from text and cleans the equation numbers from text
    connections = re.findall(r'\[([A_Za-z0-9_,]+).md\]',text)
    connections = list(set(connections))

    conns = {}

    for c in connections:
        cs = c.split(",")
        if len(cs) == 1:
            idx = None
            conn = cs[0]
            conns[conn + ".md"] = None
        else:
            idx, conn = c.split(",")
            idx = int(idx)
            conns[conn + ".md"] = "equation{}".format(idx)
        text = text.replace("[{}.md]".format(c),"[{}.md]".format(conn))

    return text, conns

def extract_citations_from_text(text):
    citations = re.findall(r'\\cite\{([A_Za-z0-9_]+)\}',text)
    citations = list(set(citations))
    return citations
    
def extract_equations(equations):
    eqs = re.findall(r'\$(.*?)\$', equations)
    return {"equation{}".format(i + 1) : eqs[i] for i in range(len(eqs))}


class equation:

    def __init__(self, eq, left_hand = []):
        self.eq = eq
        self.lh = left_hand
        self.rh = []

    def __eq__(self, other):
        if type(other) is str:
            return self.eq == other
        
        if type(other) is type(self):
            return self.eq == other.eq

        print("Types not matching")
        return False

    def __add__(self, other):
        if type(other) == str:
            self.rh += [other]

        if type(other) == type(self):
            self.rh += other.rh
        return self

    @property
    def all_quantities(self):
        return [self.lh] + self.rh


def_pre = """---
layout: post
title: [title]
category: [category]
---"""

def generate_markdown(data_full, curr, citations_json, equations, preamble = def_pre):
    data = data_full[curr]
    outf = def_pre
    outf = outf.replace("[title]",data["Name"])
    outf = outf.replace("[category]",data["category"])

    outf += "\n"
    text = data["Text"]
    
    if len(data["Equations"]) == 1:
        for eq in data['Equations']:
            text = text.replace("[equation]","\n\n$${}$$\n\n".format(data['Equations'][eq]))
            text = text.replace("[equation1]","\n\n$${}$$\n\n".format(data['Equations'][eq]))
    else:
        for eq in data["Equations"]:
            text = text.replace("[{}]".format(eq), "\n\n$${}$$\n\n".format(data['Equations'][eq]))

    outf += text

    connected_quantities = data["Connected quantities"]

    if len(connected_quantities) > 0:
        
        connection_table = """
        
        ## Connected quantities
    
        | Quantity | connection |
        | --- | --- |
        """.replace("    ","")
        
        have_eqs = False

        for eq in Equations:
            connected_q = eq.all_quantities.copy()
            
            if curr in connected_q:
                connected_q.remove(curr)
                if len(connected_q) == 0:
                    continue
                connected_q = str(["[{}]".format(str(q)) for q in connected_q])[1:-1].replace("'","")
                connection_table += "| {} | $${}$$ |\n".format(connected_q,eq.eq)
                have_eqs = True
        
                
        quants = connected_quantities
        
        for q in quants:

            links = "[{}]".format(data_full[q]['Name']) + "({{ site.baseurl }}{% link " + "_{}/{}".format(data_full[q]["category"],q) + " %})"
            
            outf = outf.replace("[{}]".format(q),links)
            connection_table = connection_table.replace("[{}]".format(q),links)

        if have_eqs:
            outf += connection_table + "\n"

    
    if "Alternative symbols" in data.keys() and data["Alternative symbols"] != "":
        outf += """
        ### Alternative symbols
        
        | Symbol | Works |
        | --- | --- |
        """.replace("    ","")
        alts = data['Alternative symbols'].split(";")
        for a in alts:
            symb, ref = a[1:-1].split(",")
            outf += "| {} | {} |\n".format(symb.rstrip(),ref.replace(" ", ""))

    if len(data["Citations"]) > 0:
        citations = data["Citations"]
        outf += """
        
        ### Citations
        """.replace("    ","")
        first_citation = np.array([outf.find(cit) for cit in citations])
        idx = np.argsort(first_citation)

        for i_, i in enumerate(idx):
            ii = i_+1
            cit = citations[i].rstrip()
            cit_ = "\\cite{" + citations[i] + "}"
            outf = outf.replace(cit_,"[[{}]]({})".format(ii,citations_json[cit]['url']))
            outf += "[[{}] {}]({})".format(ii,citations_json[cit]['url'],citations_json[cit]['url'])
            outf += "\n\n"
    outf += "\n"
        
    return outf    

        

def write_pages(data,citations_json, equations):
    for d in data:
        outf = data[d]["writefolder"] + d

        file_md = generate_markdown(data, d, citations_json,equations)

        print("writing to", outf)
        with open(outf,"w") as f:
            f.write(file_md)
    

if __name__ == "__main__":

    pwd = os.getcwd() + "/data/"
    
    fold1 = "curvatures/"
    fold2 = "global_charges/"
    fold3 = "local_charges/"
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
    
    Equations = []
    
    for d in data:
        eqs = data[d]["Equations"] 
        for eqn in eqs:
            if eqs[eqn] == "todo":
                continue

            eqnew = equation(eqs[eqn], d)
            if eqnew not in Equations:
                Equations.append(eqnew)

    for d in data: 
        for conn in data[d]["Connected quantities"]:
            eqn = data[d]["Connected quantities"][conn]
            if eqn is None:
                continue
            eq = data[conn]["Equations"][eqn] 
            eqidx = Equations.index(eq)

            Equations[eqidx] += d




    with open(pwd + "references.json", 'r') as f:
        citations_json = json.load(f)
    """
    for d in data:
        for conn in data[d]["Connected quantities"]:            
            if d not in data[conn]["Connected quantities"].keys():
                eq1 = data[d]["Equations"][data[d]["Connected quantities"][conn]]
                if eq1 not in data[conn]["Equations"].values():
                    eqn = "equation{}".format(len(data[conn]["Equations"]) + 1)
   #                 data[conn]["Equations"][eqn] = eq1
                    data[conn]["Connected quantities"][d] = eqn
                
                else:
                    for eq2 in data[conn]["Equations"]:
                        if data[conn]["Equations"][eq2] == eq1:
                            data[conn]["Connected quantities"][d] = eq2
                            print("Equations already exist, Linking {} to {}".format(conn, d))

                                



    print(data["pbphase.md"]["Equations"])
    """

    write_pages(data,citations_json,Equations)
    
