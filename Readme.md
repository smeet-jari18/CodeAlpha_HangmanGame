# 🎮 Hangman Game — Python

A simple **text-based Hangman game** written in Python for the **CodeAlpha Python Programming Internship (Task 2)**.

The computer picks one random word, and the player guesses it **one letter at a time**. The player gets only **6 wrong guesses** — after that the game is over.

---

## 📌 Project Info

| | |
|---|---|
| **Task** | Task 2 — Hangman Game |
| **Domain** | Python Programming |
| **Organisation** | CodeAlpha |
| **Repo name** | `CodeAlpha_HangmanGame` |
| **Language** | Python 3 |
| **Type** | Console / text based (no graphics, no audio) |

---

## ✨ Features

- 🎲 **5 predefined words** — `python`, `computer`, `apple`, `program`, `student`
- 🎯 One word is picked randomly with `random.choice()`
- ❤️ **Only 6 wrong guesses allowed** (`max_guesses = 6`)
- 🔤 Shows the word with blanks and fills in the correct letters: `a p p _ _`
- 🚫 **Input validation** — only one alphabet letter is accepted; numbers, symbols, empty input and repeated letters are blocked
- 🏆 Win check with `all()` — game stops the moment the last letter is found
- 💀 Lose check with the `while ... else` block — shows the correct word at the end
- 🛑 Program never crashes on a wrong input (uses `continue`)

---

## ▶️ How to Run

**1. Check that Python is installed:**

```bash
python --version
```

**2. Run the game:**

```bash
python hangman.py
```

> On Mac / Linux use `python3 hangman.py`
> No extra library is needed — only the built-in `random` module.

---

## 🕹️ How to Play

1. The game shows blank spaces — one for each letter of the hidden word.
2. Type **one letter** and press Enter.
3. Letter is in the word → it appears in the blanks ✅
4. Letter is not in the word → one wrong guess is added ❌
5. Guess all letters before 6 mistakes → **you win** 🏆
6. Make 6 wrong guesses → **you lose**, and the correct word is shown 💀

---

## 🖥️ Sample Output

**Winning game (word = apple)**

```
============================================
         Welcome To Hangman
============================================

 word : _ _ _ _ _
Wrong guesses:  0 / 6
Guess one letter : a
Correct guess

 word : a _ _ _ _
Wrong guesses:  0 / 6
Guess one letter : p
Correct guess

 word : a p p _ _
Wrong guesses:  0 / 6
Guess one letter : l
Correct guess

 word : a p p l _
Wrong guesses:  0 / 6
Guess one letter : e
Correct guess

 word : a p p l e
Wrong guesses:  0 / 6
Congratulations! You guessed the word.
```

**Losing game**

```
 word : _ _ _ _ _ _
Wrong guesses:  5 / 6
Guess one letter : b
Wrong guess

 You lost the game.
The correct word was :  python
```

---

## 🧠 Python Concepts Used

| Concept | Where it is used |
|---|---|
| **`random` module** | `random.choice(words)` picks one random word from the list |
| **List** | `words` (the 5 words), `guesses_letter` (letters already tried) |
| **`while` loop** | Runs the game while `wrong_guesses < max_guesses` |
| **`while ... else`** | The `else` part runs only when the loop ends **without** `break` → the "you lost" message |
| **`for` loop** | Goes through every letter of the word to build the blank display |
| **`if-else`** | Checks whether the guessed letter is inside the word |
| **Strings** | `.lower()`, `.strip()`, `.isalpha()`, `+=` for joining letters |
| **`in` operator** | `if letter in guesses_letter` and `if guess in select_word` |
| **`all()` function** | `all(letter in guesses_letter for letter in select_word)` → `True` only when every letter is guessed |
| **`len()`** | `len(guess) != 1` makes sure only one character is typed |
| **`break` / `continue`** | `break` ends the game on a win, `continue` skips bad or repeated input |

---

## 📂 Code Structure

