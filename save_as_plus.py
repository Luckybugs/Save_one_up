#! /usr/bin/env python
''''
a script to save the existing maya scene as a plus one version

'''
import re
import maya.cmds as cmds


#get the path of the current scene:

path_of_current_file = cmds.file(query=True, sceneName=True)
name_of_current_file = cmds.file(query=True, sceneName=True, shortName = True)
type_of_current_file = cmds.file(query=True, type = True)



# make new filename, path with regex and string methods
pattern = re.compile(r'[_.](\d*)\.')
match = re.search( pattern, name_of_current_file)
if match:
    verson_number = match.group(1)
    mach_pos = match.span()
    
    #up by one
    new_version_num = str(int(verson_number) + 1)

    #paded zeros to the right
    aj = new_version_num.rjust(len(verson_number), '0')

    foo = len(name_of_current_file)

    begin_path = path_of_current_file[:-foo]
    mid_path = name_of_current_file[:mach_pos[0]+1]
    end_path = aj + name_of_current_file[mach_pos[1]-1:]


    new_path = begin_path + mid_path + end_path

else:
	cmds.warning('No match found')
# Chek to see if the current scene has been saved on disk
# Query whether the file named "foo.mb" exists on disk

is_saved = cmds.file(path_of_current_file, query=True, exists=True)


# Chek to see if there is a file with the new name on disk
already_exists = cmds.file(new_path, query=True, exists=True)



# the save as part:

if is_saved and not already_exists:
    cmds.file(rename = new_path)
    cmds.file(save = True)
    cmds.warning('File saved as:', new_path)
else:
    cmds.warning('File not saved:', new_path)


