#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? 
# eg:- values can be integer or string and expressions will be mathematical operators.

# * : This is the muliplication operator
# 'hello' : This is a string data
# -87.8 : This is a negative float data
# - : This is the subtraction operator
# / : This is the division operator
# + : This is the addition operator
# 6 : This is an integer

# In[ ]:





# 2. What is the difference between string and variable?

# A variable is a named location in the memory which holds a value as the data. Whereas, a string is a type of data which consists of characters form A-Z and is always represented inside "" or ''

# 

# 3. Describe three different data types.

# String: A string is data type which can have "A-Z" characters. It has to be represented inside a "" or '' to be considered as a strign value. The .str() method can convert other data types into string so that operations can be performed between similiar data types. 
# 
# Boolean: A boolean is a data type which can have one of the outputs either TRUE or False. The in function is based on the same boolean logic. A number except 0 is always represented as True and it is it is 0 then, False. Similiarly, whitespaces are considered as False, while other values are considered as True.
# 
# Integer: An integer is a numercial value or a whole number without a decimal point. The int() function is used to convert a data type into an integer so  that operations can be performed on it.
# 
# Float: A float is a numerical value which has a decimal point.

# In[ ]:





# 4. What is an expression made up of? What do all expressions do?

# An expression is a combination of different operators, values and operands which when evaluated gives a single value.
# Ex: 3+5*4 : This is a combination of values and the answer is 23

# In[ ]:





# 5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?

# The basic difference b/w a statement and an expression is that a statement is a line of code that performs a specific function or operation. Whereas, an expression is a combination of variables, operators, operands, etc which evalutes to a single value.
# 
# Ex: statement = "Hello!" #This is an assignment statement
# x = 3 + 4   # Here, the expression '3 + 4' evaluates to the value 7, which is then assigned to the variable x.

# In[ ]:





# After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# The variable bacon will contain the value 23. This happens because the operator adds 1 to the value of the variable "bacon" which is 22, so 22+1 = 23

# In[ ]:





# What should the values of the following two terms be?
# 'spam' + 'spamspam' and
# 'spam' * 3

# In[11]:


'spam' + 'spamspam'


# The value returns as 'spamspamspam' because it is the result of concatenation of 2 strings with the operator + in between. So it adds two similiar data types with one another and produces the result as shown above

# In[10]:


'spam' * 3


# The result is the same because here, the string 'spam' is multiplied by itself 3 times. In a way, it means spam * spam * spam which reults in 'spamspamspam'

# In[ ]:





# 8. Why is eggs a valid variable name while 100 is invalid?

# eggs is a valid variable because a variable can contain letters A-Z or a-z, _ and numeric values. However, 100 is not a valid variable name as it cannot start with a numeric value or contain a space or special character like @#$&,etc
# 

# In[ ]:





# 9. What three functions can be used to get the integer, floating-point number, or string
# version of a value?

# There are functions in python which can help you to convert a data type from a specific type to another type.
# 
# Integer: int()
# Float: float()
# String: str()
# 
# The functions mentioned above are used for casting (convert) one data type to another.

# In[ ]:





# In[12]:


#10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos.'


# The error occurs because, python can only concatenate similiar data types together.
# In the question mentioned above, 'I have eaten' and 'burritos' are string values while 99 is an integer. To fix this issue, we need to convert the integer to a string first and then execute the code.

# In[15]:


#correction

'I have eaten ' + ' 99 ' + 'burritos.'

