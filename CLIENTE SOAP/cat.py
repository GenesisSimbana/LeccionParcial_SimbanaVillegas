import zeep
from zeep.transports import Transport
from requests import Session

# URL del servicio SOAP
url = 'http://localhost:22506/CategoryService.asmx?WSDL'

# Deshabilitar la verificación del certificado SSL
session = Session()
session.verify = False  # No verificar el certificado SSL

# Crear un transporte con la sesión modificada
transport = Transport(session=session)

# Crear el cliente SOAP usando la URL del WSDL y el transporte
client = zeep.Client(url, transport=transport)

# Método para obtener todas las categorías
def obtener_categorias():
    try:
        # Llamada al método "GetAllCategories" del servicio SOAP
        categorias = client.service.GetAllCategories()
        
        # Mostrar las categorías obtenidas
        for categoria in categorias:
            print(f"ID: {categoria.CategoryID}, Nombre: {categoria.CategoryName}, Descripción: {categoria.Description}")
    except Exception as e:
        print(f"Error al obtener categorías: {e}")

# Método para obtener una categoría por ID
def obtener_categoria_por_id(id_categoria):
    try:
        # Llamada al método "GetCategoryById" del servicio SOAP
        categoria = client.service.GetCategoryById(id_categoria)
        
        # Mostrar la categoría obtenida
        print(f"ID: {categoria.CategoryID}, Nombre: {categoria.CategoryName}, Descripción: {categoria.Description}")
    except Exception as e:
        print(f"Error al obtener categoría por ID: {e}")

# Método para agregar una nueva categoría
def agregar_categoria(nombre, descripcion):
    try:
        # Crear un objeto de categoría serializable
        categoria = {'CategoryName': nombre, 'Description': descripcion}
        
        # Llamada al método "CreateCategory" del servicio SOAP
        client.service.CreateCategory(categoria)
        
        print(f"Categoría '{nombre}' agregada con éxito.")
    except Exception as e:
        print(f"Error al agregar categoría: {e}")

# Método para actualizar una categoría existente
def actualizar_categoria(id_categoria, nombre, descripcion):
    try:
        # Crear un objeto de categoría serializable
        categoria = {'CategoryID': id_categoria, 'CategoryName': nombre, 'Description': descripcion}
        
        # Llamada al método "UpdateCategory" del servicio SOAP
        client.service.UpdateCategory(categoria)
        
        print(f"Categoría con ID {id_categoria} actualizada con éxito.")
    except Exception as e:
        print(f"Error al actualizar categoría: {e}")

# Método para eliminar una categoría
def eliminar_categoria(id_categoria):
    try:
        # Llamada al método "DeleteCategory" del servicio SOAP
        client.service.DeleteCategory(id_categoria)
        
        print(f"Categoría con ID {id_categoria} eliminada con éxito.")
    except Exception as e:
        print(f"Error al eliminar categoría: {e}")
        
# Llamada de ejemplo para obtener todas las categorías
# obtener_categorias()

# Llamada de ejemplo para obtener una categoría por ID
# obtener_categoria_por_id(2)

# Llamada de ejemplo para agregar una categoría
agregar_categoria("queeverga", "Categoría para PRUEBAS")

# Llamada de ejemplo para actualizar una categoría (usando un ID ficticio)
# actualizar_categoria(2, "Electrónica NUEVA", "AYUDA electrónicos de última tecnología")

# Llamada de ejemplo para eliminar una categoría (usando un ID ficticio)
# eliminar_categoria(1013)
