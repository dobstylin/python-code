import random

class SimplePlotGenerator:
    def __init__(self):
        self.story = 'Something happens'
    
    def generate(self):
        return self.story
        
class RandomPlotGenerator(SimplePlotGenerator):
    def __init__(self):
        """Opens and gathers list of words from each text document"""
        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof !='']
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        self.adjectives_evil = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        self.villians = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']
    
    def generate(self):
        """Randomly selects 1 terms from each subject and returns the plot"""
        self.story = random.choice(self.name) + ', a ' + random.choice(self.adjectives) + ' ' + random.choice(self.professions) + ', must ' + random.choice(self.verbs) + ' the ' + random.choice(self.adjectives_evil) + ' ' + random.choice(self.villian_job) + ', ' + random.choice(self.villians) + '.'
        #print (self.story)
        return self.story

class InteractivePlotGenerator(SimplePlotGenerator):
    def __init__(self):
        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof !='']
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        self.adjectives_evil = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        self.villians = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']
        
        print('\n You will asked to enter a number 1-5 that corresponds to your choice of word or terms.\n')
        print('This will happen 7 times to generate the plot.\n')

    def CheckInput(self, random_5):
        while True:
            try:
                print('This is a list of 5 random selections')
                print(random_5, '\n')
                user_select = int(input('For the 1st, 2nd, 3rd, 4th, and 5th terms, enter 1,2,3,4 or 5: '))
                if user_select == 1:
                    return random_5[0]
                elif user_select == 2:
                    return random_5[1]
                elif user_select == 3:
                    return random_5[2]
                elif user_select == 4:
                    return random_5[3]
                elif user_select == 5:
                    return random_5[4]                
                else:
                    print('Enter a number 1-5 please.')
            except:
                print('Invalid Input')
    
    def generate(self):
        name_5 = random.sample(self.name, 5)
        self.pick_name = self.CheckInput(name_5)
        
        adj_5 = random.sample(self.adjectives, 5)
        self.pick_adj = self.CheckInput(adj_5)
        
        prof_5 = random.sample(self.professions, 5)
        self.pick_prof = self.CheckInput(prof_5)
        
        verb_5 = random.sample(self.verbs, 5)
        self.pick_verb = self.CheckInput(verb_5)
        
        adj_e_5 = random.sample(self.adjectives_evil, 5)
        self.pick_adj_e = self.CheckInput(adj_e_5)
        
        villian_job_5 = random.sample(self.villian_job, 5)
        self.pick_villian_job = self.CheckInput(villian_job_5)
        
        villian_5 = random.sample(self.villians, 5)
        self.pick_villians = self.CheckInput(villian_5)
        
        self.story = self.pick_name + ', a ' + self.pick_adj + ' ' + self.pick_prof + ', must ' + self.pick_verb + ' the ' + self.pick_adj_e + ' ' + self.pick_villian_job + ', ' + self.pick_villians + '.'
        
        return self.story

class PlotViewer:
    """Plot Viewer to view multiple generator"""

    def registerPlotGenerator(self, generator):
        """Register generator class"""

        self.generate_sub = generator

    def generate(self):
        """Pass generate method from other Class"""

        return self.generate_sub.generate()

def main():
    """Main function, types of plot generators can be changed here"""

    pv = PlotViewer()
    pv.registerPlotGenerator(InteractivePlotGenerator())
    print(pv.generate())

if __name__ == '__main__':
    main()
    
