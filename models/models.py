# -*- coding: utf-8 -*-

from odoo import models, fields, api


SELECTION_STATE_LOT = [
    ('generado', 'En Venta'),
    ('reservado', 'Reservado'),
    ('pagado', 'Pagado'),
    ('ganador', 'Ganador'),
]

DESCRIPCION_RIFA = """
    <div>
        <b>Únete a la Rifa Pro-Salud Eliot</b> <br />
⭐ Por la Recuperación de nuestro hermano y amigo Eliot egresado de la UNI FIC⭐
Cada rifa está 10 soles y los premios son:
<ul>
<li>1er Premio: 01 Telescopio Mod. F700776, ampliación con lentes barlow</li>
<li>2do Premio: 01 Whisky Black Label Johnnie Walker 750 ml. </li>
<li>3er Premio: 01 Licuadora</li>
<li>4to Premio: 01 Micrófono para karaoke Ealsem, ES 1100</li>
<li>5to premio: 01 olla arrocera</li>
</ul>
<b>Sorteo:</b> 12 de marzo a través de Facebook live <br />
    </div>"""

class rifa(models.Model):
    _name = 'rifa.rifa'
    _description = 'rifa.rifa'



    ticket_number = fields.Char(string='Numero', readonly=True)
    description = fields.Text(default=DESCRIPCION_RIFA)
    state = fields.Selection(SELECTION_STATE_LOT,required=True, default='generado')
    name = fields.Char()
    email = fields.Char()
    telephone = fields.Char()
    address = fields.Char()
    winner = fields.Boolean()
    cost = fields.Integer(default=20)

    @api.model
    def create(self, vals):
        # Get next ticket number from the sequence
        vals['ticket_number'] = self.env['ir.sequence'].next_by_code('rifa.rifa')
        new_id = super(rifa, self).create(vals)       

        return new_id

    @api.multi
    def button_reservado(self):
        for rec in self:
            rec.write({'state': 'reservado'})
    
    @api.multi
    def button_pagado(self):
        for rec in self:
            rec.write({'state': 'pagado'})

    @api.multi
    def send_email(self):
        #Send an email out to everyone in the category
        notification_template_reservado = self.env['ir.model.data'].sudo().get_object('rifa', 'message_reservado')
        notification_template_pagado = self.env['ir.model.data'].sudo().get_object('rifa', 'message_pagado')
        values = {}
        for rec in self:
            if rec.state == 'reservado':
                values = notification_template_reservado.generate_email([self.id])[self.id]
            
            if rec.state == 'pagado':
                values = notification_template_pagado.generate_email([self.id])[self.id]
            if len(values)>0:
                values['body_html'] = values['body_html']
                values['email_to'] = my_user.partner_id.email

                send_mail = self.env['mail.mail'].create(values)
                send_mail.send()

                #Remove the message from the chatter since this would bloat the communication history by a lot
                #send_mail.mail_message_id.res_id = 0
