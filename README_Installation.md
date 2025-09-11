# SentinelNet ‒ Installation & Setup

These instructions will help you get the SentinelNet environment running locally.

---

## Prerequisites

- Python 3.8+  
- `pip` (or `conda`) for managing Python packages  
- Git (to clone the repository)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SpringBoardMentor193s/SentinelNet.git
    cd SentinelNet
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install required Python packages:

    ```bash
    pip install -r Requirements.txt
    ```

---

## Project Structure

Here are some of the important items in the repo:

```
SentinelNet/
├── Datasets/                       # Raw or processed datasets
├── Scripts/                        # Utility / preprocessing / training scripts
├── docs/                           # Documentation
├── main.py                         # Principal entry point
├── Requirements.txt               # Dependencies
├── Data sets.md                   # Dataset descriptions
├── Network Intrusion Detection Dataset.md # More dataset info
├── LICENSE                        # MIT License
└── README.md                      # Project overview
```

---

## Running the Project

To run the main module:

```bash
python main.py
```

This should kick off the process (e.g. loading data, training, evaluating, etc.) depending on how `main.py` is set up.

---

## Troubleshooting

- If you get import errors, ensure you are in the correct virtual environment.  
- Ensure that the `Datasets` folder has the required data files (as described in `Data sets.md`).  
- If package version conflicts arise, see the versions listed in `Requirements.txt`.
