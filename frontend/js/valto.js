//const myUrl = "http://127.0.0.1";
const myUrl = "http://azenhazam.mywire.org";

//restadat
var id = [];
var penznem = [];
var arfolyam = [];
var valutanevek = [];


var myTableArray =[ ["trial00", "Euro", "EUR"],
                    ["trial01", "USA dollár", "USD"],
                    ["trial02", "angol font", "GBP"],
                    ["trial03", "svájci frank", "CHF"],
                    ["trial04", "japán jen", "JPY"],
                    ["trial05", "román lej", "RON"],
                    ["trial06", "szerb dinár", "RSD"],
                    ["trial07", "cseh korona", "CZK"],
                    ["trial08", "lengyel zloty", "PLN"],
                    ["trial09", "orosz rubel", "RUB"],
                    ["trial10", "kínai jüan", "CNY"],
                ];


var arrayData = [[]];


function szamol(){
    const mirol = document.querySelector("#inputSelect").value;
    const mire = document.querySelector("#outputSelect").value;
    var mennyit = parseFloat(document.querySelector("#mennyi").value);
    const euroid = penznem.indexOf("EUR");
    const forintid = penznem.indexOf("HUF");

    var hiba = "";
    isNaN(mennyit) ? hiba = "Nem értelmezhető a mennyiség!" : "";
    if (mennyit < 0) {
        hiba = `Biztos ezt akartad? Én nem ${mennyit} számolok, hanem ${Math.abs(mennyit)}!`;
        mennyit = Math.abs(mennyit);
    }

    // 1 USA dollár = EUR/USD*HUF = 401.6 forint
    keresem = arfolyam[euroid] / arfolyam[id.indexOf(parseInt(mirol))] * arfolyam[id.indexOf(parseInt(mire))];
    visszefelekeresem = arfolyam[euroid] / arfolyam[id.indexOf(parseInt(mire))] * arfolyam[id.indexOf(parseInt(mirol))];

    odaforint = parseFloat((arfolyam[euroid] / arfolyam[id.indexOf(parseInt(mirol))] * arfolyam[forintid] * mennyit).toFixed(4));
    
    document.querySelector(".valtas0sor").innerHTML = hiba;
    document.querySelector(".valtas1sor").innerHTML = mennyit.toLocaleString('hu-HU') + " " + penznem[id.indexOf(parseInt(mirol))] + " - " + valutanevek[id.indexOf(parseInt(mirol))] + " =";
    document.querySelector(".valtas2sor").innerHTML = parseFloat((mennyit * keresem).toFixed(4)).toLocaleString('hu-HU') + " " + penznem[id.indexOf(parseInt(mire))] + " - " + valutanevek[id.indexOf(parseInt(mire))];
    document.querySelector(".valtas3sor").innerHTML = "1 " + penznem[id.indexOf(parseInt(mirol))] + " = " + keresem.toLocaleString('hu-HU') + " " + penznem[id.indexOf(parseInt(mire))] + "<br>" + "1 " + penznem[id.indexOf(parseInt(mire))] + " = " + visszefelekeresem.toLocaleString('hu-HU') + " " + penznem[id.indexOf(parseInt(mirol))];
    
    odaforint * 0.009 < 34900 ? illetek = odaforint * 0.009 : illetek = 34900;
    isNaN(odaforint) ? illetek = 0 : illetek = illetek;
 
    document.querySelector(".valtas4sor").innerHTML = `
        <b style="color:red"> ${illetek.toLocaleString('hu-HU')} HUF</b> a kezelési költség!<br>
    `;
}


function getValutaadatok(){
    document.querySelector("#inputSelect").innerHTML = "";
    document.querySelector("#outputSelect").innerHTML = "";

    fetch(`${myUrl}:8800/restadat`).then(res=>res.json()).then(result=>{
        result.forEach(item => {
            item.penznem == "EUR" ? document.querySelector("#inputSelect").innerHTML +=`<option value = "${item.id}" selected>${item.valutanevek} - (${item.penznem})</option>` : document.querySelector("#inputSelect").innerHTML +=`<option value = "${item.id}">${item.valutanevek} - (${item.penznem})</option>`;
            
            item.penznem == "HUF" ? document.querySelector("#outputSelect").innerHTML +=`<option value = "${item.id}" selected>${item.valutanevek} - (${item.penznem})</option>` : document.querySelector("#outputSelect").innerHTML +=`<option value = "${item.id}">${item.valutanevek} - (${item.penznem})</option>`;

            id.push(item.id);
            penznem.push(item.penznem);
            arfolyam.push(item.arfolyam);
            valutanevek.push(item.valutanevek);
        });
    })
}


