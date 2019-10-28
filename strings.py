html_producto = '''
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{}</h5>
    <p class="card-text">{}</p>
    <p class="card-text">Precio: Bs. {}</p>
    <p class="card-text">Quedan {} unidades</p>
    <button type="button" class="btn btn-success">Editar</button>
    <button type="button" class="btn btn-danger">Borrar</button>
  </div>
</div>
'''

html_producto_input = '''
<div class="card">
  <div class="card-header">
    {}
  </div>
  <div class="card-body">
    <form method="POST" action="/">
                <div class="input-group flex-nowrap">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="addon-wrapping">Nombre</span>
                    </div>
                    <input type="text" class="form-control" value="{}" aria-label="nombre"
                        aria-describedby="addon-wrapping" name="nombre">
                </div>
                <br>
                <div class="input-group">
                        <div class="input-group-prepend">
                          <span class="input-group-text">Descripción</span>
                        </div>
                        <textarea class="form-control" value="{}" aria-label="With textarea" name="descripcion"></textarea>
                      </div>
                <br>
                <div class="input-group flex-nowrap">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="addon-wrapping">Precio</span>
                    </div>
                    <input type="text" class="form-control" value="{}" aria-label="precio"
                        aria-describedby="addon-wrapping" name="precio">
                </div>
                <br>
                <div class="input-group flex-nowrap">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="addon-wrapping">Stock</span>
                    </div>
                    <input type="text" class="form-control" value="{}" aria-label="stock"
                        aria-describedby="addon-wrapping" name="stock">
                </div>
                <br>
                <input type="{}" class="btn btn-secondary" value="Cancelar">
                <input type="submit" class="btn btn-primary" value="Guardar">
            </form>
  </div>
</div>
'''