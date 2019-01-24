#!/usr/bin/env python
from __future__ import print_function
from cmd import Cmd
import numpy as np
import re
import time
import sys
import random

class Prompt(Cmd):

	intro = '\nwelcome. \n\nbegin by typing "help" to see what you can do'
	prompt = '\n--> '
	doc_header = 'learn what to feed me by typing "help <command>"'
	if len(sys.argv) < 2:
		pass
	else:
		try:
			text = open(sys.argv[1:][0], encoding='utf8').read()
		except IOError:
			print('let me chew on [some words]')

	def do_lullaby(self, args):
		"""just lend me your eyes and a bit of your time. i will sing to you, just tell me [how long to sing]"""
		if len(args) == 0:
			print('give me [time]')
		else: 
			command = args.split()
			corpus = re.split('\s|(?<!\d)[.]|[.](?!\d)', self.text)
			corpus = list(filter(None, corpus))

			def make_pairs(corpus):
					for i in range(len(corpus)-1):
						yield (corpus[i], corpus[i+1])

			pairs = make_pairs(corpus)

			word_dict = {}
			for word_1, word_2 in pairs:
			    if word_1 in word_dict.keys():
			        word_dict[word_1].append(word_2)
			    else:
			        word_dict[word_1] = [word_2]

			first_word = np.random.choice(corpus)

			if first_word and first_word.capitalize() not in word_dict:
					story = [random.choice(corpus)]
			else: 
					story = [first_word]

			n_words = int(command[0])
			print("%s" % first_word)
			for i in range(n_words - 1):
				found_word = np.random.choice(word_dict[story[-1]])
				time.sleep(0.55)
				print("%s" % found_word)


	def do_storytime(self, args):
		"""sit back and read. feel free to put your feet up, tuck in with a blanket, tea, etc."""
		corpus = self.text.split()

		def make_pairs(corpus):
				for i in range(len(corpus)-1):
					yield (corpus[i], corpus[i+1])

		pairs = make_pairs(corpus)

		word_dict = {}
		for word_1, word_2 in pairs:
		    if word_1 in word_dict.keys():
		        word_dict[word_1].append(word_2)
		    else:
		        word_dict[word_1] = [word_2]

		first_word = np.random.choice(corpus)

		if first_word and first_word.capitalize() not in word_dict:
				story = [random.choice(corpus)]
		else: 
				story = [first_word]

		max_sentences = 1
		count = 0
		print("%s" % first_word.capitalize(),end=" ")
		while count is not max_sentences:
			found_word = np.random.choice(word_dict[story[-1]])
			time.sleep(0.55)
			sys.stdout.write(found_word + " ")
			sys.stdout.flush()

			if "." in found_word:
				count += 1
			story.append(found_word)
		sys.stdout.write("\n")
		sys.stdout.flush()

	def do_generate(self, args):
		"""make_story [first word] [number of sentences]"""
		if len(args) < 2:
			sys.stdout.write('hungry for [word] and [number of sentences]')
			sys.stdout.flush()
		else:
			command = args.split()
			first_word = command[0]

			corpus = self.text.split()

			def make_pairs(corpus):
				for i in range(len(corpus)-1):
					yield (corpus[i], corpus[i+1])

			pairs = make_pairs(corpus)

			#initialize dictionary
			word_dict = {}
			for word_1, word_2 in pairs:
				if word_1 in word_dict.keys():
					word_dict[word_1].append(word_2)
				else:
					word_dict[word_1] = [word_2]

			story = [first_word]
			max_sentences = int(command[1])

			if first_word and first_word.capitalize() not in word_dict:
				sys.stdout.write("your chosen word does not exist in the text\nplease feed me another")
				sys.stdout.flush()

			else:
				count = 0
				print("%s" % first_word.capitalize(),end=" ")
				while count is not max_sentences:
					found_word = np.random.choice(word_dict[story[-1]])
					time.sleep(0.55)
					sys.stdout.write(found_word + " ")
					sys.stdout.flush()

					if "." in found_word:
						count += 1
					story.append(found_word)
				sys.stdout.write("\n")
				sys.stdout.flush()

				story = ' '.join(story)
				story = re.sub('<[^<]+?>', '', story)
				story = re.sub('\\s+',' ',story)
		#print("%s" % story)

	def do_quit(self, args):
		"""enter <quit> to stop this madness """
		print('The End...')
		return True


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('let me chew on [some words]... \ni.e. markov2.py [speeches.txt]')
	else:
		Prompt().cmdloop()
	# prompt = Prompt()
	# prompt.prompt = '\n--> '
	# prompt.cmdloop('\nLet''s begin...\n\nOnce upon a time,')
