from openerp.osv import fields, osv

class votacion(osv.osv):
    
    _name = "votacion"
    _description = "Votacion"
    
    _columns = {       
        'user_id': fields.integer('Usuario'),
        'lineas_votacion': fields.one2many('linea_votacion', 'votacion_id','Articulos'), 
        'state':fields.selection([('start', 'Pendiente'), ('send', 'Confirmado')], 'Estado del proceso'),
        }
    
    _defaults = {
        'state' : 'start'
                 }
       
votacion()