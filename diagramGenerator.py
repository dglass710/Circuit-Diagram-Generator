import sys

def main(s, p, of):
   if any([type(x) != int for x in [s,p]]):
       sys.exit('s or p is not an int')
#      raise Exception('s or p is not an int')
   if any([x < 2 for x in [s,p]]):
       sys.exit('s or p is less than 2')
#      raise Exception('s or p is less than 2')
   if p > 96:
       sys.exit('Too many in parallel')
#      raise Exception('Too many in parallel')
   if s > 110:
       sys.exit('Too many in series')
#      raise Exception('Too many in series')
   if s*p > 46**2:
       sys.exit('Not enough memory to generate pdf')
#      raise Exception('Not enough memory to generate pdf')

   width = 11-39*(p-2)
   outfile = open(of, 'w')
   outfile.write('\\documentclass[12pt]{article}\n%\\usepackage{a4wide}\n\\usepackage{geometry}\n\\newgeometry{vmargin={10mm,')
   outfile.write(f'{-(19+50*(s-4))}mm')
   outfile.write('}, hmargin={ ')
   outfile.write(f'{width/2}mm,')
   outfile.write(f'{width}')
   outfile.write('mm}}\n%\\usepackage{showframe}\n\\usepackage[utf8]{inputenc}\n\\usepackage[english]{babel}\n\n\\usepackage{circuitikz}\n\\usepackage{xfp}\n\\setlength{\\paperheight}{')
   outfile.write(f'{2*s+6}')
   outfile.write('in}\n\\setlength{\\paperwidth}{')
   outfile.write(f'{.85*p+9}')
   outfile.write('in}\\newcommand\\n{5}\n\\title{')
   outfile.write(f'{s}s {p}p')
   outfile.write('}\n\\author{David A. Glass}\n\\begin{document}\n\\maketitle\n\\vbox{\n\\begin{center}\n\\begin{circuitikz}\n')
   outfile.write(f'\\draw\n\t\n\t({p-1},{5*s+2}) to [short, l_={2.9*s:.1f}V - {4.2*s:.1f}V] ({(p+1)*2+2.5+4},{5*s+2})\n\t({(p-1)*2},0) to [short] ({(p+1)*2},0)\n\t({(p+1)*2},0) to [short, l_=0V] ({(p+1)*2+5+4},0);\n\\draw[red]\n\t({2*(p+1)+1},{((s-1)*5+4)}) to [generic, l_=BMS, /tikz/circuitikz/bipoles/length=5cm] ({2*(p+1)+1},4)\n;\\draw[green]\n\t({(p+1)*2+2.5+4},{(5*s+2)}) to [vR, /tikz/circuitikz/bipoles/length=5cm, l_=ESC] ({(p+1)*2+2.5+4},{4*s})\n\t({(p+1)*2+4},{4*s}) to [] ({(p+1)*2+9},{4*s});\n\\draw[blue]\n\t({(p+1)*2+4},{4*s}) to [transmission line, /tikz/circuitikz/bipoles/length=10cm] ({(p+1)*2+4},0)\n\t({(p+1)*2+5+4},{4*s}) to [transmission line, /tikz/circuitikz/bipoles/length=10cm, l_=Motors] ({(p+1)*2+5+4},0);\n')
   for i in range(1, s+1):
       outfile.write('\\draw\n\t')
       if i < s:
           outfile.write(f'({p-1},{i*5}) to [short, l_={2.9*i:.1f}V - {4.2*i:.1f}V] ({p-1},{5*(i-1)+4})\n\t')
       else:
           outfile.write(f'({p-1},{i*5+2}) to [short] ({p-1},{5*(i-1)+4})\n\t')
       outfile.write(f'(0,{(i-1)*5+4}) to [short, l_=Group {i}] ({(p-1)*2},{5*(i-1)+4})\n\t')
       outfile.write(f'to [american voltage source] ({(p-1)*2},{(i-1)*5})\n\t')
       outfile.write(f'(0,{(i-1)*5+4}) to [american voltage source, l_=2.9V - 4.2V] (0,{(i-1)*5})\n\t')
       outfile.write(f'to [short] ({(p-1)*2},{(i-1)*5});\n\t')
       outfile.write('\\draw[red]\n\t')
       outfile.write(f'({(p-1)*2},{(i-1)*5+4}) to [short] ({2*(p+1)+1},{(i-1)*5+4});\n\t')
       outfile.write('\\draw\n\t')
       for j in range(1, p-1):
           outfile.write(f'({2*j},{(i-1)*5+4}) to [american voltage source] ({2*j},{(i-1)*5})\n\t')
       outfile.write(';')

   outfile.write('\\end{circuitikz}\n\\end{center}\n}\n\\end{document}\n')

# main(50,50,'diagram.tex') # for use as a stand alone program
