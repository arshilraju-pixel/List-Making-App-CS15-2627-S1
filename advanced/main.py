
# Two separate lists
todo_list = []
completed_list = []

# Stores previous versions of both lists for undo
history = []


# Display a list with its indexes
def display_list(items, title):
    print("---", title, "---")

    if len(items) == 0:
        print("Your list is empty...")
    else:
        for index in range(len(items)):
            print(f"{index}. {items[index]}")


# Save a copy of both lists before making a change
def save_history():
    history.append((todo_list.copy(), completed_list.copy()))


# Undo the previous change
def undo_change():
    global todo_list, completed_list

    if len(history) == 0:
        print("Nothing to undo")
    else:
        previous_state = history.pop()

        todo_list = previous_state[0]
        completed_list = previous_state[1]

        print("Previous change successfully undone")


# Get a valid index from the user
def get_index(items, title):
    display_list(items, title)

    if len(items) == 0:
        return None

    try:
        index = int(input("Enter the index of the item: "))

        if index < 0 or index >= len(items):
            print("Invalid index! Please try again.")
            return None

        return index

    except ValueError:
        print("Please enter a valid number!")
        return None


# Add a new task
def add_item():
    item = input("Enter a new task: ").strip()

    if item == "":
        print("Task cannot be empty!")
        return

    save_history()
    todo_list.append(item)

    print("Task successfully added!")


# Remove a task
def remove_item():
    index = get_index(todo_list, "TO-DO LIST")

    if index is not None:
        save_history()
        removed_item = todo_list.pop(index)

        print(f"Removed: {removed_item}")


# Display the lists
def display_lists():
    print("1. View To-Do List")
    print("2. View Completed List")

    choice = input("Choose a list to display: ")

    if choice == "1":
        display_list(todo_list, "TO-DO LIST")

    elif choice == "2":
        display_list(completed_list, "COMPLETED TASKS")

    else:
        print("Invalid choice! Please choose 1 or 2.")


# Replace an existing task
def replace_item():
    index = get_index(todo_list, "TO-DO LIST")

    if index is not None:
        new_item = input("Enter the replacement task: ").strip()

        if new_item == "":
            print("Task cannot be empty!")
            return

        save_history()

        old_item = todo_list[index]
        todo_list[index] = new_item

        print(f"Replaced '{old_item}' with '{new_item}'!")


# Mark a task as completed
def complete_item():
    index = get_index(todo_list, "TO-DO LIST")

    if index is not None:
        save_history()

        completed_task = todo_list.pop(index)
        completed_list.append(completed_task)

        print(f"Congratulations! '{completed_task}' is completed!")


# Main program
while True:

    print("========== ARSHIA'S TO-DO LIST APP ==========")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")
    print("4. Undo Previous Change")
    print("5. Replace an Item")
    print("6. Mark an Item as Completed")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_item()

    elif choice == "2":
        remove_item()

    elif choice == "3":
        display_lists()

    elif choice == "4":
        undo_change()

    elif choice == "5":
        replace_item()

    elif choice == "6":
        complete_item()

    elif choice == "7":
        print("Thank you for using Arshia's To-Do List App!")
        print("bye bye!")
        break

    else:
        print("Invalid menu choice! Please enter a number from 1-7.")
