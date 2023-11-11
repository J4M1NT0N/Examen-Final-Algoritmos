import openpyxl
wb = openpyxl.Workbook()
hoja = wb.active
print(f"Mantenimiento: {hoja.title}")

hoja.title = "Valores"
print(f"Mantenimiento: {wb.active.title}")

def Crear_vehiculos(self):
    codigo = self.codigo.get()
    marca = self.marca.get()
    modelo = self.modelo.get()
    kilometraje = self.kilometraje.get()
    precio = self.precio.get()
    datos = (modelo, kilometraje, marca, precio)
    if codigo and modelo and kilometraje and marca and precio != '':
        self.tabla.insert('', 0, text=codigo, values=datos)
        self.base_datos.inserta_producto(codigo, modelo, kilometraje, marca, precio)
        
    def editar_registro(self):
        codigo = self.codigo.get()
        modelo = self.modelo.get()
        kilometraje = self.kilometraje.get()
        marca = self.marca.get()
        precio = self.precio.get()
        datos = (modelo, kilometraje, marca, precio)
        if codigo and modelo and kilometraje and marca and precio != '':
            self.tabla.item(self.tabla.selection(), values=datos)
            self.base_datos.edita_producto(
                codigo, modelo, kilometraje, marca, precio)
        
    def eliminar_vehiculo(self):
        fila = self.tabla.selection()
        if len(fila) != 0:
            self.tabla.delete(fila)
            codigo = self.codigo_borrar
            self.base_datos.elimina_productos(codigo)
            
