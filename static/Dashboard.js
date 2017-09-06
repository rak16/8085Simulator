// Author: Abid Hussain @abidhussain1997
// Date: 01/09/2017

$(document).ready(function(){
  var instructionArr = [];
  $("#addressTxtBox").attr("disabled", "disabled")
  $("#instructionTxtBox").attr("disabled", "disabled")

  $("#btnreset").click(function() {
    $("#addressTxtBox").attr("disabled", "disabled")
    $("#instructionTxtBox").attr("disabled", "disabled")
  })

  //on click function of memory Button
  $("#btnmem").click(function() {
    $("#addressTxtBox").removeAttr("disabled")
    $("#instructionTxtBox").removeAttr("disabled")
    $('#addressTxtBox').focus();
  })

  //on click function of next Button
  $('#btnnext').click(function() {
    var address = $('#addressTxtBox').val()
    var instruction = $('#instructionTxtBox').val()
    if (address == "" && instruction == "") {
      console.log("Inputs are Empty");
    } else {
      //inserting elements into the array and incrementing the address value
      var nextAddr = parseInt(address) + 1
      var arrElement = address + " " + instruction;
      console.log(arrElement)
      instructionArr.push(arrElement);
      console.log(instructionArr);
      $('#addressTxtBox').val(nextAddr);
      $('#instructionTxtBox').val("");
      $('#instructionTxtBox').focus();
    }
  })

  $('#btnexec').click(function() {
    $.ajax({
      type: 'POST',
      url: 'execute?ins_arr='+instructionArr,
      datatype:'json',
      encode: true
    }).done(function() {
      console.log("done");
    })
  })
})
