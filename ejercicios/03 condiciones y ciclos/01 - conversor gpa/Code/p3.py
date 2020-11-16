# Pregunta 2.a. C2 2015-I.

def convertir_eeuu(nota):
    
  # Procedimiento:
  if nota >= 90 and nota <= 100:
      return 'A'
  elif nota >= 70 and nota < 90:
      return 'B'
  elif nota >= 55 and nota < 70:
      return 'C'
  elif nota >= 0 and nota < 55:
      return 'F'
  else:
      print 'Error, la nota no es valida'
      return None

# Pregunta 2.b. C2 2015-I.

def convertir_gpa(nota):

  # Procedimiento:
  if nota == 'A':
      return 4.0
  elif nota == 'B':
      return 3.0
  elif nota == 'C':
      return 2.0
  elif nota == 'F':
      return 0.0
  else:
      print 'Error, nota GPA no valida'
      return None

# Pregunta 2.c. C2 2015-I.
# Programa:
minimo   = 1000
min_ramo = '' 

programacion  = int(raw_input('Nota de Programacion: '))
progra_eeuu   = convertir_eeuu(programacion)
progra_gpa    = convertir_gpa(progra_eeuu)
print 'EE.UU: ' + str(progra_eeuu)
if progra_gpa < minimo:
  minimo   = progra_gpa
  min_ramo = 'progra'
    
matematicas   = int(raw_input('Nota de Matematicas: '))
mate_eeuu     = convertir_eeuu(matematicas)
mate_gpa      = convertir_gpa(mate_eeuu)
print 'EE.UU: ' + str(mate_eeuu)
if mate_gpa < minimo:
  minimo    = mate_gpa
  min_ramo  = 'mate'

fisica        = int(raw_input('Nota de Fisica: '))
fisica_eeuu   = convertir_eeuu(fisica)
fisica_gpa    = convertir_gpa(fisica_eeuu) 
print 'EE.UU: ' + str(fisica_eeuu)
if fisica_gpa < minimo:
  minimo    = fisica_gpa
  min_ramo  = 'fisica'

if min_ramo == 'progra':
  pgpa = (5.0 * mate_gpa + 3.0 * fisica_gpa) / 8.0
elif min_ramo == 'mate':
  pgpa = (3.0 * progra_gpa + 3.0 * fisica_gpa) / 6.0
else:
  pgpa = (3.0 * progra_gpa + 5.0 * mate_gpa) / 8.0
  
print 'PGPA: ' + str(pgpa)