```
CodeAlpha_HangmanGame/
│
├── Hangman_Game.py     → the complete game (single file)
└── README.md      → this file
```

**How the code flows:**

| Step | Line idea | Work |
|---|---|---|
| 1 | `import random` | Brings in the random tool |
| 2 | `words = [...]` | The list of 5 predefined words |
| 3 | `select_word = random.choice(words)` | Picks the secret word |
| 4 | `guesses_letter = []`, `wrong_guesses = 0` | Prepares the memory (tried letters + mistake count) |
| 5 | `while wrong_guesses < max_guesses:` | Main game loop |
| 6 | `for letter in select_word:` | Builds the display `a p p _ _` |
| 7 | `if all(...)` | Checks the win condition |
| 8 | `guess = input(...).lower().strip()` | Takes one letter from the player |
| 9 | `if len(guess) != 1 or not guess.isalpha()` | Blocks wrong input |
| 10 | `if guess in guesses_letter` | Blocks repeated letters |
| 11 | `guesses_letter.append(guess)` | Remembers the letter |
| 12 | `if guess in select_word` | Correct → message; wrong → `wrong_guesses += 1` |
| 13 | `else:` (of the while) | Shows "You lost" + the correct word |

---

## 🔍 Understanding the main logic

```python
select_word = random.choice(words)
```
`random.choice()` picks **one item** from a list. The player never sees
`select_word` until the game ends.

```python
display_word = ""
for letter in select_word:
    if letter in guesses_letter:
        display_word += letter + " "
    else:
        display_word += "_ "
```
This builds the visible word. Every letter of the secret word is checked:
already guessed → show the letter, not guessed → show `_`.

> ⚠️ **Important:** the `else` must be aligned **inside** the `for` loop
> (indented under `if`). If it is written at the same level as `for`, Python
> treats it as the loop's `else` and adds only **one** underscore — then the
> word looks like `a_` instead of `_ _ _ _ _`.

```python
if all(letter in guesses_letter for letter in select_word):
    print("Congratulations! You guessed the word.")
    break
```
`all()` returns `True` only if the condition is true for **every** letter. This is
a short and clean way to check "did the player find all letters?".

```python
guess = input("Guess one letter : ").lower().strip()
```
`input()` takes the text, `.lower()` makes `A` into `a`, and `.strip()` removes
extra spaces — so `" A "` also works.

```python
if len(guess) != 1 or not guess.isalpha():
    print("Please Enter Only One alphabet letter.")
    continue
```
Two checks: exactly **one character**, and it must be a **letter**.
`continue` means "skip the rest and ask again" — so the game never crashes.

```python
if guess in guesses_letter:
    print("You already guessed this letter.")
    continue
```
A repeated letter is not counted again. This is fair play.

```python
if guess in select_word:
    print("Correct guess")
else:
    print("Wrong guess")
    wrong_guesses += 1
```
The main rule: correct letter → nothing lost; wrong letter → one chance gone.
`+= 1` is short for `wrong_guesses = wrong_guesses + 1`.

```python
else:
    print("\n You lost the game.")
    print("The correct word was : ", select_word)
```
This `else` belongs to the **`while`** loop. It runs only when the loop finishes
normally (6 wrong guesses) — not when the player wins, because a win uses `break`.
That is a very nice Python trick. 👏

---

## 🚀 Future Improvements (ideas)

- Keep a **score board** so the player can play again without restarting the program
- Show the **letters already tried** on screen
- Add difficulty levels (easy = 4 letters, hard = 8 letters)
- Add an **ASCII hangman drawing** that grows with each wrong guess
- Read the word list from a `words.txt` file
- Two-player mode (one player types the word, the other guesses)

---

## 👩‍💻 Author

**Smeet Jariwala**
Python Programming Intern @ CodeAlpha
📧 smeetjariwala17@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📜 Acknowledgement

Built as part of the **Python Programming Internship** at
[CodeAlpha](https://www.codealpha.tech) — www.codealpha.tech

⭐ If you liked this project, please give this repository a star!