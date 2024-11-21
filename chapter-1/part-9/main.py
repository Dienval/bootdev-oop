class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        cost = 0
        cost += self.armor
        cost *= self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
