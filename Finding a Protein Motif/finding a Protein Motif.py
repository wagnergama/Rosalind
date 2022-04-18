# Bibliotecas necessarias para o projeto
import urllib.request
from io import StringIO

with open('rosalind_mprt.txt') as f:
    for protein_name in f:
        line_written = False
        protein_url = 'http://www.uniprot.org/uniprot/' + protein_name.strip() + '.fasta'
        response = urllib.request.urlopen(protein_url)
        str_fasta = (response.read()).decode('UTF8')
        buff_fasta = StringIO(str_fasta)
        dict_fasta = {}
        id = None
        # Part 1: compile list of lines per sequence
        for linha in buff_fasta:
            if linha[0] == '>':
                dict_fasta[
                    protein_name.strip()] = []  ### poe o nome da proteina no dicionario como key e lista vazia como dados
            else:
                # Acrescenta nucleotideos na lista
                dict_fasta[protein_name.strip()].append(linha.rstrip())

        # Parte 2: Junta a lista em uma unica sequencia
        for id, nuc_list in dict_fasta.items():
            dict_fasta[id] = ''.join(nuc_list)

        s = dict_fasta[id]
        locations = ''
        for i in range(0, len(s)):
            # Verifica se a sequencia possui o motif N-glycosylation N{P}[ST]{P}.
            if (s[i] == 'N') and (s[i + 1] != 'P') and (s[i + 2] in ['S', 'T']) and (s[i + 3] != 'P'):
                locations += str(i + 1) + ' '

        if locations != '':
            print(protein_name.strip())
            print(locations.strip())
