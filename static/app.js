$(".btn-primary").click(function (e) {
  console.log("event is", e);
  e.preventDefault(), submitCupcake(e);
});

// $('.btn-primary').click(getCupcake)

function appendCupcake(response) {
    
    $('ul').append(`<li>
    <img src=${response.data.cupcake.image}></img>
    <h3>${response.data.cupcake.flavor}</h3>
    <div>
    <p>Size: ${response.data.cupcake.size}</p> 
    <p>Rating: ${response.data.cupcake.rating}</p> 
    </div>
    </li>`)
}

function clearForm() {
    $('form').find('input').val('')
}

// submitCupcake
async function submitCupcake(event) {
  console.log("getCupcake");
  let requestData = {}
  for (const input of event.target.form) {
    if(input.value != '') {
        requestData[input.name] = input.value
    }
  }
//   console.log('reqdata',requestData)
  response = await axios.post("/api/cupcakes", requestData);
//   console.log(response);
  clearForm()
  appendCupcake(response)
}

