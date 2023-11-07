from rembg import remove
from PIL import Image
"""import os
print(os.getcwdb())"""

# Criar uma variável com local do arquivo que vamos abrir e, salvar sem fundo (PNG):
# Precisei utilizar duas baras "\\", uma representa o ESCAPE da outra do endereços:
local_image = 'C:\\Users\\User\\OneDrive\\_Graphic Design\\_Myself\\_Photos\\piscina.jpg'
local_to_save = 'C:\\Users\\User\\OneDrive\\_Graphic Design\\_Myself\\_Photos\\BG_pyhton.png'

# Solicitar abertura do arquivo e, remoção:
open_image = Image.open(local_image)
remove_background = remove(open_image)

# Salvando arquivo sem fundo:
remove_background.save(local_to_save)