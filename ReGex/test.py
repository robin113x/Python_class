import re
sentence = 'we are humans'
rexex = re.findall('\w[1,3]', sentence)
print(rexex)
