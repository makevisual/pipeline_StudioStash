curStr = R"C:\test\mockProjects\RepoRetimeRoughKey"

# Get the drive letter
parts1 	= curStr.split(":\\")
p1 		= parts1[0]

# Get the Folder Name
parts2 	= curStr.split("\\")
p2 		= parts2[(len(parts2) - 1)]


print(curStr)
print(p1)
print(p2)
