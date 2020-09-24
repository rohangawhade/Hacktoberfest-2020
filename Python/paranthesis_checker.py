open_paranthesis = ["[","{","("] 
close_paranthesis = ["]","}",")"] 

# Function to check parentheses 
def check(myStr): 
	result = [] 
	for i in myStr: 
		if i in open_paranthesis: 
			result.append(i) 
		elif i in close_paranthesis: 
			pos = close_paranthesis.index(i) 
			if ((len(result) > 0) and (open_paranthesis[pos] == result[len(result)-1])): 
				result.pop() 
			else: 
				return "Unbalanced"
	if len(result) == 0: 
		return "Balanced"
	else: 
		return "Unbalanced"


string = "[{(({}{}[]))}]"
print(string,"-", check(string)) 

string = "[{})]"
print(string,"-", check(string))


# Output:

# [{(({}{}[]))}] - Balanced
# [{})] - Imbalanced
