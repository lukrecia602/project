//Ez a metódus részben felel a küldésnél található legördülő lista dinamikus változtatásáért. 
function copySelectValue() {
    var fromCurrency = document.getElementById("to_currency").value;
    var toCurrency = document.getElementById("kuldendopm");
    toCurrency.value = fromCurrency;
}