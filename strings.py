html_producto = '''
<p>
<div class="card" style="width: 18rem;">
  <div class="card-body" style="overflow:auto">
    <h5 class="card-title">{}</h5>
    <p class="card-text">{}</p>
    <p class="card-text">Precio: Bs. {}</p>
    <p class="card-text">Quedan {} unidades</p>
    <form method="POST" action="/editar" style="display: inline-block;">
      <input type="hidden" value="{}" name="id_producto">
      <button type="submit" class="btn btn-success">Editar</button>
    </form>
    <form method="POST" action="/borrar" style="display: inline-block;">
      <input type="hidden" value="{}" name="id_producto">
      <button type="submit" class="btn btn-danger">Borrar</button>
    </form>
  </div>
</div>
</p>
'''

html_producto_input = '''
<p>
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
        <input type="text" class="form-control" value="{}" aria-label="nombre" aria-describedby="addon-wrapping" name="nombre">
      </div>
      <br>
      <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text">Descripción</span>
      </div>
        <textarea class="form-control" aria-label="With textarea" name="descripcion">{}</textarea>
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
                <input type="hidden" value="{}" name="id_producto">
                <a href="/">
                  <input type="{}" value="Cancelar" class="btn btn-secondary"/>
                </a>
                <input type="submit" class="btn btn-primary" value="Guardar">
            </form>   
  </div>
</div>
</p>
'''

html_encontrado = '''

'''