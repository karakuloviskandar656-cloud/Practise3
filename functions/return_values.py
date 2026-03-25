# Functions can send data back to the code that called them using the return statement.

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())