// diagram.html fetch get valuta to chart
function getChartadatok(){
    valuta = [];
    arrayData = [[]];
    fetch(`${myUrl}:8800/valuta`).then(res=>res.json()).then(result=>{
        result.forEach(item => {

            //minden adat arrayData tömbe
            arrayData.push([item.date, item.currency, item.value]);

        })})

        .finally(function () {

            // a fix devizák a table be
            let fgAdatArrayx = [];
            let fgAdatArrayy = [];
            s = 0;
            for (let i = 0; i < myTableArray.length; i++){
                if (s != i){
                    s = i;
                    fgAdatArrayx = [];
                    fgAdatArrayy = [];
                }

                for(let j=0; j < arrayData.length; j++){
                    if(arrayData[j][1] == myTableArray[i][2]){
                        fgAdatArrayx.push(arrayData[j][0]);
                        fgAdatArrayy.push(arrayData[j][2]);
                    }
                }
                myValutaChartWrite(fgAdatArrayx, fgAdatArrayy, myTableArray[i][0], myTableArray[i][2], );
            }

            // select fill
            chartSelectFill('chartSelect00');
            chartSelectFill('chartSelect01');
        })
};


//diagram.html onLoad
function myValutaChart(){
    //diagram.html -> table row    
    for (let i = 0; i < myTableArray.length; i++){
        myValutaChartTable(myTableArray[i][0], myTableArray[i][1], myTableArray[i][2]); 
    }
    // backend/valuta
    getChartadatok(); 
} 


//diagram.html fill select input
function chartSelectFill(selectId){
    let shortName = [];
    document.querySelector(`#${selectId}`).innerHTML = "<option value = '' selected></option>";
    
    arrayData.forEach((i) =>{
        if (!shortName.includes(i[1])){
            shortName.push(i[1]);
            document.querySelector(`#${selectId}`).innerHTML +=`<option value = ${i[1]}>${i[1]}</option>` ;
        }
    })
}


function selectChangeChart(canvastId, selectId){
    let fgAdatArrayx = [];
    let fgAdatArrayy = [];
    let smalName =document.querySelector(`#${selectId}`).value;

    for(let j=0; j < arrayData.length; j++){
        if(arrayData[j][1] == smalName){
            fgAdatArrayx.push(arrayData[j][0]);
            fgAdatArrayy.push(arrayData[j][2]);
        }
    }

    let chartStatus = Chart.getChart(canvastId); 
    if (chartStatus != undefined) {
        chartStatus.destroy();
    }
    myValutaChartWrite(fgAdatArrayx, fgAdatArrayy, canvastId, smalName);
}


//diagram.html table new rows
function myValutaChartTable(tablerowid, longName, sign){
    document.querySelector("#myChartDataTables").innerHTML += `
        <tr>
            <td class="h1 text-end" width="40%"><br>${longName}</td>
            <td class="h1 text-center" width="10%"><br>${sign}</td>
            <td width="50%"><canvas id=${tablerowid} style="width:100%;max-height:200px"></canvas>
        </tr>
    `;
}
    

function myValutaChartWrite(xValues, yValues, myChart, myChartLabel){
    const piros =  ["rgba(205,  65,  55, 1.0)", "rgba( 240, 150, 140, 0.1)"]
    const zold  =  ["rgba( 25, 105,  60, 1.0)", "rgba(  46, 204,  25, 0.1)"]
    const kek  =   ["rgba(  0,   0, 255, 1.0)", "rgba(   0,   0, 255, 0.1)"]
    const sarga  = ["rgba(240, 195,  15, 1.0)", "rgba( 250, 220, 110, 0.1)"]

    yValues[yValues.length - 1] - yValues[yValues.length - 2] > 0 ? szin = piros : szin = zold;

    new Chart(myChart, {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                label: myChartLabel,  
                fill: false,
                lineTension: 0,
                backgroundColor: szin[0],
                borderColor: szin[1],
                data: yValues
            }]
        },
        options: {
            legend: {display: false},
            scales: {
                x: {display: false,},
                y: {display: true,},
            }
        }
    });

}