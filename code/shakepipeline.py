import updatescript
import updatealias
import scriptanalysis
import edgemerge
import os

'''
The driver file that turns a set of scripts into a network.
'''

print("Here we go")


#mydir
data_dir = "/Users/abeverid/PycharmProjects/shake/data/"



# play
play = "merchantvenice"

#outdir
out_dir = "/Users/abeverid/PycharmProjects/shake/out/" + play + "/"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)


# currently support import of more than one alias file
alias_file_list = [
    data_dir + "alias/" + play + ".csv"
]

raw_script_file = data_dir + "plays/" + play +  ".txt"

# output files
out_file_prefix = out_dir + play

update_script_file = out_file_prefix + "-updated.txt"
alias_script_file = out_file_prefix + "-alias.txt"
edge_file_prefix = out_file_prefix + "-edge"
final_edge_file = edge_file_prefix + "-all.csv"

print("UPDATING")
updatescript.update(raw_script_file, update_script_file)

print("ALIASING")
updatealias.update(update_script_file, alias_script_file, alias_file_list)

print("ANALYZING")
edge_file_list = scriptanalysis.analyze(alias_script_file, alias_file_list, edge_file_prefix)

print("MERGING")
edgemerge.merge(edge_file_list, final_edge_file)

