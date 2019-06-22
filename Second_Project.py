#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import sys
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return moves[0]

    def learn(self, my_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        my_move = input('please enter your move or z to end the game: \n')
        while my_move not in moves:
            if my_move == 'z':
                print('Thanks for Playing')
                print('***GOODBYE***')
                sys.exit()
            print('invalid input please try again')
            my_move = input('please enter your move:\n')
        return my_move


class ReflecPlayer(Player):

    def __init__(self):
        self.counter = 0

    def learn(self, my_move):
        self.my_move = my_move

    def move(self):
        if self.counter == 0:
            self.counter += 1
            return random.choice(moves)
        return self.my_move


class CyclePlyer(Player):
    counter = -1

    def move(self):
        self.counter += 1
        if self.counter == 3:
            self.counter = 0
        return moves[self.counter]


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.wins = 0
        self.loses = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1)
        print(f"YOU: {move1} || COMPUTER: {move2}")
        if move1 == move2:
            print("**TIE**")
        elif beats(move1, move2):
            self.wins += 1
            print("**YOU WON**")
        else:
            self.loses += 1
            print("**COMPUTER WON**")

    def play_game(self):
        print("**GAME START!**")
        while True:
            try:
                rounds = int(input('How many rounds would '
                                   'you like to play: \n'))
                break
            except ValueError:
                print('INVALID INPUT, PLEASE TYPE AN INTEGER')

        def one_round(self):
            if rounds == 1:
                return rounds == 1
        for round in range(int(rounds)):
            print(f"Round {round}:")
            print(f" **THE SCORE** \n You: {self.wins} X "
                  f"Computer: {self.loses}")
            round += 1
            self.play_round()
        print(f" **THE SCORE** \n You: {self.wins} X "
              f"Computer: {self.loses}")
        if self.wins > self.loses:
            print('**CONGRATS!,YOU WON THE GAME**')
        elif self.wins < self.loses:
            print("**THE COMPUTER WON THE GAME!**")
        else:
            print('**THE GAME WAS TIE**')

if __name__ == '__main__':
    while True:
        print(f"If you would like to stop playing type 'z'")
        user_choice = input('Who would you like to play with?,''\n'
                            'Please enter "random", "reflect", "repeat",'
                            'or "cycle":\n')
        if user_choice == 'z':
            print('***GOODBYE***')
            break
        elif user_choice == 'random':
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
            break
        elif user_choice == 'cycle':
            game = Game(HumanPlayer(), CyclePlyer())
            game.play_game()
            break
        elif user_choice == 'repeat':
            game = Game(HumanPlayer(), Player())
            game.play_game()
            break
        elif user_choice == 'reflect':
            game = Game(HumanPlayer(), ReflecPlayer())
            game.play_game()
            break

