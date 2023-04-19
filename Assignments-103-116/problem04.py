class Games:
    # Write Class Content
    def __init__(self, name_game):
        self.name_game = name_game
        type_arg = type(self.name_game)
    def show_games(self):
        if (isinstance(self.name_game, str)):
            print (f"I Have One Game Called \"{self.name_game}\" ")
        elif (isinstance(self.name_game, list)):
            print ("I Have Many Games : ")
            for game in self.name_game:
                print(f"-- {game}")
        else:
            print (f"I Have {self.name_game} Game.")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.

