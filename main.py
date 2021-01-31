"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""
class Record():
    def __init__(self, animal_n, endangered, continent,  life_span, enclosure):
      self.animal_n = animal_n
      self.endangered = endangered
      self.continent = continent
      self.life_span = life_span
      self.enclosure = enclosure

def main():
    animal = get_record()
    display_record(animal)

def get_record():
  animal_n = input("Animal name: ")
  endangered = input("Endangered (Yes or No): ")
  continent = input("Continent: ")
  life_span = (float(input("Life span: ")))
  enclosure = input("Enclosure: ")

  return Record(animal_n, endangered, continent, life_span, enclosure)

def display_record(record):
  print()
  print(record.animal_n, record.endangered, record.continent, record.life_span, record.enclosure)

main()
