# Simple Auction Program 🏷️

This is a simple Python project I created when I was starting my journey as a self-taught programmer. The program simulates an auction where participants can submit their bids, and the winner is determined based on the highest bid.

## Description

The auction program allows multiple participants to enter their bids, and at the end, it will announce the winner with the highest bid.

### Features:
- Collects the name and bid of each participant.
- Allows multiple participants to join the auction.
- Closes the auction when no more participants wish to join.
- Announces the winner and the winning bid.

## How It Works

1. The program asks each participant for their name and bid amount.
2. The bids are stored in a dictionary with the participant's name as the key and the bid amount as the value.
3. Once all participants have submitted their bids, the program determines the highest bid and announces the winner.

## Usage

To run this program, simply execute the script in your Python environment. The program will guide you through entering your name and bid. When all participants have joined, it will display the winner.

### Example:

```bash
Please enter your name:
John
Enter the amount you want to bid: $
150
Are there more participants? Y / N
Y

Please enter your name:
Jane
Enter the amount you want to bid: $
200
Are there more participants? Y / N
N

The auction is closed
The winner of the auction is Jane with a bid of $200