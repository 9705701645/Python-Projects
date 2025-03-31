# ATM Console Application

## Overview
This is a console-based ATM application implemented using Python. It utilizes only control and conditional statements along with dictionary data structures to manage user details. The application supports fundamental ATM operations such as deposit, withdrawal, PIN generation, and mini statements.

## Features
- **User Authentication**: Secure access using PIN-based authentication.
- **Deposit Money**: Users can deposit money into their account.
- **Withdraw Money**: Allows users to withdraw money if sufficient balance is available.
- **PIN Generation**: Users can create or reset their PIN.
- **Mini Statement**: Displays a brief transaction history.

## Technologies Used
- **Python**
- **Dictionary Data Structure**
- **Control and Conditional Statements**

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repository
   ```
3. Run the Python script:
   ```sh
   python atm.py
   ```

## How It Works
- Upon starting, users are prompted to enter their PIN to access their account.
- They can choose from available options: Deposit, Withdraw, PIN Generation, or View Mini Statement.
- Transactions are logged, and the updated balance is maintained within the dictionary-based database.
- The application runs entirely in the console without any external dependencies.

## Future Enhancements
- Implement database storage instead of dictionaries.
- Add user-friendly UI (Graphical Interface).
- Implement security features such as OTP-based authentication.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).
