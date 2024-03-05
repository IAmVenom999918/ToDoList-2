# Project To-Do List:

## UI Development:

Design and implement a user-friendly single-page interface using customtkinter.

Include:
- **Task entry section**: Entry field and button to add new tasks.
- **Task list section**: Listbox to display existing tasks with appropriate information (e.g., name, due date, priority).
- **Task action section**: Buttons or checkboxes for marking tasks complete and deleting them.
- *(Optional)* Implement additional sections for search, filters, or settings.

## Data Storage:

Choose and implement a data storage solution:

- In-memory list (simplest, data lost on app close): ✅
- External file (persists across app restarts): ⬜
- Database (scalable, advanced features): ⬜

Implement functions for CRUD (Create, Read, Update, Delete) operations on tasks:
- add_task(task_name): Adds a new task to storage. ⬜
- get_tasks(): Retrieves all tasks from storage. ⬜
- mark_task_completed(task_id): Updates a task's completion status. ⬜
- delete_task(task_id): Removes a task from storage. ⬜

## Integration:

Connect UI actions (button clicks, listbox selections) to corresponding functions for adding, retrieving, marking, and deleting tasks. ⬜

## Enhancements (Optional):

- Implement error handling for user input and data operations. ⬜
- Add search functionality for tasks. ⬜
- Include due dates and reminders for tasks (requires additional logic and data storage considerations). ⬜

## Testing:

Write unit tests to ensure the app's functionality works as expected. ⬜

## Documentation:

Update the README file with clear instructions and explanations. ✅ (This file)

