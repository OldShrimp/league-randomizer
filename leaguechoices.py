import random

REGIONS = ['Morytania', 'Varlamore', 'Fremmenik', 'Kandarin',
           'Desert', 'Wilderness', 'Tirannwn', 'Kourend', 'Asgarnia']
RELICS = [
          ['Power Miner', 'Lumberjack', 'Animal Wrangler'],
          ['Fairy\'s Flight', 'Bank Heist', 'Clue Compass'],
          ['Total Recall', 'Banker\'s Note'],
          ['Grimoire', 'Overgrown'],
          ['Golden God']
         ]

class LeagueChoices:
    def __init__(self) -> None:
        self.regions = []
        self.combat_masteries = [0,0,0]
        self.relics = []
    
    def randomize(self) -> None:
        self.randomize_regions()
        self.randomize_relics()
        self.randomize_Combats()
        
    
    def randomize_regions(self) -> None:
        self.regions = REGIONS
        random.shuffle(self.regions)
        self.regions = self.regions[:3]
        
    def randomize_relics(self) -> None:
        self.relics = RELICS
        for i in range(len(self.relics)):
            random.shuffle(self.relics[i])
            self.relics[i] = self.relics[i][0]
            
    def randomize_Combats(self) -> None:
        self.combat_masteries = [0,0,0]
        for i in range(10):
            style = random.randint(0,2)
            if self.combat_masteries[style] < 6:
                self.combat_masteries[style] += 1
            else:
                self.combat_masteries[(style + 1) % 3] += 1
  
def generate_rand_league():
    a = LeagueChoices()
    a.randomize()
    print('Randomized League Choices:')
    print(f'  Regions: {', '.join(a.regions)}\n'
         +f'  Combat Masteries: Melee {a.combat_masteries[0]}, Ranged {a.combat_masteries[1]}, Mage {a.combat_masteries[2]}\n'
         +f'  Relics: {', '.join(a.relics)}')

if __name__ == '__main__':
    random.seed()
    generate_rand_league()