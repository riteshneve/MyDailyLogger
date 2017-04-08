$(document).ready(function() {
		var title = {
			text: ''
		}
	   var chart = {
		   plotBackgroundColor: null,
		   plotBorderWidth: null,
		   plotShadow: false
	   };  
	   var tooltip = {
		  pointFormat: '<b>{point.percentage:.1f}%</b>'
	   };
	   var plotOptions = {
		  pie: {
			 allowPointSelect: true,
			 cursor: 'pointer',
			 dataLabels: {
				enabled: true,
				format: '<b>{point.name}</b>: {point.percentage:.1f} %',
				style: {
				   color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
				}
			 }
		  }
	   };
	   var series= [{
		  type: 'pie',
		  name: 'Browser share',
		  data: [
			 ['To Do',   {{targetKMs - doneKMs}}],
			 {
				name: 'Done',
				y: {{doneKMs}},
				sliced: true,
				selected: true
			 }
		  ]
	   }];     
		  
	   var json = {};   
	   json.chart = chart; 
	   json.tooltip = tooltip;  
	   json.series = series;
	   json.title = title;
	   json.plotOptions = plotOptions;
	   $('#pieChartContainer').highcharts(json);
	   
	//Line chart starts here
	var chart = {
      type: 'spline'      
   }; 
   var title = {
      text: ''   
   };
   var xAxis = {
      type: 'datetime',
      dateTimeLabelFormats: {
         month: '%e. %b',
         year: '%b'
      },
      title: {
         text: 'Date'
      }
   };
   var yAxis = {
      title: {
         text: 'KMs'
      },
      min: 0
   };
   var tooltip = {
      pointFormat: '{point.x:%e. %b}: {point.y:.2f} KM'
   };
   var plotOptions = {
      spline: {
         marker: {
            enabled: true
         }
      }
   };
   var series= [{
         name: 'Daily KMs',
         data: {{dailyKMsData}}
      }];     
      
   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.xAxis = xAxis;
   json.yAxis = yAxis;  
   json.series = series;
   json.plotOptions = plotOptions;
	   $('#lineChartContainer').highcharts(json);
	   
	   
	//Column chart starts here
	var chart = {
      type: 'column'
   };
   var title = {
      text: ''   
   };
   var xAxis = {
      //categories: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
      crosshair: true
   };
   var yAxis = {
      min: 0,
      title: {
         text: ''         
      }
   };
   var tooltip = {
      headerFormat: '<span style="font-size:10px">Week {point.key}</span><table>',
      pointFormat: '<tr>' +
         '<td style="padding:0"><b>{point.y:.1f} KM</b></td></tr>',
      footerFormat: '</table>',
      shared: true,
      useHTML: true
   };
   var plotOptions = {
      column: {
         pointPadding: 0,
         borderWidth: 0
      }
   };
   var credits = {
      enabled: false
   };
   
   var series= [{
        name: 'KMs',
            data: {{weeklyKMsData}}
        }];     
      
   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.series = series;
   json.plotOptions = plotOptions;
   json.credits = credits;
   $('#columnChartContainer').highcharts(json);
   
   
   
   var chart = {
      type: 'column'
   };
   var title = {
      text: ''   
   };    
   var xAxis = {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
   };
   var yAxis ={
      min: 0,
      title: {
        text: 'KMs'
      },
      stackLabels: {
        enabled: false,
        style: {
           fontWeight: 'bold',
           color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
        }
      }
   };
   var tooltip = {
      formatter: function () {
         return '<b>' + this.x + '</b><br/>' +
            this.series.name + ': ' + this.y + '<br/>' +
            'Total: ' + this.point.stackTotal;
      }
   };
   var plotOptions = {
      column: {
         stacking: 'normal',
         dataLabels: {
            enabled: false,
            color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
            style: {
               textShadow: '0 0 3px black'
            }
         }
      }
   };
   var credits = {
      enabled: false
   };
   var series= [{
        name: 'Week1',
            data: {{monthlyKMsData[0]}}
        }, {
            name: 'Week2',
            data: {{monthlyKMsData[1]}}
        }, {
            name: 'Week3',
            data: {{monthlyKMsData[2]}}
        }, {
            name: 'Week4',
            data: {{monthlyKMsData[3]}}
        }, {
            name: 'Week5',
            data: {{monthlyKMsData[4]}}
        }, {
            name: 'Week6',
            data: {{monthlyKMsData[5]}}
        }];
      
   var json = {};   
   json.chart = chart; 
   json.title = title;   
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   //json.legend = legend;
   json.tooltip = tooltip;
   json.plotOptions = plotOptions;
   json.credits = credits;
   json.series = series;
   $('#stackedColumnContainer').highcharts(json);
});
