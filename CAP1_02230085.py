################################
# Your Name: Tenzin Chophel
# Your Section: 1 Electrical
# Your Student ID Number: 02230085
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score: 41076
# Put your number here: 5
################################

# Function to extract game data from a file
def fetch_game_data(input_file):
    """
    This function opens the specified file and reads its content.
    Each line in the file is expected to represent a single game round,
    consisting of an opponent's choice and the outcome of that round.
    
    Args:
    input_file (str): Path to the game data file.
    
    Returns:
    list: A list of records, each containing the opponent's choice and the round's outcome.
    """
    # Attempt to open and read the file
    try:
        # 'with' statement ensures the file is properly closed after its suite finishes
        with open(input_file, 'r') as file:
            # Read each line from the file and split it into opponent's choice and outcome
            # The resulting list comprehension returns a list of tuples
            return [line.strip().split() for line in file]
    # If the file is not found, print an error message and return an empty list
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return []

# Function to compute the game score
def compute_game_score(game_rounds):
    """
    This function calculates the total score based on the game rounds data.
    It uses a predefined scoring system where different outcomes and choices
    have different point values.
    
    Args:
    game_rounds (list): List of game rounds data, each round is a tuple.
    
    Returns:
    int: The total score calculated from the game rounds.
    """
    # Define a scoring system using a nested dictionary
    # The outer keys represent the opponent's choice ('A', 'B', 'C')
    # The inner keys represent the outcome ('Y', 'X', 'Z') and their respective scores
    score_rules = {
        'A': {'Y': 4, 'X': 1, 'Z': 7},
        'B': {'Y': 3, 'X': 6, 'Z': 2},
        'C': {'Y': 7, 'X': 2, 'Z': 5}
    }
    # Calculate the total score by iterating over each game round
    # and summing up the scores based on the scoring rules
    return sum(score_rules[choice][outcome] for choice, outcome in game_rounds)

# Execute the game score calculation
def execute():
    """
    This is the main execution function of the script.
    It specifies the file path, fetches the game data, and computes the score.
    """
    # Specify the file path to the game data file
    game_file = r"C:\Users\chimi\Downloads\input_5_cap1.txt"
    # Fetch the game rounds data from the file
    game_data = fetch_game_data(game_file)
    # If there is game data, compute and print the total score
    if game_data:
        print(f"Total Game Score: {compute_game_score(game_data)}")

# Check if the script is run directly and not imported as a module
if __name__ == "__main__":
    # If the script is run directly, execute the main function
    execute()
