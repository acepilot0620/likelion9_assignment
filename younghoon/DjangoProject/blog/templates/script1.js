        //<!--2.막대그래프-->
        google.charts.load("current", {packages:['corechart']});
        google.charts.setOnLoadCallback(drawChart2);
        function drawChart2() {
        var data = google.visualization.arrayToDataTable([
            ["Element", "Density", { role: "style" } ],
            ["2016", 8.94, "#b87333"],
            ["2017", 10.49, "silver"],
            ["2018", 19.30, "gold"],
            ["2019", 21.45, "color: #e5e4e2"],
            ["2020", 21.45, "color: green"]
        ]);

        var view = new google.visualization.DataView(data);
        view.setColumns([0, 1,
                        { calc: "stringify",
                            sourceColumn: 1,
                            type: "string",
                            role: "annotation" },
                        2]);

        var options = {
            title: "아파트 평당 매매 금액",
            width: 500,
            height: 400,
            bar: {groupWidth: "80%"},
            legend: { position: "none" },
        };
        var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values2"));
        chart.draw(view, options);
        }

    

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'rising rate', '금리'],
          ['2016',  2,      1.25],
          ['2017',  1,      1.5],
          ['2018',  3,       1.75],
          ['2019',  4,      1.25],
          ['2020',  3,      0.5]
        ]);

        var options = {
          title: '전년도 대비 아파트 매매 상승률(금리비교)',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
 