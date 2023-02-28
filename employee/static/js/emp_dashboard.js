document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) => {
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
        // show navbar
        nav.classList.toggle('show')
        // change icon
        toggle.classList.toggle('bx-x')
        // add padding to body
        bodypd.classList.toggle('body-pd')
        // add padding to header
        headerpd.classList.toggle('body-pd')
        })
        }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });


    function editData(id) {
        $.ajax({
            url:"edit_data",
            type:"post",
            data: {
                'id': id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },            
    
            success: function(response) {
                console.log(response.data)
                $('#id').val(response.data.id)
                $('#e_id').val(response.data.id)
                $('#plan').val(response.data.plan)
                $('#car_name').val(response.data.car_name)
                $('#phone').val(response.data.phone)
                $('#destination').val(response.data.destination)
                $('#washing_date').val(response.data.washing_date)
                $('#hour').val(response.data.hour)
                $('#minute').val(response.data.minute)
                $('#ampm').val(response.data.ampm)
                $('#message').val(response.data.message)
                $('#status').val(response.data.status)
    
            }
        })
    }
    

    function delete_booking(id){
        $.ajax({
            url:"delete_booking",
            type:"post",
            data: {
                'id': id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },            
    
            success: function(response) {
                console.log(response.data)
                document.getElementById('cancel_booking_btn').href='cancel_booking/'+response.data.id
    
            }
        })    
    
    }