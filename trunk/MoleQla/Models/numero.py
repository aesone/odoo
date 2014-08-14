from openerp.osv import fields, osv

class numero(osv.osv):
    
    _name = "numero"
    _description = "Numero"
    
    def _articulos_default(self, cr ,uid,ids, context=None):
        obj= self.pool.get('articulo')
        ides= obj.search(cr, uid, [('state', '=', 'published')])
        obj.write(cr, uid, ids, {'numero_id' : ids})
        return ides
    
    _columns = {
        'nombre' : fields.char('Nombre', size=128, required=True),
        'numero' : fields.integer('Numero',),
        'articulos_id' : fields.one2many('articulo', 'numero_id','Articulos'),
        'fecha_p' : fields.date('Fecha de Publicacion'),
        'state':fields.selection([('start', 'Borrador'), ('builded', 'En construccion'),('send', 'Publicada'), ('voted', 'En votacion'),('closed', 'Cerrado')], 'Estado del numero'),
        }
    
    _defaults = {
                  'state':'start',
                  }
    
    def build(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'builded'})
        obj= self.pool.get('articulo')
        ides= obj.search(cr, uid, [('state', '=', 'published')])
        #for id in ides:
        obj.write(cr, uid, ides, {'numero_id' : ids[0]})
    
    def send(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'send',  })
        
    def vote(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'voted'})
        
    def close(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'closed'})
            
       
       
        
numero()