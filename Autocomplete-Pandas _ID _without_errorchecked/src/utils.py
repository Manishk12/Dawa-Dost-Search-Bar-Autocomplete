import trie
import csv
import pandas as pd
word_list = []

full_name_root = trie.Node()
middle_name_root = trie.Node()
last_name_root = trie.Node()
fourth=trie.Node()
fifth=trie.Node()
sixth=trie.Node()
seventh=trie.Node()
eighth=trie.Node()


reader =  pd.read_csv('../data/medicines_all_freq_manish.csv')   
counter=0
id = {}
for li in range(0, 141047):
    full_name = ""
    w = reader['Combined_Name'][li].split()
    ##strip() to remove blank space after end of medicines Combined_Name ex "Paracetanal     " .  (know as done practical in Jupiyter Notebook)
    id[(reader['Combined_Name'][li]).strip()] = reader['id'][li]   
    #word_list.append(w)
    word_list.append(w)
    #print("Added : " + w[0] + "Index in list : " + str(counter))
    #first_name_root.add_word(w[0].lower(),index_in_list=counter)
    full_name += w[0].lower()
    if len(w) > 1:
        middle_name_root.add_word(w[1].lower(),index_in_list=counter)
        full_name += w[1].lower() 
    if len(w) > 2:
        last_name_root.add_word(w[2].lower(),index_in_list=counter)
        full_name += w[2].lower()
    if len(w) > 3:
        fourth.add_word(w[3].lower(),index_in_list=counter)
        full_name += w[3].lower()
    if len(w) > 4:
        fifth.add_word(w[4].lower(),index_in_list=counter)
        full_name += w[4].lower()
    if len(w) > 5:
        sixth.add_word(w[5].lower(),index_in_list=counter)
        full_name += w[5].lower() 
    if len(w) > 6:
        seventh.add_word(w[6].lower(),index_in_list=counter)
        full_name += w[6].lower()
    if len(w) > 7:
        eighth.add_word(w[7].lower(),index_in_list=counter)
        full_name += w[7].lower()                     
    full_name_root.add_word(full_name, index_in_list=counter)
    counter+=1
#def val (keyer):
#reade = csv.reader(open('../data/medicinesn1.csv', 'r'))
reade = pd.read_csv('../data/medicines_all_freq_manish.csv')
dcount= {}
derror= {}
for row in range(0,141047):

    #if k[0]=='P':
       #print(k," ")
    #dcount[k] = float(v)     #I changed
    dcount[(reade['Combined_Name'][row]).strip()] = reade['freq'][row]
    #print(dcount[k]," ")
    #return d[keyer]   
    derror[reade['first_name'][row].lower()]= (reade['Combined_Name'][row]).strip()
 

"""def make_comparator(less_than):
    def compare(x, y):
        if d[x]>d[y]:
            return -1
        elif d[x]<d[y]:
            return 1
        else:
            return 0
    return compare """
def getName(index):
    name = ""
    l = len(word_list[index])
    for i in range(0,l):
        name = name + " " + word_list[index][i]
    return name.strip()
    

def convert_into_list_of_dict(list_of_names):
    result=[]
    for word in list_of_names:
        #result.append({"name": word})
        result.append({"name": word, "ID": str(id[word])})         ##added by self
    return result

##I am adding here
from difflib import get_close_matches





def get_from_trie(root, query):
    index_list = root.auto_complete_word(query.lower())
    name_list = [getName(i) for i in index_list]
    dgrouped = {}



    if len(query)>8:    # >3,4,5,6....  ##control after how much length of string error check will occur ( errorchech reduces speed of search)
     errormatch = get_close_matches(query,[*derror],n=10) # fact: by default cutoff is 0.6
    #print([*derror])
     #print(errormatch)
     pri=1.0   #to take in account get_close function order also (sorted as per closesness, closest first)
     for e in errormatch:
        if(len(query)<=5):
            dgrouped[derror[e]]=dcount[derror[e]]*0.2*pri
        else:
            dgrouped[derror[e]]=dcount[derror[e]]*0.4*pri
        pri=pri-0.05
         #print(dgrouped[e])
    
    #errm = get_close_matches(query, [*dcount])
    #print(errm)
    #I added
    if(len(query)>2):
     substrmatched = [i for i in dcount if query in i.lower()] 
    #I added
     for q in substrmatched:
      #valu=float(dcount[q])
      #print(type(valu))
      #valu=valu*0.4
      #dgrouped[q]= str(valu)
      #print(dgrouped[q])
       if(len(query)<5):
        dgrouped[q]=dcount[q]*0.45          ## 0.4 is also very well as for len <5 it is double of errormatch (len<=5 ===> 0.2 * pri)
       else:
        dgrouped[q]=dcount[q]*0.8  

    #print(len(dgrouped))
    
    #print(dcount['Pantocid L Capsule SR'],"checked","   ")
    for nq in name_list:
      #print(nq," ")
      dgrouped[nq]=dcount[nq]
      #print(dgrouped[nq],"ttttttt")
    
      
    dix= sorted(dgrouped.items(), key=lambda x: x[1], reverse=True)
    dixo=[x[0] for x in dix]
    return dixo

    

def get_results(query):
    
    full_name_result = get_from_trie(full_name_root, query)
    middle_name_result = get_from_trie(middle_name_root, query)
    last_name_result = get_from_trie(last_name_root, query)
    fourth_result = get_from_trie(fourth, query)   # I edited from here
    fifth_result = get_from_trie(fifth, query)
    sixth_result = get_from_trie(sixth, query)
    seventh_result = get_from_trie(seventh, query)
    eighth_result = get_from_trie(eighth, query)
    final_result = full_name_result + middle_name_result + last_name_result + fourth_result + fifth_result + sixth_result + seventh_result + eighth_result
    return convert_into_list_of_dict(final_result)


def process_term(query):
    # If search term consists if spaces then 
    name_list = query.split(' ')
    result = ""
    for name in name_list:
        result = result + name.lower()
    return result

