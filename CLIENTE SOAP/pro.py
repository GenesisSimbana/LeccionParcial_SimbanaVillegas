import zeep
from zeep.transports import Transport
from requests import Session

# URL del servicio SOAP
url = 'http://localhost:22506/ProductService.asmx?WSDL'

# Deshabilitar la verificación del certificado SSL
session = Session()
session.verify = False  # No verificar el certificado SSL

# Crear un transporte con la sesión modificada
transport = Transport(session=session)

# Crear el cliente SOAP usando la URL del WSDL y el transporte
client = zeep.Client(url, transport=transport)

# Método para obtener todos los productos
def obtener_productos():
    try:
        # Llamada al método "GetAllProducts" del servicio SOAP
        productos = client.service.GetAllProducts()
        
        # Mostrar los productos obtenidos
        for producto in productos:
            print(f"ID: {producto.ProductID}, Nombre: {producto.ProductName}, Categoría ID: {producto.CategoryID}, Precio: {producto.UnitPrice}, Unidades en stock: {producto.UnitsInStock}")
    except Exception as e:
        print(f"Error al obtener productos: {e}")

# Método para obtener un producto por ID
def obtener_producto_por_id(id_producto):
    try:
        # Llamada al método "GetProductById" del servicio SOAP
        producto = client.service.GetProductById(id_producto)
        
        # Mostrar el producto obtenido
        print(f"ID: {producto.ProductID}, Nombre: {producto.ProductName}, Categoría ID: {producto.CategoryID}, Precio: {producto.UnitPrice}, Unidades en stock: {producto.UnitsInStock}")
    except Exception as e:
        print(f"Error al obtener producto por ID: {e}")

# Método para agregar un nuevo producto
def agregar_producto(nombre, categoria_id, precio, unidades_en_stock):
    try:
        # Crear un objeto de producto serializable
        producto = {'ProductName': nombre, 'CategoryID': categoria_id, 'UnitPrice': precio, 'UnitsInStock': unidades_en_stock}
        
        # Llamada al método "CreateProduct" del servicio SOAP
        client.service.CreateProduct(producto)
        
        print(f"Producto '{nombre}' agregado con éxito.")
    except Exception as e:
        print(f"Error al agregar producto: {e}")

# Método para actualizar un producto existente
def actualizar_producto(id_producto, nombre, categoria_id, precio, unidades_en_stock):
    try:
        # Crear un objeto de producto serializable
        producto = {'ProductID': id_producto, 'ProductName': nombre, 'CategoryID': categoria_id, 'UnitPrice': precio, 'UnitsInStock': unidades_en_stock}
        
        # Llamada al método "UpdateProduct" del servicio SOAP
        client.service.UpdateProduct(producto)
        
        print(f"Producto con ID {id_producto} actualizado con éxito.")
    except Exception as e:
        print(f"Error al actualizar producto: {e}")

# Método para eliminar un producto
def eliminar_producto(id_producto):
    try:
        # Llamada al método "DeleteProduct" del servicio SOAP
        client.service.DeleteProduct(id_producto)
        
        print(f"Producto con ID {id_producto} eliminado con éxito.")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        
# Llamada de ejemplo para obtener todos los productos
# obtener_productos()

# Llamada de ejemplo para obtener un producto por ID
# obtener_producto_por_id(2)

# Llamada de ejemplo para agregar un producto
# agregar_producto("CARO", 1, 15, 200)

# Llamada de ejemplo para actualizar un producto (usando un ID ficticio)
# actualizar_producto(4, "Producto Editado", 1, 150.75, 250)

# Llamada de ejemplo para eliminar un producto (usando un ID ficticio)
#eliminar_producto(1033)
