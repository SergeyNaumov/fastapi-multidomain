function check_form(self){
    let exists_errors=false
    for(let f of self.check_fields){
      if('check' in f){
        let v=self[f.name], err=f.check(v)
        if(err){
          self.error[f.name]=err, exists_errors=true
        }
      }
    }
    return exists_errors
}

function init_capcha(self){
    axios.get('/capcha?action=out_key&json=1').then(
        r=>{
            let data=r.data; self.form_capture_key=data.capture_key; self.form_capture_src=data.capture_src;
        }
    )
}
function clear_errors(self){
    for(let e in self.error ){
        self.error[e]=''
    }
}
let func_not_empty=function(v){return v?'':'поле не заполнено'};