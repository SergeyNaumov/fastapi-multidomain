if(document.getElementById('app_main')){
    let app_main=new Vue({
        el:'#app_main',
        data:{
            spoiler1_show:false,
            spoiler2_show:false,
            spoiler3_show:false
        }
    })
}
// 
if(document.getElementById('form_tasks')){

    let form_tasks_fields=[
        { 
          name:'header',
          check: func_not_empty
        },
        {
          name:'body',
          check: func_not_empty
        },
        {
          name:'priority',
          check:func_not_empty
        },
        {name:'form_capture_str',check:func_not_empty}
    ];

    

    let form_tasks=new Vue({
        el:'#form_tasks',
        data:{
           check_fields:form_tasks_fields,
           header:'',
           body:'',
           priority:false,
           error:{
            header:'',
            body:'',
            priority:''
           }

           
        },
        created(){
            this.init_capcha()
        },
        methods:{
            submit(){

            },
            init_capcha(){
                init_capcha(this)
            },
            form_check(){
                clear_errors(this)
                return check_form(this)
            }
        }

    })
}