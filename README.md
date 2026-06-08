# Task-1-Vennelakanchanapalli
DecodeLabs AI Chatbot (Project 1)A lightweight, highly efficient, rule-based AI chatbot built using Python. This project serves as a foundational implementation of control flow, string manipulation, and optimized data structures for conversational logic.
Unlike traditional rule-based bots that rely on cumbersome if-elif ladders, this chatbot utilizes a Python dictionary (Hash Map) to achieve instantaneous response matching.
🚀 Key Features
~O(1) Logic Engine: Eliminates the deep nesting of conditional structures, ensuring instant response lookups regardless of the database size.
~Input Sanitization Pipeline: Automatically processes user inputs by trimming whitespace and normalizing case text to ensure robust matching.
~Graceful Fallbacks: Uses a default catch-all response system when user inputs don't match existing keys.
~Continuous Heartbeat Loop: Features an interactive command-line interface that runs uninterrupted until explicitly shut down by the user.
🛠️ How It WorksThe architecture is divided into three distinct lifecycle phases:Code snippetgraph LR
    A[Raw Input] --> B[Phase 1: Sanitization]
    B --> C[Phase 2: O1 Lookup Engine]
    C --> D[Phase 3: Heartbeat Loop Output]
Phase 1: Sanitization (sanitize) – Strips accidental leading/trailing spaces and converts the input string to lowercase to handle variations in user typing.
Phase 2: Logic Engine (get_response) – Uses Python's built-in dictionary access method (.get()) to fetch matching values in constant time while yielding a standard fallback guide string for unknown inputs.
Phase 3: Heartbeat Loop (run_chatbot) – Wraps the operations inside an infinite evaluation loop that listens for the exit trigger.
💻 Sample InteractionPlaintext========================================
     DecodeLabs AI Chatbot   -   Online
     Type 'exit' to shut down
========================================

User: Hello
Bot: Hi there! How can I help you today?

User: WHAT IS AI
Bot: AI is the simulation of human intelligence by machines.

User: project 1
Bot: I do not understand. Type 'help' to see what I can do.

User: what is project 1
Bot: Project 1 is the foundational Rule-Based AI Chatbot focused on Control Flow and Logic.

User: exit
Bot: Shutting down... See you next time!
⚙️ Installation & Running the Bot
Prerequisites
Ensure you have Python 3.x installed on your local machine.
Execution
1.Clone this repository to your desktop.
2.Open your terminal or command prompt inside the project directory.
3.Execute the script directly using:Bashpython chatbot.py
📁 File Structure
Plaintext├── chatbot.py          # Main application file containing the rules and execution loop
└── README.md           # Project documentation and setup guide
🤝 Contributing
Feel free to fork this project and scale up the responses dictionary database, or integrate a frontend framework like Tkinter or Flask!
1.Fork the Project
2.Create your Feature Branch (git checkout -b feature/NewResponses)
3.Commit your Changes (git commit -m 'Added more conversational intents')
4.Push to the Branch (git push origin feature/NewResponses)
5.Open a Pull Request
👤 ContactVennela KanchanapalliOrganization: https://www.linkedin.com/in/vennelakanchanapalli
GitHub Repository: https://github.com/vennela0811/Task-1-Vennelakanchanapalli
📄 License
Distributed under the MIT License.
See the snippet below for terms:PlaintextMIT License

Copyright (c) 2026 Vennela Kanchanapalli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
