# Reminder
Coursework Report
1. Introduction
a. Application Description:
The application is a reminder manager that allows users to create and store reminders for various tasks such as sending emails, SMS messages, or playing audio files. Users can set reminders for different events or activities and manage them efficiently through the program.
b. Running the Program:
To run the program, ensure you have Python installed on your system. Simply execute the provided Python script in your preferred Python environment.
c. Program Usage:
1. Instantiate a `ReminderManager` object with the desired file path for storing reminders.
2. Use the `save_reminder()` method of the `ReminderManager` to save reminders of different types such as email, SMS, or audio.
3. Utilize the `get_reminders()` method to retrieve saved reminders.
4. Iterate through the retrieved reminders and call the `send()` method on each reminder to execute the corresponding action (e.g., sending email/SMS, playing audio).
2. Body/Analysis
a. Functional Requirements Coverage:
1. **Reminder Creation**: The program allows users to create reminders of different types (email, SMS, audio) using the `save_reminder()` method of the `ReminderManager`.
2. **Reminder Storage :
Reminders are stored in a CSV file specified by the user, ensuring persistent storage of
reminders.
3. **Reminder Retrieval**: Users can retrieve saved reminders using the
`get_reminders()` method of the `ReminderManager`.
4. **Reminder Execution**: Reminders are executed through the `send()` method of the
respective reminder classes (`EmailReminder`, `SMSReminder`, `AudioReminder`), which perform actions such as sending emails/SMS or playing audio files.
3. Results and Summary Results
- Successfully implemented a reminder manager program capable of creating, storing, and executing reminders.
- Faced challenges in handling reminder data storage and retrieval efficiently, especially when dealing with different reminder types.
Summary
   
- The program effectively meets the functional requirements by providing a convenient way to manage reminders across different communication channels.
- This work has achieved the goal of creating a flexible and user-friendly reminder system.
Future Prospects :
- Possible extensions to the application include adding support for more reminder types
(e.g., push notifications, calendar integration), implementing user authentication for secure access, and enhancing the user interface for better usability.
3. Resources, References List
- Python Documentation: [https://docs.python.org/](https://docs.python.org/)
- CSV Module Documentation: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
- ABC (Abstract Base Classes) Module Documentation: [https://docs.python.org/3/library/abc.html](https://docs.python.org/3/library/abc.html)
