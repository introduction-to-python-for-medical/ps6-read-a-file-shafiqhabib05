def create_codon_dict(file_path):
  file = open(file_path)
  rows = file.readlines()
  file.close()
  my_dict = {}
  for row in rows:
     cells = row.strip().split('\t')
     codon = cells[0]
     amino_acid = cells[2]
     my_dict[codon] = amino_acid
  return my_dict


