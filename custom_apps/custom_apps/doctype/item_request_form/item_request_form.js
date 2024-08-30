frappe.ui.form.on('Item Request Form', {
	
    item_code_generated: function(frm){
      if(frm.doc.item_code_generated == 'No' && frm.doc.item_code || frm.doc.remarks) {
          frm.set_value('item_code', null);
          frm.refresh_field('item_code');
          frm.set_value('remarks', null);
          frm.refresh_field('remarks');
      }
      if(frm.doc.item_code_generated == 'Yes' && frm.doc.remarks) {
          frm.set_value('remarks', null);
          frm.refresh_field('remarks');
      }
      if(frm.doc.item_code_generated == 'Already Created'){
          frm.set_value('remarks', 'Already Created');
          frm.refresh_field('remarks');
      }
  }
  })