// Author: Abid Hussain @abidhussain1997
// Date: 01/09/2017

$(document).ready(function(){


  var instructionArr = [];
  $('#addressTxtBox').focus();
  $('#btnnext').click(function(){
    var address = $('#addressTxtBox').val()
    var nextAddr = parseInt(address) + 1
    var instruction = $('#instructionTxtBox').val()
    var arrElement = address + " " + instruction;
    console.log(arrElement)
    instructionArr.push(arrElement);
    console.log(instructionArr);
    $('#addressTxtBox').val(nextAddr);
    $('#instructionTxtBox').val("");
    $('#instructionTxtBox').focus();
  })

  $('#btnreset').click(function(){
    $.ajax({
      type: 'POST',
      url: '',
      data: {instructionArr:instructionArr},
      datatype:'json',
      encode: true
    }).done(function(){
      console.log("done");
    })
  })
})
