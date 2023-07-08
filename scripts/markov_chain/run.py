from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

mc.add_file('workfile.txt')
print mc.generate_text(20)