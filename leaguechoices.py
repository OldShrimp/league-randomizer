import random
from PIL import Image

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
                self.combat_masteries[(style + 1 - 2 * random.randint(0,1)) % 3] += 1
                
    def create_combat_graphic(self) -> Image.Image:
        graphic = Image.open('./images/base.png')
        melee_images = ['./images/melee1.png', './images/melee2.png', './images/melee3.png', 
                        './images/melee4.png', './images/melee5.png', './images/melee6.png']
        range_images = ['./images/range1.png', './images/range2.png', './images/range3.png', 
                        './images/range4.png', './images/range5.png', './images/range6.png']
        mage_images = ['./images/mage1.png', './images/mage2.png', './images/mage3.png', 
                       './images/mage4.png', './images/mage5.png', './images/mage6.png']
        tier_images = ['./images/tier1.png', './images/tier2.png', './images/tier3.png', 
                       './images/tier4.png', './images/tier5.png', './images/tier6.png']
        passive_images = ['./images/passive1.png', './images/passive2.png', './images/passive3.png', 
                          './images/passive4.png', './images/passive5.png', './images/passive6.png']
        tier_width = 240
        x_offset = 480
        melee_y_offset = 40
        range_y_offset = 304
        mage_y_offset = 588
        passive_y_offset = 872
        highest_tier = max(self.combat_masteries[0], max(self.combat_masteries[1], self.combat_masteries[2]))
        for i in range(highest_tier):
            tier = Image.open(tier_images[i])
            graphic.paste(tier, (x_offset + tier_width * i, 0), mask=tier)
            passive = Image.open(passive_images[i])
            graphic.paste(passive, (x_offset + tier_width * i, passive_y_offset), mask=passive)
        for i in range(self.combat_masteries[0]):
            img = Image.open(melee_images[i])
            graphic.paste(img, (x_offset + tier_width * i, melee_y_offset), mask=img)
        for i in range(self.combat_masteries[1]):
            img = Image.open(range_images[i])
            graphic.paste(img, (x_offset + tier_width * i, range_y_offset), mask=img)
        for i in range(self.combat_masteries[2]):
            img = Image.open(mage_images[i])
            graphic.paste(img, (x_offset + tier_width * i, mage_y_offset), mask=img)
        
        return graphic
 
def generate_rand_league() -> LeagueChoices:
    build = LeagueChoices()
    build.randomize()
    return build
   
if __name__ == '__main__':
    random.seed()
    a = generate_rand_league()
    print('Randomized League Choices:')
    print(f'  Regions: {', '.join(a.regions)}\n'
         +f'  Combat Masteries: Melee {a.combat_masteries[0]}, Ranged {a.combat_masteries[1]}, Mage {a.combat_masteries[2]}\n'
         +f'  Relics: {', '.join(a.relics)}')
    #a.combat_masteries = [5,5,0]
    a.create_combat_graphic().save('combat-graphic-generated.png')