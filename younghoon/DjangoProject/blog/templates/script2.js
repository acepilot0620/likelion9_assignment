        //<!--1.막대그래프-->
        google.charts.load("current", {packages:['corechart']});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
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
            title: "아파트 평균 매매금액",
            width: 500,
            height: 400,
            bar: {groupWidth: "80%"},
            legend: { position: "none" },
        };
        var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
        chart.draw(view, options);
         }