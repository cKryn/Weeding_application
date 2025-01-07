# Wedding Invitation App

This project is a wedding invitation management app built using **Streamlit** for the front-end and **SQLAlchemy** for the back-end database interaction. The application allows users to RSVP to a wedding event, provide additional details, and manage guest information.

## Features

- **Dynamic RSVP Form:**
  - Input validation for names, phone numbers, and attendance details.
  - Option to specify reasons for non-participation and provide additional feedback.
- **Tabbed Interface:**
  - Event details, schedule, menu, and transportation info available in a clean tabbed format.
- **Database Integration:**
  - Stores user responses in a MySQL database using SQLAlchemy.
- **Google Maps Embedding:**
  - Displays event locations with embedded Google Maps for user convenience.
- **Responsive UI:**
  - A responsive and visually appealing design using Streamlit features.

## Technologies Used

- **Python**
  - **Streamlit** for the user interface.
  - **SQLAlchemy** for database interaction.
  - **re** module for input validation.
- **MySQL** for database storage.
- **HTML/CSS** for custom styling within Streamlit.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/wedding-invitation-app.git
   cd wedding-invitation-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**

   - Make sure MySQL is running.
   - Update the database URL in the `mysql_db_url` variable inside the script:
     ```python
     mysql_db_url = "mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database_name>"
     ```
   - Create the required tables by running the script:
     ```bash
     python app.py
     ```

5. **Run the application:**

   ```bash
   streamlit run app.py
   ```

6. **Access the app:**

   Open your browser and navigate to `http://localhost:8501`.

## Project Structure

```plaintext
.
├── app.py                     # Main application script
├── src/
│   ├── modules.py             # Database models and session management
├── assets/
│   ├── sidebar_img.png        # Sidebar image
│   ├── weed_invitation.jpg    # Main image for invitation
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Database Schema

The application uses the following schema for storing RSVP data:

- **Table:** `users`

| Column                  | Type          | Description                                     |
|-------------------------|---------------|------------------------------------------------|
| `id`                   | Integer       | Primary key, auto-incremented.                 |
| `firstname`            | String (20)   | First name of the user.                        |
| `lastname`             | String (40)   | Last name of the user.                         |
| `phone`                | String (20)   | Phone number of the user.                      |
| `participation`        | String (20)   | RSVP status: "Particip" or "Nu particip".     |
| `non_participants_details` | String (400) | Feedback or reason for non-participation.      |
| `extra_details`        | String (400)  | Any additional feedback from the user.         |

## Customization

- Update event details, schedule, and menu in the respective `Streamlit` tabs.
- Replace placeholder images (`sidebar_img.png` and `weed_invitation.jpg`) in the `assets` folder with your custom images.
- Modify the CSS styling in the embedded HTML for further UI adjustments.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

© 2025 All Rights Reserved ~Gabriel//
