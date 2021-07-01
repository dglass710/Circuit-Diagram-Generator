def main(s, p, of):
   outfile = open(of, 'w')
   outfile.write('\\documentclass[12pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[english]{babel}\n\n\\usepackage{circuitikz}\n\\usepackage{xfp}\n\\setlength{\\paperheight}{')
   outfile.write(f'{2*s+4}')
   outfile.write('in}\n\\setlength{\\paperwidth}{')
   outfile.write(f'{.85*p+6}')
   outfile.write('in}\\newcommand\\n{5}\n\\begin{document}\n\\vbox{\n\\begin{center}\n\\begin{circuitikz}\n')
   outfile.write(f'\\draw\n\t({(p-1)*2},{(s-1)*5+4}) to [short] ({(p+1)*2},{(s-1)*5+4}) \n\t({(p+1)*2},{(s-1)*5+4}) to [short, l_={4*s}V] ({(p+1)*2+5},{(s-1)*5+4})\n\t({(p-1)*2},0) to [short] ({(p+1)*2},0)\n\t({(p+1)*2},0) to [short, l_=0V] ({(p+1)*2+5},0)\n\t({(p+1)*2},{(s-1)*5+4}) to [transmission line, /tikz/circuitikz/bipoles/length=10cm] ({(p+1)*2},0)\n\t({(p+1)*2+5},{(s-1)*5+4}) to [transmission line, /tikz/circuitikz/bipoles/length=10cm, l_=Motors] ({(p+1)*2+5},0);\n')
   for i in range(1, s+1):
       outfile.write('\\draw\n\t')
       if i < s:
           outfile.write(f'({p-1},{i*5}) to [short, l_={4*i}V] ({p-1},{5*(i-1)+4})\n\t')
       outfile.write(f'(0,{(i-1)*5+4}) to [short, l_=Group {i}] ({(p-1)*2},{5*(i-1)+4})\n\t')
       outfile.write(f'to [american voltage source, l_=4V] ({(p-1)*2},{(i-1)*5})\n\t')
       outfile.write(f'(0,{(i-1)*5+4}) to [american voltage source, l_=4V] (0,{(i-1)*5})\n\t')
       outfile.write(f'to [short] ({(p-1)*2},{(i-1)*5})\n\t')
       for j in range(1, p-1):
           outfile.write(f'({2*j},{(i-1)*5+4}) to [american voltage source, l_=4V] ({2*j},{(i-1)*5})\n\t')
       outfile.write(';')

   outfile.write('\\end{circuitikz}\n\\end{center}\n}\n\\end{document}\n')

main(24,10,'test.tex')
