# from pathlib import Path, PureWindowsPath

# carpeta = Path('C:/Users/rafae/OneDrive/Escritorio/pyfiles/nueva/otroarchivo.txt')
# rutaw = PureWindowsPath(carpeta)
#
# if carpeta.exists():
#     # print(carpeta.read_text())
#     print(carpeta)
#
# print(rutaw)


# from pathlib import Path
#
#
# base = Path.home()
# directorio_base = Path('/Developer/Python/docs')
# guia = Path(directorio_base, 'Europa')
#
# for txt in guia.glob('**/*.txt'):
#     print(txt)

# guia = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
#
# en_europa = guia.relative_to(Path('Europa'))
# en_espania = guia.relative_to(Path('Europa', 'España'))
#
# print(en_europa)
# print(en_espania)


from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)