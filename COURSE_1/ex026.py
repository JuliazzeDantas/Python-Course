'''Exercise: Write a program that reads a sentence and displays:
    * How many time appear the letter "A"
    * Wich index does the letter "A" appears first
    * Wich index does the letter "A" appears last'''

sentence = input("Enter the sentence: ").strip().upper()

print('The letter "A" appears {} time'.format(sentence.count("A")))
print('The letter "A" appears firstly in index {}'.format(sentence.find("A")+1))
print('The last time that the letter "A" appears is in index {}'.format(sentence.rfind("A")+1))