function doPost(event){
  let request_data =JSON.parse(event.postData.contents);
  let status = addDailyRow(request_data.task,request_data.remarks,request_data.eodStatus)
  return ContentService.createTextOutput(JSON.stringify(status)).setMimeType(ContentService.MimeType.JSON);; 

}
function addDailyRow(task, remarks, eodStatus) {

  if(task == undefined){
    task = "task",
    remarks = "remarks"
    eodStatus = "Done"
  }

  // open the sheet
  let spreadsheet = SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1Uhpy0pgrRihGNpu4VFRnrIKpymuOi-Eya0Vorhw75Fc/edit")
  let sheet = spreadsheet.getSheetByName("Sheet1")
  
  // Get the current date
  var date = new Date();
  
  // Format the date as needed, e.g., "MM/dd/yyyy"
  var formattedDate = Utilities.formatDate(date, Session.getScriptTimeZone(), "dd/MM/yyyy");
  
  // Get the range of data in the sheet
  var dataRange = sheet.getDataRange();
  var data = dataRange.getValues();
  
  // Check if the date already exists in the sheet
  var dateExists = false;
  for (var i = 1; i < data.length; i++) { // start from 1 to skip header row
    if (data[i][0] === formattedDate) {
      dateExists = true;
      break;
    }
  }
  
  if (!dateExists) {
    // Add the new row with the date and the first task
    sheet.appendRow([formattedDate, task, remarks, eodStatus]);
  
  } else {
    // Add a new row with the task, remarks, and EOD status, but leave the date empty
    sheet.appendRow(["", task, remarks, eodStatus]);
  }

  let send_this = {
    status:"done"
  }

  return send_this
}