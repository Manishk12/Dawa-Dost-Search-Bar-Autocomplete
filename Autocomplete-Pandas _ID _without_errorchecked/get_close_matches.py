from difflib import get_close_matches
  
def closeMatches(patterns, word):
     print(get_close_matches(word, patterns))
  
# Driver program
if __name__ == "__main__":
    word = 'mcolen'
    patterns = ['ape', 'apple', 'peach', 'puppy']
    medi = ['Ramiday', 'Cevicitt50mgtablett', 'Siquil', 'Rindopril', 'Mirise']
    medis =['lacoptal', 'ozenin', 'wodrone', 'leksobrain', 'etori', 'iniflox', 'mupinase', 'cialis', 'duloxee', 'neurotic', 'proloc-d', 'zadimac', 'pantorite', 'linzomust', 
'swich', 'pizicef', 'prosafe', 'mecolin', 'aspenta', 'ticmoxy', 'matce', 'rabitis', 'olmelive', 'lomofar', 'ofmod', 'rabogest-dsr', 'esomi', 'gedopan', 'eventin', 'cloxy', 'aloclin', 'nurocap', 'jubiglim', 'imoxil', 'menomune', 'norbactin', 'rapitry', 'toprazol-d', 'lokpam', 'rypsin', 'bm', 'neuroage', 'triclotross', 'refexine', 'doliza', 'zorpex', 'befotrik']
    closeMatches(medis,word)