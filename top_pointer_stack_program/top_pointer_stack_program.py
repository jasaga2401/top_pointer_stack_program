stack = []
top = -1  # Initialize top pointer to -1 for an empty stack

def is_empty():
    return top == -1

def push(item):
    global top
    top += 1
    stack.append(item)
    print(f"Pushed {item} onto the stack.")

def pop():
    global top
    if not is_empty():
        popped_item = stack.pop()
        top -= 1
        print(f"Popped {popped_item} from the stack.")
        return popped_item
    else:
        print("Stack is empty")

def peek():
    if not is_empty():
        return stack[top]
    else:
        print("Stack is empty")

def size():
    return top + 1

# Example usage:
push(1)
push(2)
push(3)

print("Stack size:", size())
print("Top of the stack:", peek())

while not is_empty():
    popped_item = pop()
    print("Popped:", popped_item)

